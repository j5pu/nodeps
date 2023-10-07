from pathlib import Path

import pytest

from nodeps.__main__ import app
from nodeps import NODEPS_PROJECT_NAME


@pytest.mark.parametrize("invoke", [[app, "build"]], indirect=True)
def test_build(invoke):
    assert invoke.exit_code == 0


@pytest.mark.parametrize("invoke", [[app, "build", str(Path(__file__))]], indirect=True)
def test_build_path(invoke):
    assert invoke.exit_code == 0


@pytest.mark.parametrize("invoke", [[app, "build", NODEPS_PROJECT_NAME]], indirect=True)
def test_build_name(invoke):
    assert invoke.exit_code == 0


@pytest.mark.parametrize("invoke", [[app, "buildrequires"]], indirect=True)
def test_buildrequires(invoke):
    assert invoke.exit_code == 0


@pytest.mark.parametrize("invoke", [[app, "commit"]], indirect=True)
def test_commit(invoke):
    assert invoke.exit_code == 0


@pytest.mark.parametrize("invoke", [[app, "dependencies"]], indirect=True)
def test_dependencies(invoke):
    assert invoke.exit_code == 0


@pytest.mark.parametrize("invoke", [[app, "distribution"]], indirect=True)
def test_dependencies(invoke):
    assert invoke.exit_code == 0


@pytest.mark.parametrize("invoke", [[app, "extras"]], indirect=True)
def test_extras(invoke):
    assert invoke.exit_code == 0


@pytest.mark.parametrize("invoke", [[app, "latest"]], indirect=True)
def test_latest(invoke):
    assert invoke.exit_code == 0


@pytest.mark.parametrize("invoke", [[app, "next"]], indirect=True)
def test_next(invoke):
    assert invoke.exit_code == 0


@pytest.mark.parametrize("invoke", [[app, "repos"]], indirect=True)
def test_repos(invoke):
    assert invoke.exit_code == 0


@pytest.mark.parametrize("invoke", [[app, "sha"]], indirect=True)
def test_sha(invoke):
    assert invoke.exit_code == 0


@pytest.mark.parametrize("invoke", [[app, "superproject"]], indirect=True)
def test_superproject(invoke):
    assert invoke.exit_code == 0


@pytest.mark.parametrize("invoke", [[app, "top"]], indirect=True)
def test_top(invoke):
    assert invoke.exit_code == 0


@pytest.mark.parametrize("invoke", [[app, "version"]], indirect=True)
def test_version(invoke):
    assert invoke.exit_code == 0


@pytest.mark.parametrize("invoke", [[app, "venv"]], indirect=True)
def test_venv(invoke):
    assert invoke.exit_code == 0