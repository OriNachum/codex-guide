#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import subprocess
import sys

NONE_FOUND = "- none"

def run_gh(args: list[str]) -> str:
    result = subprocess.run(
        ["gh", *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def gh_json(args: list[str]):
    return json.loads(run_gh(args))


def detect_source(login: str | None) -> str:
    login = (login or "").lower()
    if "qodo" in login:
        return "qodo"
    if "copilot" in login:
        return "copilot"
    if "sonar" in login:
        return "sonarcloud"
    return "github"


def current_repo() -> str:
    data = gh_json(["repo", "view", "--json", "nameWithOwner"])
    return data["nameWithOwner"]


def current_pr_number() -> int:
    data = gh_json(["pr", "view", "--json", "number"])
    return int(data["number"])


def graphql_threads(repo: str, pr_number: int):
    owner, name = repo.split("/", 1)
    query = """
query($owner: String!, $name: String!, $number: Int!) {
  repository(owner: $owner, name: $name) {
    pullRequest(number: $number) {
      reviewThreads(first: 100) {
        nodes {
          id
          isResolved
          isOutdated
          comments(first: 100) {
            nodes {
              databaseId
              url
              body
              path
              line
              author {
                login
              }
            }
          }
        }
      }
    }
  }
}
"""
    return gh_json(
        [
            "api",
            "graphql",
            "-f",
            f"query={query}",
            "-F",
            f"owner={owner}",
            "-F",
            f"name={name}",
            "-F",
            f"number={pr_number}",
        ]
    )


def build_report(repo: str, pr_number: int) -> dict:
    pr = gh_json(
        [
            "pr",
            "view",
            str(pr_number),
            "--repo",
            repo,
            "--json",
            "number,title,url,state,isDraft,headRefName,baseRefName,comments,reviews,statusCheckRollup",
        ]
    )
    inline_comments = gh_json(
        ["api", f"repos/{repo}/pulls/{pr_number}/comments?per_page=100"]
    )
    review_threads = graphql_threads(repo, pr_number)["data"]["repository"][
        "pullRequest"
    ]["reviewThreads"]["nodes"]

    top_level_comments = []
    for comment in pr.get("comments", []):
        login = comment.get("author", {}).get("login")
        top_level_comments.append(
            {
                "id": comment["id"],
                "url": comment["url"],
                "author": login,
                "source": detect_source(login),
                "body": comment["body"],
                "createdAt": comment["createdAt"],
            }
        )

    reviews = []
    for review in pr.get("reviews", []):
        login = review.get("author", {}).get("login")
        reviews.append(
            {
                "id": review["id"],
                "url": review.get("url") or "",
                "author": login,
                "source": detect_source(login),
                "state": review["state"],
                "body": review["body"],
                "submittedAt": review["submittedAt"],
            }
        )

    normalized_inline = []
    for comment in inline_comments:
        login = comment.get("user", {}).get("login")
        normalized_inline.append(
            {
                "id": comment["id"],
                "url": comment["html_url"],
                "author": login,
                "source": detect_source(login),
                "path": comment.get("path"),
                "line": comment.get("line"),
                "body": comment.get("body"),
                "reviewId": comment.get("pull_request_review_id"),
            }
        )

    normalized_threads = []
    for thread in review_threads:
        comments = []
        for comment in thread.get("comments", {}).get("nodes", []):
            login = comment.get("author", {}).get("login")
            comments.append(
                {
                    "commentId": comment["databaseId"],
                    "url": comment["url"],
                    "author": login,
                    "source": detect_source(login),
                    "path": comment.get("path"),
                    "line": comment.get("line"),
                    "body": comment.get("body"),
                }
            )
        normalized_threads.append(
            {
                "id": thread["id"],
                "isResolved": thread["isResolved"],
                "isOutdated": thread["isOutdated"],
                "comments": comments,
            }
        )

    checks = []
    for check in pr.get("statusCheckRollup", []):
        checks.append(
            {
                "type": check.get("__typename"),
                "name": check.get("name"),
                "status": check.get("status"),
                "conclusion": check.get("conclusion"),
                "detailsUrl": check.get("detailsUrl"),
                "workflowName": check.get("workflowName"),
            }
        )

    return {
        "repo": repo,
        "pr": {
            "number": pr["number"],
            "title": pr["title"],
            "url": pr["url"],
            "state": pr["state"],
            "isDraft": pr["isDraft"],
            "headRefName": pr["headRefName"],
            "baseRefName": pr["baseRefName"],
        },
        "checks": checks,
        "topLevelComments": top_level_comments,
        "reviews": reviews,
        "inlineComments": normalized_inline,
        "reviewThreads": normalized_threads,
    }


def append_check_lines(lines: list[str], checks: list[dict]) -> None:
    if not checks:
        lines.append(NONE_FOUND)
        return

    for check in checks:
        lines.append(
            f"- `{check['name']}`: `{check['status']}` / `{check['conclusion']}`"
            + (f" ({check['detailsUrl']})" if check.get("detailsUrl") else "")
        )


def append_comment_lines(lines: list[str], comments: list[dict]) -> None:
    if not comments:
        lines.append(NONE_FOUND)
        return

    for comment in comments:
        lines.append(f"- `{comment['source']}` by `{comment['author']}`: {comment['url']}")


def append_inline_comment_lines(lines: list[str], comments: list[dict]) -> None:
    if not comments:
        lines.append(NONE_FOUND)
        return

    for comment in comments:
        lines.append(
            f"- `{comment['source']}` `{comment['path']}:{comment['line']}`"
            f" comment_id={comment['id']} {comment['url']}"
        )


def append_review_thread_lines(lines: list[str], threads: list[dict]) -> None:
    if not threads:
        lines.append(NONE_FOUND)
        return

    for thread in threads:
        state = "resolved" if thread["isResolved"] else "open"
        first = thread["comments"][0] if thread["comments"] else {}
        path = first.get("path", "?")
        line = first.get("line", "?")
        comment_id = first.get("commentId", "?")
        source = first.get("source", "github")
        lines.append(
            f"- `{source}` `{path}:{line}` thread_id={thread['id']} "
            f"comment_id={comment_id} state={state}"
        )


def markdown_report(report: dict) -> str:
    lines: list[str] = []
    pr = report["pr"]
    lines.append(f"# PR Feedback: #{pr['number']} {pr['title']}")
    lines.append("")
    lines.append(f"- Repo: `{report['repo']}`")
    lines.append(f"- PR: {pr['url']}")
    lines.append(f"- Branch: `{pr['headRefName']}` -> `{pr['baseRefName']}`")
    lines.append(f"- State: `{pr['state']}` draft=`{pr['isDraft']}`")
    lines.append("")
    lines.append("## Status checks")
    append_check_lines(lines, report["checks"])
    lines.append("")
    lines.append("## Top-level comments")
    append_comment_lines(lines, report["topLevelComments"])
    lines.append("")
    lines.append("## Inline comments")
    append_inline_comment_lines(lines, report["inlineComments"])
    lines.append("")
    lines.append("## Review threads")
    append_review_thread_lines(lines, report["reviewThreads"])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo")
    parser.add_argument("--pr", type=int)
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    args = parser.parse_args()

    repo = args.repo or current_repo()
    pr_number = args.pr or current_pr_number()
    report = build_report(repo, pr_number)

    if args.format == "markdown":
        print(markdown_report(report))
    else:
        json.dump(report, sys.stdout, indent=2)
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
