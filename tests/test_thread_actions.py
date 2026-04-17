from __future__ import annotations

import argparse
import importlib.util
import json
import pathlib
import subprocess

import pytest


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent


def load_module(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


thread_actions = load_module(
    "thread_actions", REPO_ROOT / "skills" / "pr-review" / "scripts" / "thread_actions.py"
)


def test_run_gh_forwards_stdin_to_subprocess(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, object] = {}

    def fake_run(*args, **kwargs):
        captured["args"] = args[0]
        captured["kwargs"] = kwargs
        return subprocess.CompletedProcess(args[0], 0, stdout="ok", stderr="")

    monkeypatch.setattr(thread_actions.subprocess, "run", fake_run)

    output = thread_actions.run_gh(["api", "graphql"], input_text='{"query":"x"}')

    assert output == "ok"
    assert captured["args"] == ["gh", "api", "graphql"]
    assert captured["kwargs"]["input"] == '{"query":"x"}'
    assert captured["kwargs"]["text"] is True


def test_reply_inline_posts_json_payload(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, object] = {}

    def fake_run_gh(args: list[str], *, input_text: str | None = None) -> str:
        captured["args"] = args
        captured["input_text"] = input_text
        return ""

    monkeypatch.setattr(thread_actions, "run_gh", fake_run_gh)

    body = "Handled in commit\n\n- bullet"
    thread_actions.reply_inline("OriNachum/codex-guide", 7, 42, body)

    assert captured["args"] == [
        "api",
        "-X",
        "POST",
        "repos/OriNachum/codex-guide/pulls/7/comments/42/replies",
        "--input",
        "-",
    ]
    assert json.loads(captured["input_text"]) == {"body": body}


def test_batch_reply_and_resolve_uses_payload_file(
    monkeypatch: pytest.MonkeyPatch, tmp_path: pathlib.Path
) -> None:
    payload_path = tmp_path / "payload.json"
    payload_path.write_text(
        json.dumps(
            [
                {"comment_id": 1, "body": "first"},
                {"comment_id": 2, "body": "second"},
            ]
        ),
        encoding="utf-8",
    )
    calls: list[tuple[str, object]] = []

    monkeypatch.setattr(
        thread_actions,
        "thread_id_for_comment",
        lambda repo, pr, comment_id: f"thread-{comment_id}",
    )
    monkeypatch.setattr(
        thread_actions,
        "reply_inline",
        lambda repo, pr, comment_id, body: calls.append(("reply", comment_id, body)),
    )
    monkeypatch.setattr(
        thread_actions,
        "resolve_thread",
        lambda thread_id: calls.append(("resolve", thread_id)),
    )

    assert (
        thread_actions.batch_reply_and_resolve(
            "OriNachum/codex-guide", 7, str(payload_path)
        )
        == 0
    )
    assert calls == [
        ("reply", 1, "first"),
        ("resolve", "thread-1"),
        ("reply", 2, "second"),
        ("resolve", "thread-2"),
    ]


def test_handle_command_resolve_thread(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[str, object]] = []
    monkeypatch.setattr(thread_actions, "thread_id_for_comment", lambda *args: "thread-9")
    monkeypatch.setattr(
        thread_actions, "resolve_thread", lambda thread_id: calls.append(("resolve", thread_id))
    )

    args = argparse.Namespace(
        command="resolve-thread",
        repo="OriNachum/codex-guide",
        pr=7,
        comment_id=9,
    )

    assert thread_actions.handle_command(args) == 0
    assert calls == [("resolve", "thread-9")]
