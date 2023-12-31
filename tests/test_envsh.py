import os

import pytest
from _pytest.fixtures import FixtureRequest

from nodeps import envsh, Path

keys = [f'TEST_{_i}' for _i in ['MACOS', 'LOGNAME', 'LOGNAMEHOME', 'ROOTHOME', 'LOGGEDINUSER',
                                'LOGNAMEREALNAME', 'MULTILINE']]

EnvironOS = type(os.environ)


@pytest.fixture(scope="session")
def tests_envsh(request: FixtureRequest) -> Path:
    return Path(__file__).parent / "env.sh"


def check(env, environ=True):
    for i in keys:
        assert env.get(i) is not None
        del env[i]
        if environ:
            assert i in os.environ
            del os.environ[i]
    for item in ["COLUMNS", "LINES", "PYTHONSTARTUP"]:
        if item in env:
            del env[item]
    assert env == {}


def test_envsh_env_not_override():
    rv = envsh(override=False, missing_ok=True)
    if rv:
        assert "LOGURU_LEVEL" in rv
        assert "LOG_LEVEL" in rv
        assert "LOGURU_LEVEL" not in os.environ
        assert "LOG_LEVEL" not in os.environ


def test_envsh_env_override():
    rv = envsh(missing_ok=True)
    if rv:
        assert "LOGURU_LEVEL" in rv
        assert "LOG_LEVEL" in rv
        assert "LOGURU_LEVEL" in os.environ
        del os.environ["LOGURU_LEVEL"]
        assert "LOG_LEVEL" in os.environ
        del os.environ["LOG_LEVEL"]


def test_envsh_envsh_override(tests_envsh: Path):
    rv = envsh(tests_envsh)
    check(rv)


def test_envsh_envsh_not_override(tests_envsh: Path):
    rv = envsh(tests_envsh)
    check(rv, False)
