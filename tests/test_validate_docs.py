from __future__ import annotations

import importlib.util
import pathlib

import pytest


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent


def load_module(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


validate_docs = load_module("validate_docs", REPO_ROOT / "scripts" / "validate-docs.py")


def write_skill(tmp_path: pathlib.Path, name: str = "demo-skill") -> pathlib.Path:
    skill_dir = tmp_path / "skills" / name
    (skill_dir / "agents").mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(
        "---\nname: demo-skill\ndescription: Demo skill.\n---\n\n# Demo\n",
        encoding="utf-8",
    )
    (skill_dir / "agents" / "openai.yaml").write_text("model: gpt-5\n", encoding="utf-8")
    return skill_dir


def configure_module(monkeypatch: pytest.MonkeyPatch, root: pathlib.Path) -> None:
    monkeypatch.setattr(validate_docs, "ROOT", root)
    monkeypatch.setattr(validate_docs, "SKILLS_DIR", root / "skills")


def test_main_passes_for_valid_repo(monkeypatch: pytest.MonkeyPatch, tmp_path: pathlib.Path) -> None:
    write_skill(tmp_path)
    (tmp_path / "README.md").write_text("[Skill](skills/demo-skill/SKILL.md)\n", encoding="utf-8")
    configure_module(monkeypatch, tmp_path)

    assert validate_docs.main() == 0


def test_validate_skill_fails_when_openai_yaml_missing(
    monkeypatch: pytest.MonkeyPatch, tmp_path: pathlib.Path, capsys: pytest.CaptureFixture[str]
) -> None:
    skill_dir = write_skill(tmp_path)
    (skill_dir / "agents" / "openai.yaml").unlink()
    configure_module(monkeypatch, tmp_path)

    with pytest.raises(SystemExit):
        validate_docs.validate_skill(skill_dir)
    assert "missing skills/demo-skill/agents/openai.yaml" in capsys.readouterr().out


def test_validate_markdown_links_rejects_absolute_paths(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: pathlib.Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    write_skill(tmp_path)
    markdown_file = tmp_path / "README.md"
    markdown_file.write_text("[Bad](/tmp/example)\n", encoding="utf-8")
    configure_module(monkeypatch, tmp_path)

    with pytest.raises(SystemExit):
        validate_docs.validate_markdown_links(markdown_file)
    assert "uses absolute filesystem link" in capsys.readouterr().out


def test_validate_markdown_links_rejects_missing_paths(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: pathlib.Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    write_skill(tmp_path)
    markdown_file = tmp_path / "README.md"
    markdown_file.write_text("[Missing](docs/nope.md)\n", encoding="utf-8")
    configure_module(monkeypatch, tmp_path)

    with pytest.raises(SystemExit):
        validate_docs.validate_markdown_links(markdown_file)
    assert "links to missing path" in capsys.readouterr().out
