#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys


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


def current_repo() -> str:
    data = gh_json(["repo", "view", "--json", "nameWithOwner"])
    return data["nameWithOwner"]


def thread_id_for_comment(repo: str, pr_number: int, comment_id: int) -> str:
    owner, name = repo.split("/", 1)
    query = """
query($owner: String!, $name: String!, $number: Int!) {
  repository(owner: $owner, name: $name) {
    pullRequest(number: $number) {
      reviewThreads(first: 100) {
        nodes {
          id
          comments(first: 100) {
            nodes {
              databaseId
            }
          }
        }
      }
    }
  }
}
"""
    data = gh_json(
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
    threads = data["data"]["repository"]["pullRequest"]["reviewThreads"]["nodes"]
    for thread in threads:
        for comment in thread.get("comments", {}).get("nodes", []):
            if int(comment["databaseId"]) == comment_id:
                return thread["id"]
    raise SystemExit(f"could not find thread for comment_id={comment_id}")


def reply_inline(repo: str, pr_number: int, comment_id: int, body: str) -> None:
    subprocess.run(
        [
            "gh",
            "api",
            "-X",
            "POST",
            f"repos/{repo}/pulls/{pr_number}/comments/{comment_id}/replies",
            "-f",
            f"body={body}",
        ],
        check=True,
    )


def resolve_thread(thread_id: str) -> None:
    mutation = """
mutation($threadId: ID!) {
  resolveReviewThread(input: {threadId: $threadId}) {
    thread {
      id
      isResolved
    }
  }
}
"""
    subprocess.run(
        [
            "gh",
            "api",
            "graphql",
            "-f",
            f"query={mutation}",
            "-F",
            f"threadId={thread_id}",
        ],
        check=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    shared = argparse.ArgumentParser(add_help=False)
    shared.add_argument("--repo")
    shared.add_argument("--pr", type=int, required=True)
    shared.add_argument("--comment-id", type=int, required=True)

    reply = subparsers.add_parser("reply-inline", parents=[shared])
    reply.add_argument("--body", required=True)

    resolve = subparsers.add_parser("resolve-thread", parents=[shared])

    both = subparsers.add_parser("reply-and-resolve", parents=[shared])
    both.add_argument("--body", required=True)

    batch = subparsers.add_parser("reply-and-resolve-batch")
    batch.add_argument("--repo")
    batch.add_argument("--pr", type=int, required=True)
    batch.add_argument("--file", required=True)

    args = parser.parse_args()
    repo = args.repo or current_repo()

    if args.command == "reply-inline":
        reply_inline(repo, args.pr, args.comment_id, args.body)
        return 0

    if args.command == "reply-and-resolve-batch":
        payload = json.loads(pathlib.Path(args.file).read_text(encoding="utf-8"))
        for item in payload:
            comment_id = int(item["comment_id"])
            body = item["body"]
            thread_id = thread_id_for_comment(repo, args.pr, comment_id)
            reply_inline(repo, args.pr, comment_id, body)
            resolve_thread(thread_id)
        return 0

    thread_id = thread_id_for_comment(repo, args.pr, args.comment_id)
    if args.command == "resolve-thread":
        resolve_thread(thread_id)
        return 0

    reply_inline(repo, args.pr, args.comment_id, args.body)
    resolve_thread(thread_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
