from __future__ import annotations

import importlib.util
import pathlib


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent


def load_module(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


fetch_feedback = load_module(
    "fetch_feedback", REPO_ROOT / "skills" / "pr-review" / "scripts" / "fetch_feedback.py"
)


def test_detect_source_maps_known_review_bots() -> None:
    assert fetch_feedback.detect_source("qodo-code-review") == "qodo"
    assert fetch_feedback.detect_source("copilot-pull-request-reviewer") == "copilot"
    assert fetch_feedback.detect_source("sonarqubecloud") == "sonarcloud"
    assert fetch_feedback.detect_source("someone-else") == "github"
    assert fetch_feedback.detect_source(None) == "github"


def test_markdown_report_uses_none_fallbacks() -> None:
    report = {
        "repo": "OriNachum/codex-guide",
        "pr": {
            "number": 7,
            "title": "Example",
            "url": "https://example.test/pr/7",
            "state": "OPEN",
            "isDraft": False,
            "headRefName": "feature",
            "baseRefName": "main",
        },
        "checks": [],
        "topLevelComments": [],
        "reviews": [],
        "inlineComments": [],
        "reviewThreads": [],
    }

    output = fetch_feedback.markdown_report(report)

    assert "## Status checks" in output
    assert "## Top-level comments" in output
    assert "## Inline comments" in output
    assert "## Review threads" in output
    assert output.count(fetch_feedback.NONE_FOUND) == 4


def test_markdown_report_renders_populated_sections() -> None:
    report = {
        "repo": "OriNachum/codex-guide",
        "pr": {
            "number": 7,
            "title": "Example",
            "url": "https://example.test/pr/7",
            "state": "OPEN",
            "isDraft": False,
            "headRefName": "feature",
            "baseRefName": "main",
        },
        "checks": [
            {
                "name": "SonarCloud Code Analysis",
                "status": "COMPLETED",
                "conclusion": "FAILURE",
                "detailsUrl": "https://sonarcloud.io",
            }
        ],
        "topLevelComments": [
            {
                "source": "sonarcloud",
                "author": "sonarqubecloud",
                "url": "https://example.test/comment",
            }
        ],
        "reviews": [],
        "inlineComments": [
            {
                "source": "copilot",
                "path": "skills/pr-review/scripts/thread_actions.py",
                "line": 74,
                "id": 123,
                "url": "https://example.test/inline",
            }
        ],
        "reviewThreads": [
            {
                "id": "thread-1",
                "isResolved": False,
                "comments": [
                    {
                        "source": "copilot",
                        "path": "skills/pr-review/scripts/thread_actions.py",
                        "line": 74,
                        "commentId": 123,
                    }
                ],
            }
        ],
    }

    output = fetch_feedback.markdown_report(report)

    assert "SonarCloud Code Analysis" in output
    assert "https://sonarcloud.io" in output
    assert "`sonarcloud` by `sonarqubecloud`" in output
    assert "comment_id=123" in output
    assert "thread_id=thread-1" in output
    assert "state=open" in output
