"""NoDeps Helpers and Utils Module."""
from __future__ import annotations

__all__ = (
    "CONSOLE",

    "Bump",
    "CalledProcessError",
    "Chain",
    "CmdError",
    "ColorLogger",
    "CommandNotFoundError",
    "dd",
    "dictsort",
    "Env",
    "EnvBuilder",
    "FileConfig",
    "FrameSimple",
    "getter",
    "Gh",
    "GitStatus",
    "GitUrl",
    "GroupUser",
    "InvalidArgumentError",
    "LetterCounter",
    "MyPrompt",
    "NamedtupleMeta",
    "Noset",
    "Passwd",
    "PathStat",
    "Path",
    "PipMetaPathFinder",
    "ProjectRepos",
    "Project",
    "PTHBuildPy",
    "PTHDevelop",
    "PTHEasyInstall",
    "PTHInstallLib",
    "TempDir",
    "aioclone",
    "aioclosed",
    "aiocmd",
    "aiocommand",
    "aiodmg",
    "aiogz",
    "aioloop",
    "aioloopid",
    "aiorunning",
    "allin",
    "ami",
    "anyin",
    "chdir",
    "clone",
    "cmd",
    "cmdrun",
    "cmdsudo",
    "command",
    "completions",
    "current_task_name",
    "dict_sort",
    "dmg",
    "effect",
    "elementadd",
    "exec_module_from_file",
    "filterm",
    "findfile",
    "findup",
    "firstfound",
    "flatten",
    "framesimple",
    "from_latin9",
    "fromiter",
    "getpths",
    "getsitedir",
    "group_user",
    "gz",
    "in_tox",
    "indict",
    "ins",
    "is_idlelib",
    "is_repl",
    "is_terminal",
    "iscoro",
    "map_with_args",
    "mip",
    "noexc",
    "parent",
    "parse_str",
    "pipmetapathfinder",
    "returncode",
    "siteimported",
    "sourcepath",
    "split_pairs",
    "stdout",
    "stdquiet",
    "suppress",
    "syssudo",
    "tardir",
    "tilde",
    "timestamp_now",
    "to_camel",
    "toiter",
    "tomodules",
    "urljson",
    "varname",
    "which",
    "yield_if",
    "yield_last",
    "getstdout",
    "strip",
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "bblack",
    "bred",
    "bgreen",
    "byellow",
    "bblue",
    "bmagenta",
    "bcyan",
    "bwhite",
    "reset",
    "COLORIZE",
    "EnumLower",
    "Color",
    "SYMBOL",
    "Symbol",
    "LOGGER_DEFAULT_FMT",
    "logger",
    "cache",
    "ic",
    "icc",
    "Repo",
    "PYTHON_FTP",
    "python_latest",
    "python_version",
    "python_versions",
    "request_x_api_key_json",
    "EXECUTABLE",
    "EXECUTABLE_SITE",
    "NOSET",
)

import abc
import ast
import asyncio
import collections
import contextlib
import copy
import dataclasses
import datetime
import enum
import filecmp
import fnmatch
import getpass
import grp
import hashlib
import importlib.abc
import importlib.metadata
import importlib.util
import inspect
import io
import ipaddress
import itertools
import json
import logging
import os
import pathlib
import pickle
import platform
import pwd
import re
import shutil
import signal
import stat
import string
import subprocess
import sys
import sysconfig
import tarfile
import tempfile
import textwrap
import threading
import time
import tokenize
import types
import urllib.error
import urllib.request
import venv
import warnings
import zipfile
from collections.abc import Callable, Generator, Hashable, Iterable, Iterator, Mapping, MutableMapping, Sequence
from io import BufferedRandom, BufferedReader, BufferedWriter, FileIO, TextIOWrapper
from ipaddress import IPv4Address, IPv6Address
from typing import (
    IO,
    TYPE_CHECKING,
    Any,
    AnyStr,
    BinaryIO,
    ClassVar,
    Generic,
    Literal,
    ParamSpec,
    TextIO,
    TypeAlias,
    TypeVar,
    Union,
    cast,
)

# <editor-fold desc="nodeps[pretty] extras">
try:
    # nodeps[pretty] extras
    import rich.console  # type: ignore[attr-defined]
    import rich.pretty  # type: ignore[attr-defined]
    import rich.traceback  # type: ignore[attr-defined]
    from rich.console import Console  # type: ignore[name-defined]
    CONSOLE = rich.console.Console(color_system="standard")
    rich.pretty.install(CONSOLE, expand_all=True)  # type: ignore[attr-defined]
    rich.traceback.install(show_locals=True,  # type: ignore[attr-defined]
                           suppress={"click", "_pytest", "pluggy", "rich", })
except ModuleNotFoundError:
    Console = object
    CONSOLE = None
# </editor-fold>

# <editor-fold desc="nodeps[pth] extras">
try:
    # nodeps[pth] extras
    import setuptools  # type: ignore[attr-defined]
    from setuptools.command.build_py import build_py  # type: ignore[attr-defined]
    from setuptools.command.develop import develop  # type: ignore[attr-defined]
    from setuptools.command.easy_install import easy_install  # type: ignore[attr-defined]
    from setuptools.command.install_lib import install_lib  # type: ignore[attr-defined]
except ModuleNotFoundError:
    setuptools = object
    build_py = object
    develop = object
    easy_install = object
    install_lib = object
# </editor-fold>


try:
    if "_in_process.py" not in sys.argv[0]:
        # Avoids failing when asking for build requirements and distutils.core is not available since pip patch it
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=UserWarning, message="Setuptools is replacing distutils.")

            # Must be imported after setuptools
            # noinspection PyCompatibility
            import pip._internal.cli.base_command
            import pip._internal.metadata
            import pip._internal.models.direct_url
            import pip._internal.models.scheme
            import pip._internal.operations.install.wheel
            import pip._internal.req.req_install
            import pip._internal.req.req_uninstall
except ModuleNotFoundError:
    pip = object

try:
    from IPython.terminal.prompts import Prompts, Token  # type: ignore[attr-defined]
except ModuleNotFoundError:
    Prompts = Token = object

from nodeps.platforms import (
    PLATFORMS,
    AssemblaPlatform,
    BasePlatform,
    BitbucketPlatform,
    FriendCodePlatform,
    GitHubPlatform,
    GitLabPlatform,
)

if TYPE_CHECKING:
    EnvironOS: TypeAlias = type(os.environ)
    from urllib.parse import ParseResult

    from decouple import CONFIG  # type: ignore[attr-defined]
    from IPython.core.interactiveshell import InteractiveShell

    # noinspection PyCompatibility
    from pip._internal.cli.base_command import Command
    from traitlets.config import Config

LOGGER = logging.getLogger(__name__)

_NODEPS_PIP_POST_INSTALL = {}
"""Holds the context with wheels installed and paths to package installed to be used in post install"""


_KT = TypeVar("_KT")
_T = TypeVar("_T")
_VT = TypeVar("_VT")
P = ParamSpec("P")
T = TypeVar("T")

# noinspection LongLine,SpellCheckingInspection
@dataclasses.dataclass
class Env:
    """Environ Class.

    See Also: `Environment variables
    <https://docs.github.com/en/enterprise-cloud@latest/actions/learn-github-actions/environment-variables>`_

    If you need to use a workflow run's URL from within a job, you can combine these environment variables:
        ``$GITHUB_SERVER_URL/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID``

    If you generate a value in one step of a job, you can use the value in subsequent ``steps`` of
        the same job by assigning the value to an existing or new environment variable and then writing
        this to the ``GITHUB_ENV`` environment file, see `Commands
        <https://docs.github.com/en/enterprise-cloud@latest/actions/reference/workflow-commands-for-github-actions
        /#setting-an-environment-variable>`_.

    If you want to pass a value from a step in one job in a ``workflow`` to a step in another job in the workflow,
        you can define the value as a job output, see `Syntax
        <https://docs.github.com/en/enterprise-cloud@latest/actions/learn-github-actions/workflow-syntax-for-github
        -actions#jobsjob_idoutputs>`_.
    """

    config: CONFIG = dataclasses.field(default=None, init=False)
    """Searches for `settings.ini` and `.env` cwd up. Usage: var = Env()._config("VAR", default=True, cast=bool)."""

    CI: bool | str | None = dataclasses.field(default=None, init=False)
    """Always set to ``true`` in a GitHub Actions environment."""

    GITHUB_ACTION: str | None = dataclasses.field(default=None, init=False)
    # noinspection LongLine
    """
    The name of the action currently running, or the `id
    <https://docs.github.com/en/enterprise-cloud@latest/actions/using-workflows/workflow-syntax-for-github-actions#jobs\
        job_idstepsid>`_ of a step.

    For example, for an action, ``__repo-owner_name-of-action-repo``.

    GitHub removes special characters, and uses the name ``__run`` when the current step runs a script without an id.

    If you use the same script or action more than once in the same job,
    the name will include a suffix that consists of the sequence number preceded by an underscore.

    For example, the first script you run will have the name ``__run``, and the second script will be named ``__run_2``.

    Similarly, the second invocation of ``actions/checkout`` will be ``actionscheckout2``.
    """

    GITHUB_ACTION_PATH: Path | str | None = dataclasses.field(default=None, init=False)
    """
    The path where an action is located. This property is only supported in composite actions.

    You can use this path to access files located in the same repository as the action.

    For example, ``/home/runner/work/_actions/repo-owner/name-of-action-repo/v1``.
    """

    GITHUB_ACTION_REPOSITORY: str | None = dataclasses.field(default=None, init=False)
    """
    For a step executing an action, this is the owner and repository name of the action.

    For example, ``actions/checkout``.
    """

    GITHUB_ACTIONS: bool | str | None = dataclasses.field(default=None, init=False)
    """
    Always set to ``true`` when GitHub Actions is running the workflow.

    You can use this variable to differentiate when tests are being run locally or by GitHub Actions.
    """

    GITHUB_ACTOR: str | None = dataclasses.field(default=None, init=False)
    """
    The name of the person or app that initiated the workflow.

    For example, ``octocat``.
    """

    GITHUB_API_URL: ParseResult | str | None = dataclasses.field(default=None, init=False)
    """
    API URL.

    For example: ``https://api.github.com``.
    """

    GITHUB_BASE_REF: str | None = dataclasses.field(default=None, init=False)
    """
    The name of the base ref or target branch of the pull request in a workflow run.

    This is only set when the event that triggers a workflow run is either ``pull_request`` or ``pull_request_target``.

    For example, ``main``.
    """

    GITHUB_ENV: Path | str | None = dataclasses.field(default=None, init=False)
    """
    The path on the runner to the file that sets environment variables from workflow commands.

    This file is unique to the current step and changes for each step in a job.

    For example, ``/home/runner/work/_temp/_runner_file_commands/set_env_87406d6e-4979-4d42-98e1-3dab1f48b13a``.

    For more information, see `Workflow commands for GitHub Actions.
    <https://docs.github.com/en/enterprise-cloud@latest/actions/using-workflows/workflow-commands-for-github-actions
    #setting-an-environment-variable>`_
    """

    GITHUB_EVENT_NAME: str | None = dataclasses.field(default=None, init=False)
    """
    The name of the event that triggered the workflow.

    For example, ``workflow_dispatch``.
    """

    GITHUB_EVENT_PATH: Path | str | None = dataclasses.field(default=None, init=False)
    """
    The path to the file on the runner that contains the full event webhook payload.

    For example, ``/github/workflow/event.json``.
    """

    GITHUB_GRAPHQL_URL: ParseResult | str | None = dataclasses.field(default=None, init=False)
    """
    Returns the GraphQL API URL.

    For example: ``https://api.github.com/graphql``.
    """

    GITHUB_HEAD_REF: str | None = dataclasses.field(default=None, init=False)
    """
    The head ref or source branch of the pull request in a workflow run.

    This property is only set when the event that triggers a workflow run is either
    ``pull_request`` or ``pull_request_target``.

    For example, ``feature-branch-1``.
    """

    GITHUB_JOB: str | None = dataclasses.field(default=None, init=False)
    """
    The `job_id
    <https://docs.github.com/en/enterprise-cloud@latest/actions/reference/workflow-syntax-for-github-actions
    #jobsjob_id>`_
    of the current job.

    For example, ``greeting_job``.
    """

    GITHUB_PATH: Path | str | None = dataclasses.field(default=None, init=False)
    """
    The path on the runner to the file that sets system PATH variables from workflow commands.
    This file is unique to the current step and changes for each step in a job.

    For example, ``/home/runner/work/_temp/_runner_file_commands/add_path_899b9445-ad4a-400c-aa89-249f18632cf5``.

    For more information, see `Workflow commands for GitHub Actions.
    <https://docs.github.com/en/enterprise-cloud@latest/actions/using-workflows/workflow-commands-for-github-actions
    #adding-a-system-path>`_
    """

    GITHUB_REF: str | None = dataclasses.field(default=None, init=False)
    """
    The branch or tag ref that triggered the workflow run.

    For branches this is the format ``refs/heads/<branch_name>``,
    for tags it is ``refs/tags/<tag_name>``,
    and for pull requests it is ``refs/pull/<pr_number>/merge``.

    This variable is only set if a branch or tag is available for the event type.

    For example, ``refs/heads/feature-branch-1``.
    """

    GITHUB_REF_NAME: str | None = dataclasses.field(default=None, init=False)
    """
    The branch or tag name that triggered the workflow run.

    For example, ``feature-branch-1``.
    """

    GITHUB_REF_PROTECTED: bool | str | None = dataclasses.field(default=None, init=False)
    """
    ``true`` if branch protections are configured for the ref that triggered the workflow run.
    """

    GITHUB_REF_TYPE: str | None = dataclasses.field(default=None, init=False)
    """
    The type of ref that triggered the workflow run.

    Valid values are ``branch`` or ``tag``.

    For example, ``branch``.
    """

    GITHUB_REPOSITORY: str | None = dataclasses.field(default=None, init=False)
    """
    The owner and repository name.

    For example, ``octocat/Hello-World``.
    """

    GITHUB_REPOSITORY_OWNER: str | None = dataclasses.field(default=None, init=False)
    """
    The repository owner's name.

    For example, ``octocat``.
    """

    GITHUB_RETENTION_DAYS: str | None = dataclasses.field(default=None, init=False)
    """
    The number of days that workflow run logs and artifacts are kept.

    For example, ``90``.
    """

    GITHUB_RUN_ATTEMPT: str | None = dataclasses.field(default=None, init=False)
    """
    A unique number for each attempt of a particular workflow run in a repository.

    This number begins at ``1`` for the workflow run's first attempt, and increments with each re-run.

    For example, ``3``.
    """

    GITHUB_RUN_ID: str | None = dataclasses.field(default=None, init=False)
    """
    A unique number for each workflow run within a repository.

    This number does not change if you re-run the workflow run.

    For example, ``1658821493``.
    """

    GITHUB_RUN_NUMBER: str | None = dataclasses.field(default=None, init=False)
    """
    A unique number for each run of a particular workflow in a repository.

    This number begins at ``1`` for the workflow's first run, and increments with each new run.
    This number does not change if you re-run the workflow run.

    For example, ``3``.
    """

    GITHUB_SERVER_URL: ParseResult | str | None = dataclasses.field(default=None, init=False)
    """
    The URL of the GitHub Enterprise Cloud server.

    For example: ``https://github.com``.
    """

    GITHUB_SHA: str | None = dataclasses.field(default=None, init=False)
    """
    The commit SHA that triggered the workflow.

    The value of this commit SHA depends on the event that triggered the workflow.
    For more information, see `Events that trigger workflows.
    <https://docs.github.com/en/enterprise-cloud@latest/actions/using-workflows/events-that-trigger-workflows>`_

    For example, ``ffac537e6cbbf934b08745a378932722df287a53``.
    """

    GITHUB_WORKFLOW: Path | str | None = dataclasses.field(default=None, init=False)
    """
    The name of the workflow.

    For example, ``My test workflow``.

    If the workflow file doesn't specify a name,
    the value of this variable is the full path of the workflow file in the repository.
    """

    GITHUB_WORKSPACE: Path | str | None = dataclasses.field(default=None, init=False)
    """
    The default working directory on the runner for steps, and the default location of your repository
    when using the `checkout <https://github.com/actions/checkout>`_ action.

    For example, ``/home/runner/work/my-repo-name/my-repo-name``.
    """

    RUNNER_ARCH: str | None = dataclasses.field(default=None, init=False)
    """
    The architecture of the runner executing the job.

    Possible values are ``X86``, ``X64``, ``ARM``, or ``ARM64``.

    For example, ``X86``.
    """

    RUNNER_NAME: str | None = dataclasses.field(default=None, init=False)
    """
    The name of the runner executing the job.

    For example, ``Hosted Agent``.
    """

    RUNNER_OS: str | None = dataclasses.field(default=None, init=False)
    """
    The operating system of the runner executing the job.

    Possible values are ``Linux``, ``Windows``, or ``macOS``.

    For example, ``Linux``.
    """

    RUNNER_TEMP: Path | str | None = dataclasses.field(default=None, init=False)
    """
    The path to a temporary directory on the runner.

    This directory is emptied at the beginning and end of each job.

    Note that files will not be removed if the runner's user account does not have permission to delete them.

    For example, ``_temp``.
    """

    RUNNER_TOOL_CACHE: str | None = dataclasses.field(default=None, init=False)
    # noinspection LongLine
    """
    The path to the directory containing preinstalled tools for GitHub-hosted runners.

    For more information, see `About GitHub-hosted runners.
    <https://docs.github.com/en/enterprise-cloud@latest/actions/reference/specifications-for-github-hosted-runners
    /#supported-software>`_

    `Ubuntu latest <https://github.com/actions/virtual-environments/blob/main/images/linux/Ubuntu2004-Readme.md>`_
    `macOS latest <https://github.com/actions/virtual-environments/blob/main/images/macos/macos-11-Readme.md>`_

    For example, ``C:/hostedtoolcache/windows``.
    """

    COMMAND_MODE: str | None = dataclasses.field(default=None, init=False)
    HOME: str | None = dataclasses.field(default=None, init=False)
    IPYTHONENABLE: str | None = dataclasses.field(default=None, init=False)
    LC_TYPE: str | None = dataclasses.field(default=None, init=False)
    LOGNAME: str | None = dataclasses.field(default=None, init=False)
    OLDPWD: str | None = dataclasses.field(default=None, init=False)
    PATH: str | None = dataclasses.field(default=None, init=False)
    PS1: str | None = dataclasses.field(default=None, init=False)
    PWD: str | None = dataclasses.field(default=None, init=False)
    PYCHARM_DISPLAY_PORT: str | None = dataclasses.field(default=None, init=False)
    PYCHARM_HOSTED: str | None = dataclasses.field(default=None, init=False)
    PYCHARM_MATPLOTLIB_INDEX: str | None = dataclasses.field(default=None, init=False)
    PYCHARM_MATPLOTLIB_INTERACTIVE: str | None = dataclasses.field(default=None, init=False)
    PYCHARM_PROPERTIES: str | None = dataclasses.field(default=None, init=False)
    PYCHARM_VM_OPTIONS: str | None = dataclasses.field(default=None, init=False)
    PYDEVD_LOAD_VALUES_ASYNC: str | None = dataclasses.field(default=None, init=False)
    PYTHONIOENCODING: str | None = dataclasses.field(default=None, init=False)
    PYTHONPATH: str | None = dataclasses.field(default=None, init=False)
    PYTHONUNBUFFERED: str | None = dataclasses.field(default=None, init=False)
    SHELL: str | None = dataclasses.field(default=None, init=False)
    SSH_AUTH_SOCK: str | None = dataclasses.field(default=None, init=False)
    SUDO_USER: str | None = dataclasses.field(default=None, init=False)
    TMPDIR: str | None = dataclasses.field(default=None, init=False)
    XPC_FLAGS: str | None = dataclasses.field(default=None, init=False)
    XPC_SERVICE_NAME: str | None = dataclasses.field(default=None, init=False)
    __CFBundleIdentifier: str | None = dataclasses.field(default=None, init=False)
    __CF_USER_TEXT_ENCODING: str | None = dataclasses.field(default=None, init=False)

    LOGURU_LEVEL: str | None = dataclasses.field(default="DEBUG", init=False)
    LOG_LEVEL: int | str | None = dataclasses.field(default="DEBUG", init=False)

    _parse_as_int: ClassVar[tuple[str, ...]] = (
        "GITHUB_RUN_ATTEMPT",
        "GITHUB_RUN_ID",
        "GITHUB_RUN_NUMBER",
    )
    _parse_as_int_suffix: ClassVar[tuple[str, ...]] = (
        "_GID",
        "_JOBS",
        "_PORT",
        "_UID",
    )
    parsed: dataclasses.InitVar[bool] = True

    def __post_init__(self, parsed: bool) -> None:
        """Instance of Env class.

        Examples:
            >>> import logging
            >>> from nodeps import Env
            >>> from nodeps import Path
            >>>
            >>> env = Env()
            >>> assert env.config("DECOUPLE_CONFIG_TEST") == 'True'
            >>> assert env.config("DECOUPLE_CONFIG_TEST",  cast=bool) == True
            >>> assert env.LOG_LEVEL == logging.DEBUG
            >>> assert isinstance(env.PWD, Path)
            >>> assert "PWD" in env

        Args:
            parsed: Parse the environment variables using :func:`nodeps.parse_str`,
                except :func:`Env.as_int` (default: True)
        """
        envbash()
        self.__dict__.update({k: self.as_int(k, v) for k, v in os.environ.items()} if parsed else os.environ)
        self.LOG_LEVEL = getattr(logging, self.LOG_LEVEL.upper() if isinstance(self.LOG_LEVEL, str) else self.LOG_LEVEL)

        if path := (Path.cwd() / "settings.ini").find_up():
            with pipmetapathfinder():
                import decouple  # type: ignore[attr-defined]

                self.config = decouple.Config(decouple.RepositoryIni(path.absolute()))

    def __contains__(self, item):
        """Check if item is in self.__dict__."""
        return item in self.__dict__

    def __getattr__(self, name: str) -> bool | Path | ParseResult | IPv4Address | IPv6Address | int | str | None:
        """Get attribute from self.__dict__ if exists, otherwise return None."""
        if name in self:
            return self.__dict__[name]
        return None

    def __getattribute__(self, name: str) -> bool | Path | ParseResult | IPv4Address | IPv6Address | int | str | None:
        """Get attribute from self.__dict__ if exists, otherwise return None."""
        try:
            return super().__getattribute__(name)
        except AttributeError:
            return None

    def __getitem__(self, item: str) -> bool | Path | ParseResult | IPv4Address | IPv6Address | int | str | None:
        """Get item from self.__dict__ if exists, otherwise return None."""
        return self.__getattr__(item)

    @classmethod
    def as_int(cls, key: str, value: str = "") -> bool | Path | ParseResult | IPv4Address | IPv6Address | int | str:
        """Parse as int if environment variable should be forced to be parsed as int checking if:.

            - has value,
            - key in :data:`Env._parse_as_int` or
            - key ends with one of the items in :data:`Env._parse_as_int_suffix`.

        Args:
            key: Environment variable name.
            value: Environment variable value (default: "").

        Returns:
            int, if key should be parsed as int and has value, otherwise according to :func:`parse_str`.
        """
        convert = False
        if value:
            if key in cls._parse_as_int:
                convert = True
            else:
                for item in cls._parse_as_int_suffix:
                    if key.endswith(item):
                        convert = True
        return int(value) if convert and value.isnumeric() else parse_str(value)

    @staticmethod
    def parse_as_bool(
        variable: str = "USER",
    ) -> bool | Path | ParseResult | IPv4Address | IPv6Address | int | str | None:
        """Parses variable from environment 1 and 0 as bool instead of int.

        Parses:
            - bool: 1, 0, True, False, yes, no, on, off (case insensitive)
            - int: integer only numeric characters but 1 and 0 or SUDO_UID or SUDO_GID
            - ipaddress: ipv4/ipv6 address
            - url: if "//" or "@" is found it will be parsed as url
            - path: start with / or ~ or .
            - others as string

        Arguments:
            variable: variable name to parse from environment (default: USER)

        Examples:
            >>> from nodeps import Path
            >>> from nodeps import Env
            >>>
            >>> assert isinstance(Env.parse_as_bool(), str)
            >>>
            >>> os.environ['FOO'] = '1'
            >>> assert Env.parse_as_bool("FOO") is True
            >>>
            >>> os.environ['FOO'] = '0'
            >>> assert Env.parse_as_bool("FOO") is False
            >>>
            >>> os.environ['FOO'] = 'TrUe'
            >>> assert Env.parse_as_bool("FOO") is True
            >>>
            >>> os.environ['FOO'] = 'OFF'
            >>> assert Env.parse_as_bool("FOO") is False
            >>>
            >>> os.environ['FOO'] = '~/foo'
            >>> assert Env.parse_as_bool("FOO") == Path('~/foo')
            >>>
            >>> os.environ['FOO'] = '/foo'
            >>> assert Env.parse_as_bool("FOO") == Path('/foo')
            >>>
            >>> os.environ['FOO'] = './foo'
            >>> assert Env.parse_as_bool("FOO") == Path('./foo')
            >>>
            >>> os.environ['FOO'] = './foo'
            >>> assert Env.parse_as_bool("FOO") == Path('./foo')
            >>>
            >>> v = "https://github.com"
            >>> os.environ['FOO'] = v
            >>> assert Env.parse_as_bool("FOO").geturl() == v
            >>>
            >>> v = "git@github.com"
            >>> os.environ['FOO'] = v
            >>> assert Env.parse_as_bool("FOO").geturl() == v
            >>>
            >>> v = "0.0.0.0"
            >>> os.environ['FOO'] = v
            >>> assert Env.parse_as_bool("FOO").exploded == v
            >>>
            >>> os.environ['FOO'] = "::1"
            >>> assert Env.parse_as_bool("FOO").exploded.endswith(":0001")
            >>>
            >>> v = "2"
            >>> os.environ['FOO'] = v
            >>> assert Env.parse_as_bool("FOO") == int(v)
            >>>
            >>> v = "2.0"
            >>> os.environ['FOO'] = v
            >>> assert Env.parse_as_bool("FOO") == v
            >>>
            >>> del os.environ['FOO']
            >>> assert Env.parse_as_bool("FOO") is None

        Returns:
            None
        """
        if value := os.environ.get(variable):
            if variable in ("SUDO_UID", "SUDO_GID"):
                return int(value)
            if variable == "PATH":
                return value
            return parse_str(value)
        return value

    @classmethod
    def parse_as_int(
        cls,
        name: str = "USER",
    ) -> bool | Path | ParseResult | IPv4Address | IPv6Address | int | str | None:
        """Parses variable from environment using :func:`mreleaser.parse_str`,.

        except ``SUDO_UID`` or ``SUDO_GID`` which are parsed as int instead of bool.

        Arguments:
            name: variable name to parse from environment (default: USER)

        Examples:
            >>> from nodeps import Path
            >>> from nodeps import Env
            >>> assert isinstance(Env.parse_as_int(), str)
            >>>
            >>> os.environ['FOO'] = '1'
            >>> assert Env.parse_as_int("FOO") is True
            >>>
            >>> os.environ['FOO'] = '0'
            >>> assert Env.parse_as_int("FOO") is False
            >>>
            >>> os.environ['FOO'] = 'TrUe'
            >>> assert Env.parse_as_int("FOO") is True
            >>>
            >>> os.environ['FOO'] = 'OFF'
            >>> assert Env.parse_as_int("FOO") is False
            >>>
            >>> os.environ['FOO'] = '~/foo'
            >>> assert Env.parse_as_int("FOO") == Path('~/foo')
            >>>
            >>> os.environ['FOO'] = '/foo'
            >>> assert Env.parse_as_int("FOO") == Path('/foo')
            >>>
            >>> os.environ['FOO'] = './foo'
            >>> assert Env.parse_as_int("FOO") == Path('./foo')
            >>>
            >>> os.environ['FOO'] = './foo'
            >>> assert Env.parse_as_int("FOO") == Path('./foo')
            >>>
            >>> v = "https://github.com"
            >>> os.environ['FOO'] = v
            >>> assert Env.parse_as_int("FOO").geturl() == v
            >>>
            >>> v = "git@github.com"
            >>> os.environ['FOO'] = v
            >>> assert Env.parse_as_int("FOO").geturl() == v
            >>>
            >>> v = "0.0.0.0"
            >>> os.environ['FOO'] = v
            >>> assert Env.parse_as_int("FOO").exploded == v
            >>>
            >>> os.environ['FOO'] = "::1"
            >>> assert Env.parse_as_int("FOO").exploded.endswith(":0001")
            >>>
            >>> v = "2"
            >>> os.environ['FOO'] = v
            >>> assert Env.parse_as_int("FOO") == int(v)
            >>>
            >>> v = "2.0"
            >>> os.environ['FOO'] = v
            >>> assert Env.parse_as_int("FOO") == v
            >>>
            >>> del os.environ['FOO']
            >>> assert Env.parse_as_int("FOO") is None
            >>>
            >>> if not os.environ.get("CI"):
            ...     assert isinstance(Env.parse_as_int("PATH"), str)

        Returns:
            Value parsed
        """
        if value := os.environ.get(name):
            return cls.as_int(name, value)
        return value


@dataclasses.dataclass
class EnvBuilder(venv.EnvBuilder):
    """Wrapper for :class:`venv.EnvBuilder`.

    Changed defaults for: `prompt`` `symlinks` and `with_pip`, adds `env_dir` to `__init__` arguments.

    Post install in :py:meth:`.post_setup`.

    This class exists to allow virtual environment creation to be
    customized. The constructor parameters determine the builder's
    behaviour when called upon to create a virtual environment.

    By default, the builder makes the system (global) site-packages dir *un*available to the created environment.

    If invoked using the Python -m option, the default is to use copying
    on Windows platforms but symlinks elsewhere. If instantiated some
    other way, the default is to *not* use symlinks (changed with the wrapper to use symlinks always).

    Attributes:
        system_site_packages: bool
            If True, the system (global) site-packages dir is available to created environments.
        clear: bool
            If True, delete the contents of the environment directory if it already exists, before environment creation.
        symlinks: bool
            If True, attempt to symlink rather than copy files into virtual environment.
        upgrade: bool
            If True, upgrade an existing virtual environment.
        with_pip: bool
            If True, ensure pip is installed in the virtual environment.
        prompt: str
            Alternative terminal prefix for the environment.
        upgrade_deps: bool
            Update the base venv modules to the latest on PyPI (python 3.9+).
        context: Simplenamespace
            The information for the environment creation request being processed.
        env_dir: bool
            The target directory to create an environment in.
    """

    system_site_packages: bool = False
    clear: bool = False
    symlinks: bool = True
    upgrade: bool = True
    """Upgrades scripts and run :class:`venv.EnvBuilder.post_setup`."""
    with_pip: bool = True
    prompt: str | None = "."
    """To use basename use '.'."""
    upgrade_deps: bool = True
    """upgrades :data:`venv.CORE_VENV_DEPS`."""
    env_dir: Path | str | None = "venv"
    context: types.SimpleNamespace | None = dataclasses.field(default=None, init=False)

    def __post_init__(self):
        """Initialize the environment builder and also creates the environment is does not exist."""
        super().__init__(
            system_site_packages=self.system_site_packages,
            clear=self.clear,
            symlinks=self.symlinks,
            upgrade=self.upgrade,
            with_pip=self.with_pip,
            prompt=self.prompt,
            **({"upgrade_deps": self.upgrade_deps} if sys.version_info >= (3, 9) else {}),
        )
        if self.env_dir:
            self.env_dir = Path(self.env_dir).absolute()
            if self.env_dir.exists():
                self.ensure_directories()
            else:
                self.create(self.env_dir)

    def create(self, env_dir: Path | str | None = None) -> None:
        """Create a virtual environment in a directory.

        Args:
            env_dir: The target directory to create an environment in.
        """
        self.env_dir = env_dir or self.env_dir
        super().create(self.env_dir)

    def ensure_directories(self, env_dir: Path | str | None = None) -> types.SimpleNamespace:
        """Create the directories for the environment.

        Args:
            env_dir: The target directory to create an environment in.

        Returns:
            A context object which holds paths in the environment, for use by subsequent logic.
        """
        self.context = super().ensure_directories(env_dir or self.env_dir)
        return self.context

    def post_setup(self, context: types.SimpleNamespace | None = None) -> None:
        """Hook for post-setup modification of the venv.

        Subclasses may install additional packages or scripts here, add activation shell scripts, etc.

        Args:
            context: The information for the environment creation request being processed.
        """


@dataclasses.dataclass
class FileConfig:
    """FileConfig class."""

    file: Path | None = None
    config: dict = dataclasses.field(default_factory=dict)


@dataclasses.dataclass
class FrameSimple:
    """Simple frame class."""

    back: types.FrameType
    code: types.CodeType
    frame: types.FrameType
    function: str
    globals: dict[str, Any]  # noqa: A003, A003
    lineno: int
    locals: dict[str, Any]  # noqa: A003
    name: str
    package: str
    path: Path
    vars: dict[str, Any]  # noqa: A003


@dataclasses.dataclass
class GitUrl:
    """Parsed Git URL Helper Class.

    Attributes:
        data: Url, path or user (to be used with name), default None for cwd. Does not have .git unless is git+file
        repo: Repo name. If not None it will use data as the owner if not None, otherwise $GIT.

    Examples:
            >>> import nodeps
            >>> from nodeps import GitUrl
            >>> from nodeps import Path
            >>> from nodeps import NODEPS_PROJECT_NAME
            >>> from nodeps import NODEPS_PATH
            >>>
            >>> p = GitUrl()
            >>> p1 = GitUrl(nodeps.__file__)
            >>> p2 = GitUrl(repo=NODEPS_PROJECT_NAME)
            >>> p.host, p.owner, p.repo, p.protocol, p.protocols, p.platform, p.pathname, p.ownerrepo
            ('github.com', 'j5pu', 'nodeps', 'https', ['https'], 'github', '/j5pu/nodeps', 'j5pu/nodeps')
            >>> assert p2.url == p1.url == p.url == "https://github.com/j5pu/nodeps"
            >>> assert NODEPS_PATH == p1._path
            >>>
            >>> u = 'git@bitbucket.org:AaronO/some-repo.git'
            >>> p = GitUrl(u)
            >>> p.host, p.owner, p.repo, p.protocol, p.protocols, p.platform, p.pathname, p.ownerrepo
            ('bitbucket.org', 'AaronO', 'some-repo', 'ssh', ['ssh'], 'bitbucket', 'AaronO/some-repo.git',\
 'AaronO/some-repo')
            >>> assert p.normalized == u
            >>> assert p.url == u.removesuffix(".git")
            >>> assert p.ownerrepo == "AaronO/some-repo"
            >>>
            >>> u = "https://github.com/cpython/cpython"
            >>> p = GitUrl(u)
            >>> p.host, p.owner, p.repo, p.protocol, p.protocols, p.platform, p.pathname, p.ownerrepo
            ('github.com', 'cpython', 'cpython', 'https', ['https'], 'github', '/cpython/cpython', 'cpython/cpython')
            >>> assert p.normalized == u + ".git"
            >>> assert p.url == u
            >>>
            >>> p1 = GitUrl(data="cpython", repo="cpython")
            >>> assert p == p1
            >>>
            >>> u = "git+https://github.com/cpython/cpython"
            >>> p = GitUrl(u)
            >>> p.host, p.owner, p.repo, p.protocol, p.protocols, p.platform, p.pathname, p.ownerrepo
            ('github.com', 'cpython', 'cpython', 'https', ['git', 'https'], 'github', '/cpython/cpython',\
 'cpython/cpython')
            >>> p.normalized, p.url, p.url2githttps
            ('https://github.com/cpython/cpython.git', 'git+https://github.com/cpython/cpython',\
 'git+https://github.com/cpython/cpython.git')
            >>> assert p.normalized == u.removeprefix("git+") + ".git"
            >>> assert p.url == u
            >>> assert p.url2githttps == u + ".git"
            >>>
            >>> u = "git+ssh://git@github.com/cpython/cpython"
            >>> p = GitUrl(u)
            >>> p.host, p.owner, p.repo, p.protocol, p.protocols, p.platform, p.pathname, p.ownerrepo
            ('github.com', 'cpython', 'cpython', 'ssh', ['git', 'ssh'], 'github', '/cpython/cpython', 'cpython/cpython')
            >>> p.normalized, p.url, p.url2githttps
            ('git@github.com:cpython/cpython.git', 'git+ssh://git@github.com/cpython/cpython',\
 'git+https://github.com/cpython/cpython.git')
            >>> assert p.normalized == 'git@github.com:cpython/cpython.git'
            >>> assert p.url == u
            >>> assert p.url2gitssh == u + ".git"
            >>>
            >>> u = "git@github.com:cpython/cpython"
            >>> p = GitUrl(u)
            >>> p.host, p.owner, p.repo, p.protocol, p.protocols, p.platform, p.pathname, p.ownerrepo
            ('github.com', 'cpython', 'cpython', 'ssh', ['ssh'], 'github', 'cpython/cpython', 'cpython/cpython')
            >>> p.normalized, p.url, p.url2git
            ('git@github.com:cpython/cpython.git', 'git@github.com:cpython/cpython',\
 'git://github.com/cpython/cpython.git')
            >>> assert p.normalized == u + ".git"
            >>> assert p.url == u
            >>>
            >>> u = "https://domain.com/cpython/cpython"
            >>> p = GitUrl(u)
            >>> p.host, p.owner, p.repo, p.protocol, p.protocols, p.platform, p.pathname, p.ownerrepo
            ('domain.com', 'cpython', 'cpython', 'https', ['https'], 'gitlab', '/cpython/cpython', 'cpython/cpython')
            >>> p.normalized, p.url, p.url2https
            ('https://domain.com/cpython/cpython.git', 'https://domain.com/cpython/cpython',\
 'https://domain.com/cpython/cpython.git')
            >>> assert p.normalized == u + ".git"
            >>> assert p.url == u
            >>>
            >>> u = "git+https://domain.com/cpython/cpython"
            >>> p = GitUrl(u)
            >>> p.host, p.owner, p.repo, p.protocol, p.protocols, p.platform, p.pathname, p.ownerrepo
            ('domain.com', 'cpython', 'cpython', 'https', ['git', 'https'], 'gitlab', '/cpython/cpython',\
 'cpython/cpython')
            >>> p.normalized, p.url, p.url2githttps
            ('https://domain.com/cpython/cpython.git', 'git+https://domain.com/cpython/cpython',\
 'git+https://domain.com/cpython/cpython.git')
            >>> assert p.normalized == u.removeprefix("git+") + ".git"
            >>> assert p.url == u
            >>> assert p.url2githttps == u + ".git"
            >>>
            >>> u = "git+ssh://git@domain.com/cpython/cpython"
            >>> p = GitUrl(u)
            >>> p.host, p.owner, p.repo, p.protocol, p.protocols, p.platform, p.pathname, p.ownerrepo
            ('domain.com', 'cpython', 'cpython', 'ssh', ['git', 'ssh'], 'gitlab', '/cpython/cpython', 'cpython/cpython')
            >>> p.normalized, p.url, p.url2gitssh
            ('git@domain.com:cpython/cpython.git', 'git+ssh://git@domain.com/cpython/cpython',\
 'git+ssh://git@domain.com/cpython/cpython.git')
            >>> assert p.normalized == "git@domain.com:cpython/cpython.git"
            >>> assert p.url == u
            >>> assert p.url2gitssh == u + ".git"
            >>>
            >>> u = "git@domain.com:cpython/cpython"
            >>> p = GitUrl(u)
            >>> p.host, p.owner, p.repo, p.protocol, p.protocols, p.platform, p.pathname, p.ownerrepo
            ('domain.com', 'cpython', 'cpython', 'ssh', ['ssh'], 'gitlab', 'cpython/cpython', 'cpython/cpython')
            >>> p.normalized, p.url, p.url2ssh
            ('git@domain.com:cpython/cpython.git', 'git@domain.com:cpython/cpython',\
 'git@domain.com:cpython/cpython.git')
            >>> assert p.normalized == u + ".git"
            >>> assert p.url == u
            >>> assert p.url2ssh == u + ".git"
            >>>
            >>> u = "git+file:///tmp/cpython.git"
            >>> p = GitUrl(u)
            >>> p.host, p.owner, p.repo, p.protocol, p.protocols, p.platform, p.pathname, p.ownerrepo
            ('/tmp', '', 'cpython', 'file', ['git', 'file'], 'base', '/cpython.git', 'cpython')
            >>> p.normalized, p.url
            ('git+file:///tmp/cpython.git', 'git+file:///tmp/cpython.git')
            >>>
            >>> p = GitUrl("git+file:///tmp/cpython")
            >>> p.host, p.owner, p.repo, p.protocol, p.protocols, p.platform, p.pathname, p.ownerrepo
            ('/tmp', '', 'cpython', 'file', ['git', 'file'], 'base', '/cpython', 'cpython')
            >>> p.normalized, p.url
            ('git+file:///tmp/cpython.git', 'git+file:///tmp/cpython.git')
            >>> assert p.normalized == u
            >>> assert p.url == u
    """
    data: dataclasses.InitVar[str | Path | None] = ""
    """Url, path or user (to be used with name), default None for cwd. Does not have .git unless is git+file"""
    repo: str = dataclasses.field(default="", hash=True)
    """Repo name. If not None it will use data as the owner if not None, otherwise $GIT."""

    _platform_obj: (
        AssemblaPlatform | BasePlatform | BitbucketPlatform | FriendCodePlatform | GitHubPlatform | GitLabPlatform
    ) = dataclasses.field(default_factory=BasePlatform, init=False)
    _path: Path | None = dataclasses.field(default=None, init=False)
    """Path from __post_init__ method when path is provided in url argument."""
    _user: str = dataclasses.field(default="", init=False)
    access_token: str = dataclasses.field(default="", init=False)
    branch: str = dataclasses.field(default="", init=False)
    domain: str = dataclasses.field(default="", init=False)
    groups_path: str = dataclasses.field(default="", init=False)
    owner: str = dataclasses.field(default="", hash=True, init=False)
    ownerrepo: str = dataclasses.field(default="", init=False)
    path: str = dataclasses.field(default="", init=False)
    pathname: str = dataclasses.field(default="", init=False)
    path_raw: str = dataclasses.field(default="", init=False)
    platform: str = dataclasses.field(default="", init=False)
    protocol: str = dataclasses.field(default="", init=False)
    protocols: list[str] = dataclasses.field(default_factory=list, init=False)
    port: str = dataclasses.field(default="", init=False)
    url: str | Path = dataclasses.field(default="", hash=True, init=False)
    username: str = dataclasses.field(default="", init=False)
    api_repos_url: ClassVar[str] = f"{GITHUB_URL['api']}/repos"

    def __post_init__(self, data: str | Path | None):  # noqa: PLR0912
        """Post Init."""
        self.url = "" if data is None else str(data)  # because of CLI g default Path is None
        parsed_info = collections.defaultdict(lambda: "")
        parsed_info["protocols"] = cast(str, [])
        self._path = None

        if self.repo:
            parsed_info["repo"] = self.repo
            self.url = f"https://github.com/{self.url or GIT}/{self.repo}"
        elif not self.url:
            self._path = Path.cwd().absolute()
        elif (_path := Path(self.url)).exists():
            self._path = _path.to_parent()
        self.url = stdout(f"git -C {self._path} config --get remote.origin.url") if self._path else self.url

        if self.url is None:
            msg = f"Invalid argument: {data=}, {self.repo=}"
            raise InvalidArgumentError(msg)

        found = False
        for name, plat in PLATFORMS:
            for protocol, regex in plat.COMPILED_PATTERNS.items():
                # Match current regex against URL
                if not (match := regex.match(self.url)):
                    # Skip if not matched
                    continue

                # Skip if domain is bad
                domain = match.group("domain")

                # print('[%s] DOMAIN = %s' % (url, domain,))
                if plat.DOMAINS and domain not in plat.DOMAINS:
                    continue
                if plat.SKIP_DOMAINS and domain in plat.SKIP_DOMAINS:
                    continue

                found = True

                # add in platform defaults
                parsed_info.update(plat.DEFAULTS)

                # Get matches as dictionary
                matches = plat.clean_data(match.groupdict(default=""))

                # Update info with matches
                parsed_info.update(matches)

                owner = f"{parsed_info['owner']}/" if parsed_info["owner"] else ""

                if protocol == "ssh" and "ssh" not in parsed_info["protocols"]:
                    # noinspection PyUnresolvedReferences
                    parsed_info["protocols"].append(protocol)

                if protocol == "file" and not domain.startswith("/"):
                    msg = f"Invalid argument, git+file should have an absolute path: {data=}, {self.repo=}"
                    raise InvalidArgumentError(msg)

                parsed_info.update(
                    {
                        "url": self.url.removesuffix(".git")
                        if protocol != "file"
                        else self.url
                        if self.url.endswith(".git")
                        else f"{self.url}.git",
                        "platform": name,
                        "protocol": protocol,
                        "ownerrepo": f"{owner}{parsed_info['repo']}",
                    }
                )

                for k, v in parsed_info.items():
                    setattr(self, k, v)
                break

            if found:
                break

        for name, plat in PLATFORMS:
            if name == self.platform:
                self._platform_obj = plat
                break

        if not self.repo and self._path:
            self.repo = self._path.name

    def admin(self, user: str = GIT, rm: bool = False) -> bool:
        """Check if user has admin permissions.

        Examples:
            >>> import nodeps
            >>> from nodeps import GitUrl
            >>> from nodeps import NODEPS_PROJECT_NAME
            >>>
            >>> assert GitUrl(nodeps.__file__).admin() is True
            >>> assert GitUrl(nodeps.__file__).admin("foo") is False

        Arguments:
            user: default $GIT
            rm: use pickle cache or remove it before

        Returns:
            bool
        """
        try:
            return (
                urljson(f"{self.api_repos_url}/{self.ownerrepo}/collaborators/{user}/permission", rm=rm)["permission"]
                == "admin"
            )
        except urllib.error.HTTPError as err:
            if err.code == 403 and err.reason == "Forbidden":  # noqa: PLR2004
                return False
            raise

    def default(self, rm: bool = False) -> str:
        """Default remote branch.

        Examples:
            >>> import nodeps
            >>> from nodeps import GitUrl
            >>>
            >>> assert GitUrl(nodeps.__file__).default() == "main"

        Args:
            rm: remove cache

        Returns:
            bool
        """
        return self.github(rm=rm)["default_branch"]

    def format(self, protocol):  # noqa: A003
        """Reformat URL to protocol."""
        items = dataclasses.asdict(self)
        items["port_slash"] = f"{self.port}/" if self.port else ""
        items["groups_slash"] = f"{self.groups_path}/" if self.groups_path else ""
        items["dot_git"] = "" if items["repo"].endswith(".git") else ".git"
        return self._platform_obj.FORMATS[protocol] % items

    def github(
        self,
        rm: bool = False,
    ) -> dict[str, str | list | dict[str, str | list | dict[str, str | list]]]:
        """GitHub repos api.

        Examples:
            >>> from nodeps import GitUrl
            >>> from nodeps import NODEPS_PROJECT_NAME
            >>>
            >>> assert GitUrl().github()["name"] == NODEPS_PROJECT_NAME

        Returns:
            dict: pypi information
            rm: use pickle cache or remove it.
        """
        return urljson(f"{self.api_repos_url}/{self.ownerrepo}", rm=rm)

    @property
    def groups(self):
        """List of groups. GitLab only."""
        if self.groups_path:
            return self.groups_path.split("/")
        return []

    @property
    def host(self):
        """Alias property for domain."""
        return self.domain

    @property
    def is_github(self):
        """GitHub platform."""
        return self.platform == "github"

    @property
    def is_bitbucket(self):
        """BitBucket platform."""
        return self.platform == "bitbucket"

    @property
    def is_friendcode(self):
        """FriendCode platform."""
        return self.platform == "friendcode"

    @property
    def is_assembla(self):
        """Assembla platform."""
        return self.platform == "assembla"

    @property
    def is_gitlab(self):
        """GitLab platform."""
        return self.platform == "gitlab"

    @property
    def name(self):
        """Alias property for repo."""
        return self.repo

    @property
    def normalized(self):
        """Normalize URL with .git."""
        return self.format(self.protocol)

    def public(self, rm: bool = False) -> bool:
        """Check if repo ius public.

        Examples:
            >>> import nodeps
            >>> from nodeps import GitUrl
            >>>
            >>> assert GitUrl(nodeps.__file__).public() is True
            >>> assert GitUrl(repo="pdf").public() is False

        Args:
            rm: remove cache

        Returns:
            bool
        """
        return self.github(rm=rm)["visibility"] == "public"

    @property
    def resource(self):
        """Alias property for domain."""
        return self.domain

    @property
    def url2git(self):
        """Rewrite url to git.

        Examples:
            >>> from nodeps import GitUrl
            >>>
            >>> url = 'git@github.com:Org/Private-repo.git'
            >>> p = GitUrl(url)
            >>> p.url2git
            'git://github.com/Org/Private-repo.git'
        """
        return self.format("git")

    @property
    def url2githttps(self):
        """Rewrite url to git.

        Examples:
            >>> from nodeps import GitUrl
            >>>
            >>> url = 'git@github.com:Org/Private-repo.git'
            >>> p = GitUrl(url)
            >>> p.url2githttps
            'git+https://github.com/Org/Private-repo.git'
        """
        return self.format("git+https")

    @property
    def url2gitssh(self):
        """Rewrite url to git.

        Examples:
            >>> from nodeps import GitUrl
            >>>
            >>> url = 'git@github.com:Org/Private-repo.git'
            >>> p = GitUrl(url)
            >>> p.url2gitssh
            'git+ssh://git@github.com/Org/Private-repo.git'
        """
        return self.format("git+ssh")

    @property
    def url2https(self):
        """Rewrite url to https.

        Examples:
            >>> from nodeps import GitUrl
            >>>
            >>> url = 'git@github.com:Org/Private-repo.git'
            >>> p = GitUrl(url)
            >>> p.url2https
            'https://github.com/Org/Private-repo.git'
        """
        return self.format("https")

    @property
    def url2ssh(self):
        """Rewrite url to ssh.

        Examples:
            >>> from nodeps import GitUrl
            >>>
            >>> url = 'git@github.com:Org/Private-repo.git'
            >>> p = GitUrl(url)
            >>> p.url2ssh
            'git@github.com:Org/Private-repo.git'
        """
        return self.format("ssh")

    @property
    def urls(self):
        """All supported urls for a repo.

        Examples:
            >>> from nodeps import GitUrl
            >>> url = 'git@github.com:Org/Private-repo.git'
            >>>
            >>> GitUrl(url).urls
            {'git': 'git://github.com/Org/Private-repo.git',\
 'git+https': 'git+https://github.com/Org/Private-repo.git',\
 'git+ssh': 'git+ssh://git@github.com/Org/Private-repo.git',\
 'https': 'https://github.com/Org/Private-repo.git',\
 'ssh': 'git@github.com:Org/Private-repo.git'}
        """
        return {protocol: self.format(protocol) for protocol in self._platform_obj.PROTOCOLS}

    @property
    def user(self):
        """Alias property for _user or owner. _user == "git for ssh."""
        if hasattr(self, "_user"):
            return self._user

        return self.owner

    @property
    def valid(self):
        """Checks if url is valid.

        It is equivalent to :meth:`validate`.

        Examples:
            >>> from nodeps import GitUrl
            >>>
            >>> url = 'git@github.com:Org/Private-repo.git'
            >>> GitUrl(url).valid
            True
            >>> GitUrl.validate(url)
            True

        """
        return all(
            [
                all(
                    getattr(self, attr, None)
                    for attr in (
                        "domain",
                        "repo",
                    )
                ),
            ]
        )

    @classmethod
    def validate(cls, data: str | Path | None = None, repo: str | None = None):
        """Validate url.

        Examples:
            >>> from nodeps import GitUrl
            >>>
            >>> u = 'git@bitbucket.org:AaronO/some-repo.git'
            >>> p = GitUrl(u)
            >>> p.host, p.owner, p.repo
            ('bitbucket.org', 'AaronO', 'some-repo')
            >>> assert p.valid is True
            >>> assert GitUrl.validate(u) is True

        Args:
            data: user (when repo is provided, default GIT), url,
                path to get from git config if exists, default None for cwd.
            repo: repo to parse url from repo and get user from data
        """
        return cls(data=data, repo=repo).valid


@dataclasses.dataclass
class Gh(GitUrl):
    """Git Repo Class.

    Examples:
        >>> import os
        >>> import pytest
        >>> import nodeps
        >>> from nodeps import Gh
        >>>
        >>> r = Gh()
        >>> r.url # doctest: +ELLIPSIS
        'https://github.com/.../nodeps'

    Args:
        owner: repo owner or Path
        repo: repo name or repo path for git+file scheme (default: None)

    Raises:
        InvalidArgumentError: if GitUrl is not initialized with path
    """

    def __post_init__(self, data: str | Path | None = None):
        """Post Init."""
        super().__post_init__(data=data)
        if not self._path:
            msg = f"Path must be provided when initializing {self.__class__.__name__}: {data=}, {self.repo=}"
            raise InvalidArgumentError(msg)

        self.git = f"git -C '{self._path}'"
        self.log = ColorLogger.logger(self.__class__.__qualname__)

    def info(self, msg: str):
        """Logger info."""
        self.log.info(msg, extra={"extra": self.repo})

    def warning(self, msg: str):
        """Logger warning."""
        self.log.warning(msg, extra={"extra": self.repo})

    def commit(self, msg: str | None = None, force: bool = False, quiet: bool = True) -> None:
        """commit.

        Raises:
            CalledProcessError: if  fails
            RuntimeError: if diverged or dirty
        """
        status = self.status(quiet=quiet)
        if status.dirty:
            if status.diverge and not force:
                msg = f"Diverged: {status=}, {self.repo=}"
                raise RuntimeError(msg)
            if msg is None or msg == "":
                msg = "fix: "
            self.git_check_call("add -A")
            self.git_check_call(f"commit -a {'--quiet' if quiet else ''} -m '{msg}'")
            self.info(self.commit.__name__)

    def current(self) -> str:
        """Current branch.

        Examples:
            >>> from nodeps import Gh
            >>>
            >>> assert Gh().current() == 'main'
        """
        return self.git_stdout("branch --show-current") or ""

    def gh_check_call(self, line: str):
        """Runs git command and raises exception if error (stdout is not captured and shown).

        Examples:
            >>> from nodeps import Gh
            >>>
            >>> assert Gh().gh_check_call("repo view") == 0  # doctest: +SKIP
        """
        return subprocess.check_call(f"gh {line}", shell=True, cwd=self._path)

    def gh_stdout(self, line: str):
        """Runs git command and returns stdout.

        Examples:
            >>> from nodeps import Gh
            >>> from nodeps import NODEPS_PROJECT_NAME
            >>>
            >>> assert NODEPS_PROJECT_NAME in Gh().gh_stdout("repo view")  # doctest: +SKIP
        """
        return stdout(f"gh {line}", cwd=self._path)

    def git_check_call(self, line: str):
        """Runs git command and raises exception if error (stdout is not captured and shown).

        Examples:
            >>> from nodeps import Gh
            >>>
            >>> assert Gh().git_check_call("rev-parse --abbrev-ref HEAD") == 0

        """
        return subprocess.check_call(f"{self.git} {line}", shell=True)

    def git_stdout(self, line: str):
        """Runs git command and returns stdout.

        Examples:
            >>> from nodeps import Gh
            >>>
            >>> assert Gh().git_stdout("rev-parse --abbrev-ref HEAD") == "main"
        """
        return stdout(f"{self.git} {line}")

    def latest(self) -> str:
        """Latest tag: git {c} describe --abbrev=0 --tags."""
        latest = self.git_stdout("tag | sort -V | tail -1") or ""
        if not latest:
            latest = "0.0.0"
            self.commit(msg=f"{self.latest.__name__}: {latest}")
            self._tag(latest)
        return latest

    def _next(self, part: Bump = Bump.PATCH) -> str:
        latest = self.latest()
        v = "v" if latest.startswith("v") else ""
        version = latest.replace(v, "").split(".")
        match part:
            case Bump.MAJOR:
                index = 0
            case Bump.MINOR:
                index = 1
            case _:
                index = 2
        version[index] = str(int(version[index]) + 1)
        return f"{v}{'.'.join(version)}"

    def next(self, part: Bump = Bump.PATCH, force: bool = False) -> str:  # noqa: A003
        """Show next version based on fix: feat: or BREAKING CHANGE:.

        Args:
            part: part to increase if force
            force: force bump
        """
        latest = self.latest()
        out = self.git_stdout(f"log --pretty=format:'%s' {latest}..@")
        if force:
            return self._next(part)
        if out:
            if "breaking change:" in out.lower():
                return self._next(Bump.MAJOR)
            if "feat:" in out.lower():
                return self._next(Bump.MINOR)
            if "fix:" in out.lower():
                return self._next()
        return latest

    def pull(self, force: bool = False, quiet: bool = True) -> None:
        """pull.

        Raises:
            CalledProcessError: if pull fails
            RuntimeError: if diverged or dirty
        """
        status = self.status(quiet=quiet)
        if status.diverge and not force:
            msg = f"Diverged: {status=}, {self.repo=}"
            raise RuntimeError(msg)
        if status.pull:
            self.git_check_call(f"pull {'--force' if force else ''} {'--quiet' if quiet else ''}")
            self.info(self.pull.__name__)

    def push(self, force: bool = False, quiet: bool = True) -> None:
        """push.

        Raises:
            CalledProcessError: if push fails
            RuntimeError: if diverged
        """
        self.commit(force=force, quiet=quiet)
        status = self.status(quiet=quiet)
        if status.push:
            if status.pull and not force:
                msg = f"Diverged: {status=}, {self.repo=}"
                raise RuntimeError(msg)
            self.git_check_call(f"push {'--force' if force else ''} {'--quiet' if quiet else ''}")
            self.info(self.push.__name__)

    def secrets(self, force: bool = False) -> int:
        """Update GitHub repository secrets."""
        if os.environ.get("CI") is not None:
            return 0
        if not self.secrets_names() or force:
            self.gh_check_call(f"secret set GH_TOKEN --body {GITHUB_TOKEN}")
            if (secrets := Path.home() / "secrets/profile.d/secrets.sh").is_file():
                with tempfile.NamedTemporaryFile() as tmp:
                    subprocess.check_call(
                        f"grep -v GITHUB_ {secrets} > {tmp.name} && cd {self._path} && gh secret set -f {tmp.name}",
                        shell=True,
                    )
                    self.info(self.secrets.__name__)
        return 0

    def secrets_names(self):
        """List GitHub repository secrets names."""
        return self.gh_stdout("secret list --jq .[].name  --json name").splitlines()

    def status(self, quiet: bool = True) -> GitStatus:
        """Git status instance and fetch if necessary."""
        diverge = pull = push = False
        local = self.git_stdout("rev-parse @")
        base = remote = self.git_stdout("ls-remote origin HEAD | awk '{ print $1 }'")

        dirty = bool(self.git_stdout("status -s"))
        if local != remote:
            self.git_check_call(f"fetch --all --tags --prune {'--quiet' if quiet else ''}")
            base = self.git_stdout("merge-base @ @{u}")
            if local == base:
                pull = True
                diverge = dirty
            elif remote == base:
                push = True
            else:
                diverge = True
                pull = True
                push = True
        return GitStatus(base=base, dirty=dirty, diverge=diverge, local=local, pull=pull, push=push, remote=remote)

    def superproject(self) -> Path | None:
        """Git rev-parse --show-superproject-working-tree --show-toplevel."""
        if v := self.git_stdout("rev-parse --show-superproject-working-tree --show-toplevel"):
            return Path(v[0])
        return None

    def _tag(self, tag: str, quiet: bool = True) -> None:
        self.git_check_call(f"tag {tag}")
        self.git_check_call(f"push origin {tag} {'--quiet' if quiet else ''}")
        self.info(f"{self.tag.__name__}: {tag}")

    def tag(self, tag: str, quiet: bool = True) -> str | None:
        """Git tag."""
        if self.latest() == tag:
            self.warning(f"{self.tag.__name__}: {tag} -> nothing to do")
            return
        self._tag(tag, quiet=quiet)

    def sync(self):
        """Sync repository."""
        self.push()
        self.pull()

    def top(self) -> Path | None:
        """Git rev-parse --show-toplevel."""
        if v := self.git_stdout("rev-parse --show-toplevel"):
            return Path(v)
        return None



class MyPrompt(Prompts):
    """IPython prompt."""

    @property
    def project(self) -> Project:
        """Project instance."""
        return Project()

    def in_prompt_tokens(self, cli=None):
        """In prompt tokens."""
        return [
            (Token, ""),
            (Token.OutPrompt, pathlib.Path().absolute().stem),
            (Token, " "),
            (Token.Generic, "↪"),
            (Token.Generic, self.project.gh.current()),
            *((Token, " "), (Token.Prompt, "©") if os.environ.get("VIRTUAL_ENV") else (Token, "")),
            (Token, " "),
            (Token.Name.Class, "v" + platform.python_version()),
            (Token, " "),
            (Token.Name.Entity, self.project.gh.latest()),
            (Token, " "),
            (Token.Prompt, "["),
            (Token.PromptNum, str(self.shell.execution_count)),
            (Token.Prompt, "]: "),
            (
                Token.Prompt if self.shell.last_execution_succeeded else Token.Generic.Error,
                "❯ ",  # noqa: RUF001
            ),
        ]

    def out_prompt_tokens(self, cli=None):
        """Out Prompt."""
        return [
            (Token.OutPrompt, "Out<"),
            (Token.OutPromptNum, str(self.shell.execution_count)),
            (Token.OutPrompt, ">: "),
        ]


class Noset:
    """Marker object for globals not initialized or other objects.

    Examples:
        >>> from nodeps import NOSET
        >>>
        >>> name = Noset.__name__.lower()
        >>> assert str(NOSET) == f'<{name}>'
        >>> assert repr(NOSET) == f'<{name}>'
        >>> assert repr(Noset("test")) == f'<test>'
    """

    name: str
    __slots__ = ("name",)

    def __init__(self, name: str = ""):
        """Init."""
        self.name = name if name else self.__class__.__name__.lower()

    def __hash__(self) -> int:
        """Hash."""
        return hash(
            (
                self.__class__,
                self.name,
            )
        )

    def __reduce__(self) -> tuple[type[Noset], tuple[str]]:
        """Reduce."""
        return self.__class__, (self.name,)

    def __repr__(self):
        """Repr."""
        return self.__str__()

    def __str__(self):
        """Str."""
        return f"<{self.name}>"


@dataclasses.dataclass
class Project:
    """Project Class."""

    data: Path | str | types.ModuleType = None
    """File, directory or name (str or path with one word) of project (default: current working directory)"""
    brewfile: Path | None = dataclasses.field(default=None, init=False)
    """Data directory Brewfile"""
    ci: bool = dataclasses.field(default=False, init=False)
    """running in CI or tox"""
    data_dir: Path | None = dataclasses.field(default=None, init=False)
    """Data directory"""
    directory: Path | None = dataclasses.field(default=None, init=False)
    """Parent of data if data is a file or None if it is a name (one word)"""
    docsdir: Path | None = dataclasses.field(default=None, init=False)
    """Docs directory"""
    gh: Gh = dataclasses.field(default=None, init=False)
    git: str = dataclasses.field(default="git", init=False)
    """git -C directory if self.directory is not None"""
    installed: bool = dataclasses.field(default=False, init=False)
    name: str = dataclasses.field(default=None, init=False)
    """Pypi project name from setup.cfg, pyproject.toml or top name or self.data when is one word"""
    profile: Path | None = dataclasses.field(default=None, init=False)
    """Data directory profile.d"""
    pyproject_toml: FileConfig = dataclasses.field(default_factory=FileConfig, init=False)
    repo: Path = dataclasses.field(default=None, init=False)
    """top or superproject"""
    root: Path = dataclasses.field(default=None, init=False)
    """pyproject.toml or setup.cfg parent or superproject or top directory"""
    source: Path | None = dataclasses.field(default=None, init=False)
    """sources directory, parent of __init__.py or module path"""
    clean_match: ClassVar[list[str]] = ["*.egg-info", "build", "dist"]
    rm: dataclasses.InitVar[bool] = False
    """remove cache"""

    def __post_init__(self, rm: bool = False):  # noqa: PLR0912, PLR0915
        """Post init."""
        self.ci = any([in_tox(), os.environ.get("CI")])
        self.data = self.data if self.data else Path.cwd()
        data = Path(self.data.__file__ if isinstance(self.data, types.ModuleType) else self.data)
        if (
            (isinstance(self.data, str) and len(toiter(self.data, split="/")) == 1)
            or (isinstance(self.data, pathlib.PosixPath) and len(self.data.parts) == 1)
        ) and (str(self.data) != "/"):
            if r := self.repos(ret=ProjectRepos.DICT, rm=rm).get(self.data
                                                                 if isinstance(self.data, str) else self.data.name):
                self.directory = r
        elif data.is_dir():
            self.directory = data.absolute()
        elif data.is_file():
            self.directory = data.parent.absolute()
        else:
            msg = f"Invalid argument: {self.data=}"
            raise InvalidArgumentError(msg)

        if self.directory:
            self.git = f"git -C '{self.directory}'"
            if ((path := findup(self.directory, name="pyproject.toml", uppermost=True))
                    and (path.parent / ".git").exists()):
                path = path[0] if isinstance(path, list) else path
                with pipmetapathfinder():
                    import tomlkit
                with Path.open(path, "rb") as f:
                    self.pyproject_toml = FileConfig(path, tomlkit.load(f))
                self.name = self.pyproject_toml.config.get("project", {}).get("name")
                self.root = path.parent
            elif ((path := findup(self.directory, name=".git", kind="exists", uppermost=True))
                    and (path.parent / ".git").exists()):
                self.root = path.parent
                self.name = self.root.name

            if self.root:
                self.gh = Gh(self.root)
                self.repo = self.gh.top() or self.gh.superproject()
            purelib = sysconfig.get_paths()["purelib"]
            if root := self.root or self.repo:
                self.root = root.absolute()
                if (src := (root / "src")) and (str(src) not in sys.path):
                    sys.path.insert(0, str(src))
            elif self.directory.is_relative_to(purelib):
                self.name = Path(self.directory).relative_to(purelib).parts[0]
            self.name = self.name if self.name else self.root.name if self.root else None
        else:
            self.name = str(self.data)

        try:
            if self.name and ((spec := importlib.util.find_spec(self.name)) and spec.origin):
                self.source = Path(spec.origin).parent if "__init__.py" in spec.origin else Path(spec.origin)
                self.installed = True
                self.root = self.root if self.root else self.source.parent
                purelib = sysconfig.get_paths()["purelib"]
                self.installed = bool(self.source.is_relative_to(purelib) or Path(purelib).name in str(self.source))
        except (ModuleNotFoundError, ImportError):
            pass

        if self.source:
            self.data_dir = d if (d := self.source / "data").is_dir() else None
            if self.data_dir:
                self.brewfile = b if (b := self.data_dir / "Brewfile").is_file() else None
                self.profile = pr if (pr := self.data_dir / "profile.d").is_dir() else None
        if self.root:
            self.docsdir = doc if (doc := self.root / "docs").is_dir() else None
            if self.gh is None and (self.root / ".git").exists():
                self.gh = Gh(self.root)
        self.log = ColorLogger.logger(__name__)

    def info(self, msg: str):
        """Logger info."""
        self.log.info(msg, extra={"extra": self.name})

    def warning(self, msg: str):
        """Logger warning."""
        self.log.warning(msg, extra={"extra": self.name})

    def bin(self, executable: str | None = None, version: str = PYTHON_DEFAULT_VERSION) -> Path:  # noqa: A003
        """Bin directory.

        Args;
            executable: command to add to path
            version: python version
        """
        return Path(self.executable(version=version)).parent / executable if executable else ""

    def brew(self, c: str | None = None) -> int:
        """Runs brew bundle."""
        if which("brew") and self.brewfile and (c is None or not which(c)):
            rv = subprocess.run(
                [
                    "brew",
                    "bundle",
                    "--no-lock",
                    "--quiet",
                    f"--file={self.brewfile}",
                ],
                shell=False,
            ).returncode
            self.info(self.brew.__name__)
            return rv
        return 0

    def browser(self, version: str = PYTHON_DEFAULT_VERSION, quiet: bool = True) -> int:
        """Build and serve the documentation with live reloading on file changes.

        Arguments:
            version: python version
            quiet: quiet mode (default: True)
        """
        global NODEPS_QUIET  # noqa: PLW0603
        NODEPS_QUIET = quiet

        if not self.docsdir:
            return 0
        build_dir = self.docsdir / "_build"
        q = "-Q" if quiet else ""
        if build_dir.exists():
            shutil.rmtree(build_dir)

        if (
            subprocess.check_call(
                f"{self.executable(version=version)} -m sphinx_autobuild {q} {self.docsdir} {build_dir}", shell=True
            )
            == 0
        ):
            self.info(self.docs.__name__)
        return 0

    def build(self, version: str = PYTHON_DEFAULT_VERSION, quiet: bool = True, rm: bool = False) -> Path | None:
        """Build a project `venv`, `completions`, `docs` and `clean`.

        Arguments:
            version: python version (default: PYTHON_DEFAULT_VERSION)
            quiet: quiet mode (default: True)
            rm: remove cache
        """
        # TODO: el pth sale si execute en terminal pero no en run
        global NODEPS_QUIET  # noqa: PLW0603
        NODEPS_QUIET = quiet

        if not self.pyproject_toml.file:
            return None
        self.venv(version=version, quiet=quiet, rm=rm)
        self.completions()
        self.docs(quiet=quiet)
        self.clean()
        rv = subprocess.run(
            f"{self.executable(version=version)} -m build {self.root} --wheel",
            stdout=subprocess.PIPE,
            shell=True,
        )
        if rv.returncode != 0:
            sys.exit(rv.returncode)
        wheel = rv.stdout.splitlines()[-1].decode().split(" ")[2]
        if "py3-none-any.whl" not in wheel:
            raise CalledProcessError(completed=rv)
        self.info(
            f"{self.build.__name__}: {wheel}: {version}",
        )
        return self.root / "dist" / wheel

    def builds(self, quiet: bool = True, rm: bool = False) -> None:
        """Build a project `venv`, `completions`, `docs` and `clean`.

        Arguments:
            quiet: quiet mode (default: True)
            rm: remove cache
        """
        global NODEPS_QUIET  # noqa: PLW0603
        NODEPS_QUIET = quiet

        if self.ci:
            self.build(quiet=quiet, rm=rm)
        else:
            for version in PYTHON_VERSIONS:
                self.build(version=version, quiet=quiet, rm=rm)

    def buildrequires(self) -> list[str]:
        """pyproject.toml build-system requires."""
        if self.pyproject_toml.file:
            return self.pyproject_toml.config.get("build-system", {}).get("requires", [])
        return []

    def clean(self) -> None:
        """Clean project."""
        if not in_tox():
            for item in self.clean_match:
                try:
                    for file in self.root.rglob(item):
                        if file.is_dir():
                            shutil.rmtree(self.root / item, ignore_errors=True)
                        else:
                            file.unlink(missing_ok=True)
                except FileNotFoundError:
                    pass

    def completions(self, uninstall: bool = False):
        """Generate completions to /usr/local/etc/bash_completion.d."""
        value = []

        if self.pyproject_toml.file:
            value = self.pyproject_toml.config.get("project", {}).get("scripts", {}).keys()
        elif d := self.distribution():
            value = [item.name for item in d.entry_points]
        if value:
            for item in value:
                if file := completions(item, uninstall=uninstall):
                    self.info(f"{self.completions.__name__}: {item} -> {file}")

    def coverage(self) -> int:
        """Runs coverage."""
        if (
            self.pyproject_toml.file
            and subprocess.check_call(f"{self.executable()} -m coverage run -m pytest {self.root}", shell=True) == 0
            and subprocess.check_call(
                f"{self.executable()} -m coverage report --data-file={self.root}/reports/.coverage",
                shell=True,
            )
            == 0
        ):
            self.info(self.coverage.__name__)
        return 0

    def dependencies(self) -> list[str]:
        """Dependencies from pyproject.toml or distribution."""
        if self.pyproject_toml.config:
            return self.pyproject_toml.config.get("project", {}).get("dependencies", [])
        if d := self.distribution():
            return [item for item in d.requires if "; extra" not in item]
        msg = f"Dependencies not found for {self.name=}"
        raise RuntimeWarning(msg)

    def distribution(self) -> importlib.metadata.Distribution | None:
        """Distribution."""
        return suppress(importlib.metadata.Distribution.from_name, self.name)

    def docs(self, version: str = PYTHON_DEFAULT_VERSION, quiet: bool = True) -> int:
        """Build the documentation.

        Arguments:
            version: python version
            quiet: quiet mode (default: True)
        """
        global NODEPS_QUIET  # noqa: PLW0603
        NODEPS_QUIET = quiet

        if not self.docsdir:
            return 0
        build_dir = self.docsdir / "_build"
        q = "-Q" if quiet else ""
        if build_dir.exists():
            shutil.rmtree(build_dir)

        if (
            subprocess.check_call(
                f"{self.executable(version=version)} -m sphinx {q} --color {self.docsdir} {build_dir}",
                shell=True,
            )
            == 0
        ):
            self.info(f"{self.docs.__name__}: {version}")
        return 0

    def executable(self, version: str = PYTHON_DEFAULT_VERSION) -> Path:
        """Executable."""
        return v / f"bin/python{version}" if (v := self.root / "venv").is_dir() and not self.ci else sys.executable

    @staticmethod
    def _extras(d):
        e = {}
        for item in d:
            if "; extra" in item:
                key = item.split("; extra == ")[1].replace("'", "").replace('"', "").removesuffix(" ")
                if key not in e:
                    e[key] = []
                e[key].append(item.split("; extra == ")[0].replace('"', "").removesuffix(" "))
        return e

    def extras(self, as_list: bool = False, rm: bool = False) -> dict[str, list[str]] | list[str]:
        """Optional dependencies from pyproject.toml or distribution.

        Examples:
            >>> import typer
            >>> from nodeps import Project
            >>>
            >>> nodeps = Project.nodeps()
            >>> nodeps.extras()  # doctest: +ELLIPSIS
            {'ansi': ['...
            >>> nodeps.extras(as_list=True)  # doctest: +ELLIPSIS
            ['...
            >>> Project(typer.__name__).extras()  # doctest: +ELLIPSIS
            {'all':...
            >>> Project("sampleproject").extras()  # doctest: +ELLIPSIS
            {'dev':...

        Args:
            as_list: return as list
            rm: remove cache

        Returns:
            dict or list
        """
        if self.pyproject_toml.config:
            e = self.pyproject_toml.config.get("project", {}).get("optional-dependencies", {})
        elif d := self.distribution():
            e = self._extras(d.requires)
        elif pypi := self.pypi(rm=rm):
            e = self._extras(pypi["info"]["requires_dist"])
        else:
            msg = f"Extras not found for {self.name=}"
            raise RuntimeWarning(msg)

        if as_list:
            return sorted({extra for item in e.values() for extra in item})
        return e

    @classmethod
    def nodeps(cls) -> Project:
        """Project Instance of nodeps."""
        return cls(__file__)

    def publish(
        self,
        part: Bump = Bump.PATCH,
        force: bool = False,
        ruff: bool = True,
        tox: bool = False,
        quiet: bool = True,
        rm: bool = False,
    ):
        """Publish runs runs `tests`, `commit`, `tag`, `push`, `twine` and `clean`.

        Args:
            part: part to increase if force
            force: force bump
            ruff: run ruff
            tox: run tox
            quiet: quiet mode (default: True)
            rm: remove cache
        """
        global NODEPS_QUIET  # noqa: PLW0603
        NODEPS_QUIET = quiet

        self.tests(ruff=ruff, tox=tox, quiet=quiet)
        self.gh.commit()
        if (n := self.gh.next(part=part, force=force)) != (l := self.gh.latest()):
            self.gh.tag(n)
            self.gh.push()
            if rc := self.twine(rm=rm) != 0:
                sys.exit(rc)
            self.info(f"{self.publish.__name__}: {l} -> {n}")
        else:
            self.warning(f"{self.publish.__name__}: {n} -> nothing to do")

        self.clean()

    def pypi(
        self,
        rm: bool = False,
    ) -> dict[str, str | list | dict[str, str | list | dict[str, str | list]]]:
        """Pypi information for a package.

        Examples:
            >>> from nodeps import Project
            >>> from nodeps import NODEPS_PROJECT_NAME
            >>>
            >>> assert Project(NODEPS_PROJECT_NAME).pypi()["info"]["name"] == NODEPS_PROJECT_NAME

        Returns:
            dict: pypi information
            rm: use pickle cache or remove it.
        """
        return urljson(f"https://pypi.org/pypi/{self.name}/json", rm=rm)

    def pytest(self, version: str = PYTHON_DEFAULT_VERSION) -> int:
        """Runs pytest."""
        if self.pyproject_toml.file:
            rc = subprocess.run(f"{self.executable(version=version)} -m pytest {self.root}", shell=True).returncode
            self.info(f"{self.pytest.__name__}: {version}")
            return rc
        return 0

    def pytests(self) -> int:
        """Runs pytest for all versions."""
        rc = 0
        if self.ci:
            rc = self.pytest()
        else:
            for version in PYTHON_VERSIONS:
                rc = self.pytest(version=version)
                if rc != 0:
                    sys.exit(rc)
        return rc

    @classmethod
    def repos(
        cls,
        ret: ProjectRepos = ProjectRepos.NAMES,
        sync: bool = False,
        archive: bool = False,
        rm: bool = False,
    ) -> list[Path] | list[str] | dict[str, Project | str] | None:
        """Repo paths, names or Project instances under home and Archive.

        Examples:
            >>> from nodeps import Project
            >>> from nodeps import NODEPS_PROJECT_NAME
            >>>
            >>> assert NODEPS_PROJECT_NAME in Project.repos()
            >>> assert NODEPS_PROJECT_NAME in Project.repos(ProjectRepos.DICT)
            >>> assert NODEPS_PROJECT_NAME in Project.repos(ProjectRepos.INSTANCES)
            >>> assert NODEPS_PROJECT_NAME in Project.repos(ProjectRepos.PY)
            >>> assert "shrc" not in Project.repos(ProjectRepos.PY)

        Args:
            ret: return names, paths, dict or instances
            sync: push or pull all repos
            archive: look for repos under ~/Archive
            rm: remove cache
        """
        if rm or (rv := Path.pickle(name=cls.repos)) is None:
            add = sorted(add.iterdir()) if (add := Path.home() / "Archive").is_dir() and archive else []
            rv = {
                ProjectRepos.DICT: {},
                ProjectRepos.INSTANCES: {},
                ProjectRepos.NAMES: [],
                ProjectRepos.PATHS: [],
                ProjectRepos.PY: {},
            }
            for path in add + sorted(Path.home().iterdir()):
                if path.is_dir() and (path / ".git").exists() and Gh(path).admin(rm=rm):
                    instance = cls(path)
                    name = path.name
                    rv[ProjectRepos.DICT] |= {name: path}
                    rv[ProjectRepos.INSTANCES] |= {name: instance}
                    rv[ProjectRepos.NAMES].append(name)
                    rv[ProjectRepos.PATHS].append(path)
                    if instance.pyproject_toml.file:
                        rv[ProjectRepos.PY] |= {name: instance}
            Path.pickle(name=cls.repos, data=rv, rm=rm)

        if not rv:
            rv = Path.pickle(name=cls.repos)

        if sync:
            for item in rv[ProjectRepos.INSTANCES].values():
                item.sync()
            return None
        return rv[ret]

    def requirement(
        self,
        version: str = PYTHON_DEFAULT_VERSION,
        install: bool = False,
        upgrade: bool = False,
        quiet: bool = True,
        rm: bool = False,
    ) -> list[str] | int:
        """Dependencies and optional dependencies from pyproject.toml or distribution."""
        global NODEPS_QUIET  # noqa: PLW0603
        NODEPS_QUIET = quiet

        req = sorted({*self.dependencies() + self.extras(as_list=True, rm=rm)})
        req = [item for item in req if not item.startswith(f"{self.name}[")]
        if (install or upgrade) and req:
            upgrade = ["--upgrade"] if upgrade else []
            quiet = "-q" if quiet else ""
            rv = subprocess.check_call([self.executable(version), "-m", "pip", "install", quiet, *upgrade, *req])
            self.info(f"{self.requirements.__name__}: {version}")
            return rv
        return req

    def requirements(
        self,
        upgrade: bool = False,
        quiet: bool = True,
        rm: bool = False,
    ) -> None:
        """Install dependencies and optional dependencies from pyproject.toml or distribution for python versions."""
        global NODEPS_QUIET  # noqa: PLW0603
        NODEPS_QUIET = quiet

        if self.ci:
            self.requirement(install=True, upgrade=upgrade, quiet=quiet, rm=rm)
        else:
            for version in PYTHON_VERSIONS:
                self.requirement(version=version, install=True, upgrade=upgrade, quiet=quiet, rm=rm)

    def ruff(self, version: str = PYTHON_DEFAULT_VERSION) -> int:
        """Runs ruff."""
        if self.pyproject_toml.file:
            rv = subprocess.run(f"{self.executable(version=version)} -m ruff check {self.root}", shell=True).returncode
            self.info(f"{self.ruff.__name__}: {version}")
            return rv
        return 0

    # TODO: delete all tags and pypi versions

    def test(
        self, version: str = PYTHON_DEFAULT_VERSION, ruff: bool = True, tox: bool = False, quiet: bool = True
    ) -> int:
        """Test project, runs `build`, `ruff`, `pytest` and `tox`.

        Arguments:
            version: python version
            ruff: run ruff (default: True)
            tox: run tox (default: True)
            quiet: quiet mode (default: True)
        """
        global NODEPS_QUIET  # noqa: PLW0603
        NODEPS_QUIET = quiet

        self.build(version=version, quiet=quiet)
        if ruff and (rc := self.ruff(version=version) != 0):
            sys.exit(rc)

        if rc := self.pytest(version=version) != 0:
            sys.exit(rc)

        if tox and (rc := self.tox() != 0):
            sys.exit(rc)

        return rc

    def tests(self, ruff: bool = True, tox: bool = False, quiet: bool = True) -> int:
        """Test project, runs `build`, `ruff`, `pytest` and `tox` for all versions.

        Arguments:
            ruff: runs ruff
            tox: runs tox
            quiet: quiet mode (default: True)
        """
        global NODEPS_QUIET  # noqa: PLW0603
        NODEPS_QUIET = quiet

        rc = 0
        if self.ci:
            rc = self.test(ruff=ruff, tox=tox, quiet=quiet)
        else:
            for version in PYTHON_VERSIONS:
                rc = self.test(version=version, ruff=ruff, tox=tox, quiet=quiet)
                if rc != 0:
                    sys.exit(rc)
        return rc

    def tox(self) -> int:
        """Runs tox."""
        if self.pyproject_toml.file:
            rv = subprocess.run(f"{self.executable()} -m tox --root {self.root}", shell=True).returncode
            self.info(self.tox.__name__)
            return rv
        return 0

    def twine(
        self,
        part: Bump = Bump.PATCH,
        force: bool = False,
        rm: bool = False,
    ) -> int:
        """Twine.

        Args:
            part: part to increase if force
            force: force bump
            rm: remove cache
        """
        pypi = d.version if (d := self.distribution()) else None

        if (
            self.pyproject_toml.file
            and (pypi != self.gh.next(part=part, force=force))
            and "Private :: Do Not Upload" not in self.pyproject_toml.config.get("project", {}).get("classifiers", [])
        ):
            c = f"{self.executable()} -m twine upload -u __token__  {self.build(rm=rm).parent}/*"
            rc = subprocess.run(c, shell=True).returncode
            if rc != 0:
                return rc

        return 0

    def version(self, rm: bool = True) -> str:
        """Version from pyproject.toml, tag, distribution or pypi.

        Args:
            rm: remove cache
        """
        if v := self.pyproject_toml.config.get("project", {}).get("version"):
            return v
        if self.gh.top() and (v := self.gh.latest()):
            return v
        if d := self.distribution():
            return d.version
        if pypi := self.pypi(rm=rm):
            return pypi["info"]["version"]
        msg = f"Version not found for {self.name=} {self.directory=}"
        raise RuntimeWarning(msg)

    def venv(
        self,
        version: str = PYTHON_DEFAULT_VERSION,
        clear: bool = False,
        upgrade: bool = False,
        quiet: bool = True,
        rm: bool = False,
    ) -> None:
        """Creates venv, runs: `write` and `requirements`.

        Args:
            version: python version
            clear: remove venv
            upgrade: upgrade packages
            quiet: quiet
            rm: remove cache
        """
        global NODEPS_QUIET  # noqa: PLW0603
        NODEPS_QUIET = quiet

        version = "" if self.ci else version
        if not self.pyproject_toml.file:
            return
        if not self.root:
            msg = f"Undefined: {self.root=} for {self.name=} {self.directory=}"
            raise RuntimeError(msg)
        self.write(rm=rm)
        if not self.ci:
            v = self.root / "venv"
            python = f"python{version}"
            clear = "--clean" if clear else ""
            subprocess.check_call(f"{python} -m venv {v} --prompt '.' {clear} --upgrade-deps --upgrade", shell=True)
            self.info(f"{self.venv.__name__}: {version}")
        self.requirement(version=version, install=True, upgrade=upgrade, quiet=quiet, rm=rm)

    def venvs(
        self,
        upgrade: bool = False,
        quiet: bool = True,
        rm: bool = False,
    ):
        """Installs venv for all python versions in :data:`PYTHON_VERSIONS`."""
        global NODEPS_QUIET  # noqa: PLW0603
        NODEPS_QUIET = quiet

        if self.ci:
            self.venv(upgrade=upgrade, quiet=quiet, rm=rm)
        else:
            for version in PYTHON_VERSIONS:
                self.venv(version=version, upgrade=upgrade, quiet=quiet, rm=rm)

    def write(self, rm: bool = False):
        """Updates pyproject.toml and docs conf.py.

        Args:
            rm: remove cache
        """
        if self.pyproject_toml.file:
            original_project = copy.deepcopy(self.pyproject_toml.config.get("project", {}))
            github = self.gh.github(rm=rm)
            project = {
                "name": github["name"],
                "authors": [
                    {"name": AUTHOR, "email": EMAIL},
                ],
                "description": github.get("description", ""),
                "urls": {"Homepage": github["html_url"], "Documentation": f"https://{self.name}.readthedocs.io"},
                "dynamic": ["version"],
                "license": {"text": "MIT"},
                "readme": "README.md",
                "requires-python": f">={PYTHON_DEFAULT_VERSION}",
            }
            if "project" not in self.pyproject_toml.config:
                self.pyproject_toml.config["project"] = {}
            for key, value in project.items():
                if key not in self.pyproject_toml.config["project"]:
                    self.pyproject_toml.config["project"][key] = value

            self.pyproject_toml.config["project"] = dict_sort(self.pyproject_toml.config["project"])
            if original_project != self.pyproject_toml.config["project"]:
                with self.pyproject_toml.file.open("w") as f:
                    with pipmetapathfinder():
                        import tomlkit
                        tomlkit.dump(self.pyproject_toml.config, f)
                    self.info(f"{self.write.__name__}: {self.pyproject_toml.file}")

            if self.docsdir:
                imp = f"import {NODEPS_PROJECT_NAME}.__main__" if self.name == NODEPS_PROJECT_NAME else ""
                conf = f"""import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
{imp}
project = "{github["name"]}"
author = "{AUTHOR}"
# noinspection PyShadowingBuiltins
copyright = "{datetime.datetime.now().year}, {AUTHOR}"
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.extlinks",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_click",
    "sphinx.ext.intersphinx",
]
autoclass_content = "both"
autodoc_default_options = {{"members": True, "member-order": "bysource",
                           "undoc-members": True, "show-inheritance": True}}
autodoc_typehints = "description"
autosectionlabel_prefix_document = True
html_theme = "furo"
html_title, html_last_updated_fmt = "{self.name} docs", "%Y-%m-%dT%H:%M:%S"
inheritance_alias = {{}}
nitpicky = True
nitpick_ignore = [('py:class', '*')]
toc_object_entries = True
toc_object_entries_show_parents = "all"
pygments_style, pygments_dark_style = "sphinx", "monokai"
extlinks = {{
    "issue": ("https://github.com/{GIT}/{self.name}/issues/%s", "#%s"),
    "pull": ("https://github.com/{GIT}/{self.name}/pull/%s", "PR #%s"),
    "user": ("https://github.com/%s", "@%s"),
}}
intersphinx_mapping = {{
    "python": ("https://docs.python.org/3", None),
    "packaging": ("https://packaging.pypa.io/en/latest", None),
}}
"""  # noqa: DTZ005
                file = self.docsdir / "conf.py"
                original = file.read_text() if file.is_file() else ""
                if original != conf:
                    file.write_text(conf)
                    self.info(f"{self.write.__name__}: {file}")

                requirements = """click
furo >=2023.9.10, <2024
linkify-it-py >=2.0.2, <3
myst-parser >=2.0.0, <3
sphinx >=7.2.6, <8
sphinx-autobuild >=2021.3.14, <2022
sphinx-click >=5.0.1, <6
sphinx_autodoc_typehints
sphinxcontrib-napoleon >=0.7, <1
"""
                file = self.docsdir / "requirements.txt"
                original = file.read_text() if file.is_file() else ""
                if original != requirements:
                    file.write_text(requirements)
                    self.info(f"{self.write.__name__}: {file}")

                reference = f"""# Reference

## {self.name}

```{{eval-rst}}
.. automodule:: {self.name}
   :members:
```
"""
                file = self.docsdir / "reference.md"
                original = file.read_text() if file.is_file() else ""
                if original != reference:
                    file.write_text(reference)
                    self.info(f"{self.write.__name__}: {file}")


class PTHBuildPy(build_py):
    """Build py with pth files installed."""

    def run(self):
        """Run build py."""
        super().run()
        self.outputs = []
        self.outputs = _copy_pths(self, self.build_lib)

    def get_outputs(self, include_bytecode=1):
        """Get outputs."""
        return itertools.chain(build_py.get_outputs(self, 0), self.outputs)


class PTHDevelop(develop):
    """PTH Develop Install."""

    def run(self):
        """Run develop."""
        super().run()
        _copy_pths(self, self.install_dir)


class PTHEasyInstall(easy_install):
    """PTH Easy Install."""

    def run(self, *args, **kwargs):
        """Run easy install."""
        super().run(*args, **kwargs)
        _copy_pths(self, self.install_dir)


class PTHInstallLib(install_lib):
    """PTH Install Library."""

    def run(self):
        """Run Install Library."""
        super().run()
        self.outputs = []
        self.outputs = _copy_pths(self, self.install_dir)

    def get_outputs(self):
        """Get outputs."""
        return itertools.chain(install_lib.get_outputs(self), self.outputs)


class TempDir(tempfile.TemporaryDirectory):
    """Wrapper for :class:`tempfile.TemporaryDirectory` that provides Path-like.

    Examples:
        >>> from nodeps import TempDir
        >>> from nodeps import MACOS
        >>> with TempDir() as tmp:
        ...     if MACOS:
        ...         assert tmp.parts[1] == "var"
        ...         assert tmp.resolve().parts[1] == "private"
    """

    def __enter__(self) -> Path:
        """Return the path of the temporary directory.

        Returns:
            Path of the temporary directory
        """
        return Path(self.name)


def _copy_pths(self: PTHBuildPy | PTHDevelop | PTHEasyInstall | PTHInstallLib, directory: str) -> list[str]:
    log = ColorLogger.logger()
    outputs = []
    data = self.get_outputs() if isinstance(self, (PTHBuildPy | PTHInstallLib)) else self.outputs
    for source in data:
        if source.endswith(".pth"):
            destination = Path(directory, Path(source).name)
            if not destination.is_file() or not filecmp.cmp(source, destination):
                destination = str(destination)
                msg = f"{self.__class__.__name__}: {str(Path(sys.executable).resolve())[-4:]}"
                log.info(
                    msg,
                    extra={"extra": f"{source} -> {destination}"},
                )
                self.copy_file(source, destination)
                outputs.append(destination)
    return outputs


def _pip_base_command(self: Command, args: list[str]) -> int:
    """Post install pip patch."""
    try:
        log = ColorLogger.logger()
        with self.main_context():
            rv = self._main(args)
            if rv == 0 and self.__class__.__name__ == "InstallCommand":
                for key, value in _NODEPS_PIP_POST_INSTALL.items():
                    p = Project(key)
                    p.completions()
                    p.brew()
                    for file in findfile(NODEPS_PIP_POST_INSTALL_FILENAME, value):
                        log.info(self.__class__.__name__, extra={"extra": f"post install '{key}': {file}"})
                        exec_module_from_file(file)
            return rv
    finally:
        logging.shutdown()


def _pip_install_wheel(
    name: str,
    wheel_path: str,
    scheme: pip._internal.models.scheme.Scheme,
    req_description: str,
    pycompile: bool = True,
    warn_script_location: bool = True,
    direct_url: pip._internal.models.direct_url.DirectUrl | None = None,
    requested: bool = False,
):
    """Pip install wheel patch to post install."""
    with zipfile.ZipFile(wheel_path) as z, pip._internal.operations.install.wheel.req_error_context(req_description):
        pip._internal.operations.install.wheel._install_wheel(
            name=name,
            wheel_zip=z,
            wheel_path=wheel_path,
            scheme=scheme,
            pycompile=pycompile,
            warn_script_location=warn_script_location,
            direct_url=direct_url,
            requested=requested,
        )
        global _NODEPS_PIP_POST_INSTALL  # noqa: PLW0602
        _NODEPS_PIP_POST_INSTALL[name] = Path(scheme.purelib, name)


def _pip_uninstall_req(self, auto_confirm: bool = False, verbose: bool = False):
    """Pip uninstall patch to post install."""
    assert self.req  # noqa: S101
    p = Project(self.req.name)
    p.completions(uninstall=True)

    dist = pip._internal.metadata.get_default_environment().get_distribution(self.req.name)
    if not dist:
        pip._internal.req.req_install.logger.warning("Skipping %s as it is not installed.", self.name)
        return None
    pip._internal.req.req_install.logger.info("Found existing installation: %s", dist)
    uninstalled_pathset = pip._internal.req.req_uninstall.UninstallPathSet.from_dist(dist)
    uninstalled_pathset.remove(auto_confirm, verbose)
    return uninstalled_pathset


def _setuptools_build_quiet(self, importable) -> None:
    """Setuptools build py patch to quiet build."""
    if NODEPS_QUIET:
        return
    if importable not in self._already_warned:
        self._Warning.emit(importable=importable)
        self._already_warned.add(importable)


async def aioclone(
    owner: str | None = None,
    repository: str = NODEPS_PROJECT_NAME,
    path: Path | str | None = None,
) -> Path:
    """Async Clone Repository.

    Examples:
        >>> import asyncio
        >>> from nodeps import TempDir
        >>> from nodeps import aioclone
        >>>
        >>> with TempDir() as tmp:
        ...     directory = tmp / "1" / "2" / "3"
        ...     rv = asyncio.run(aioclone("octocat", "Hello-World", path=directory))
        ...     assert (rv / "README").exists()

    Args:
        owner: github owner, None to use GIT or USER environment variable if not defined (Default: `GIT`)
        repository: github repository (Default: `PROJECT`)
        path: path to clone (Default: `repo`)

    Returns:
        Path of cloned repository
    """
    path = path or Path.cwd() / repository
    path = Path(path)
    if not path.exists():
        if not path.parent.exists():
            path.parent.mkdir()
        await aiocmd("git", "clone", GitUrl(owner, repository).url, path)
    return path


def clone(
    owner: str | None = None,
    repository: str = NODEPS_PROJECT_NAME,
    path: Path | str = None,
) -> Path:
    """Clone Repository.

    Examples:
        >>> import os
        >>> from nodeps import TempDir
        >>> from nodeps import clone
        >>>
        >>> with TempDir() as tmp:
        ...     directory = tmp / "1" / "2" / "3"
        >>> if not os.environ.get("CI"):
        ...     rv = clone("octocat", "Hello-World", directory)
        ...     assert (rv / "README").exists()

    Args:
        owner: github owner, None to use GIT or USER environment variable if not defined (Default: `GIT`)
        repository: github repository (Default: `PROJECT`)
        path: path to clone (Default: `repo`)

    Returns:
        CompletedProcess
    """
    path = path or Path.cwd() / repository
    path = Path(path)
    if not path.exists():
        if not path.parent.exists():
            path.parent.mkdir()
        cmd("git", "clone", GitUrl(owner, repository).url, path)
    return path


def completions(name: str, install: bool = True, uninstall: bool = False) -> str | None:
    """Generate completions for command.

    Args:
        name: command name
        install: install completions to /usr/local/etc/bash_completion.d/ or /etc/bash_completion.d
        uninstall: uninstall completions

    Returns:
        Path to file if installed or prints if not installed
    """
    completion = f"""# shellcheck shell=bash

#
# generated by {__file__}

#######################################
# {name} completion
# Globals:
#   COMPREPLY
#   COMP_CWORD
#   COMP_WORDS
# Arguments:
#   1
# Returns:
#   0 ...
#######################################
_{name}_completion() {{
    local IFS=$'
'
  mapfile -t COMPREPLY < <(env COMP_WORDS="${{COMP_WORDS[*]}}" \\
    COMP_CWORD="${{COMP_CWORD}}" \\
    _{name.upper()}_COMPLETE=complete_bash "$1")
  return 0
}}

complete -o default -F _{name}_completion {name}
"""
    path = Path("/usr/local/etc/bash_completion.d" if MACOS else "/etc/bash_completion.d").mkdir()
    file = Path(path, f"{NODEPS_PROJECT_NAME}:{name}.bash")
    if uninstall:
        file.unlink(missing_ok=True)
        return None
    if install:
        if not file.is_file() or (file.read_text() != completion):
            file.write_text(completion)
            return str(file)
        return None
    print(completion)
    return None

def envbash(
    path: AnyPath = ".env",
    fixups: Iterable | None = None,
    into: Mapping | None = None,
    missing_ok: bool = False,
    new: bool = False,
    override: bool = True,
) -> EnvironOS | dict[str, str]:
    """Source ``path`` or ``path``relative to cwd upwards and return the resulting environment as a dictionary.

    Args:
        path: bash file to source or name relative to cwd upwards.
        fixups: remove from new environment if they are not in os.environ or get from os.environ instead of new env.
        into: if override updated into (Default: None for os.environ).
        missing_ok: do not raise exception if file ot found.
        new: return only vars in file.
        override: override

    Raises:
        FileNotFoundError.

    Return:
        Dict.
    """
    p = Path(path)
    p = p.find_up()
    if p is None:
        if missing_ok:
            return None
        msg = f"{path=}"
        raise FileNotFoundError(msg)

    rv = stdout(f'set -a; . {p} > /dev/null; python -c "import os; print(repr(dict(os.environ)))"')

    if not rv:
        msg = f"source {path=}"
        raise ValueError(msg)

    fixups = fixups or ["_", "OLDPWD", "PWD", "SHLVL"]

    if new:
        return {k: v for k, v in ast.literal_eval(rv).items() if k not in os.environ and k not in fixups}

    new = {}
    for k, v in ast.literal_eval(rv).items():
        if not k.startswith("BASH_FUNC_"):
            if k in fixups and k in os.environ:
                new[k] = os.environ[k]
            elif k not in fixups:
                new[k] = v

    if override:
        into = os.environ if into is None else into
        into.update(new)
        return into
    return new


def exec_module_from_file(file: Path | str, name: str | None = None) -> types.ModuleType:
    """Executes module from file location.

    Examples:
        >>> import nodeps
        >>> from nodeps import exec_module_from_file
        >>> m = exec_module_from_file(nodeps.__file__)
        >>> assert m.__name__ == nodeps.__name__

    Args:
        file: file location
        name: module name (default from file)

    Returns:
        Module instance
    """
    file = Path(file)
    spec = importlib.util.spec_from_file_location(
        name or file.parent.name if file.name == "__init__.py" else file.stem, file
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def filterm(
    d: MutableMapping[_KT, _VT], k: Callable[..., bool] = lambda x: True, v: Callable[..., bool] = lambda x: True
) -> MutableMapping[_KT, _VT]:
    """Filter Mutable Mapping.

    Examples:
        >>> from nodeps import filterm
        >>>
        >>> assert filterm({'d':1}) == {'d': 1}
        >>> # noinspection PyUnresolvedReferences
        >>> assert filterm({'d':1}, lambda x: x.startswith('_')) == {}
        >>> # noinspection PyUnresolvedReferences
        >>> assert filterm({'d': 1, '_a': 2}, lambda x: x.startswith('_'), lambda x: isinstance(x, int)) == {'_a': 2}

    Returns:
        Filtered dict with
    """
    # noinspection PyArgumentList
    return d.__class__({x: y for x, y in d.items() if k(x) and v(y)})


def findfile(pattern, path: StrOrBytesPath = None) -> list[Path]:
    """Find file with pattern.

    Examples:
        >>> from pathlib import Path
        >>> import nodeps
        >>> from nodeps import findfile
        >>>
        >>> assert Path(nodeps.__file__) in findfile("*.py")

    Args:
        pattern: pattern to search files
        path: default cwd

    Returns:
        list of files found
    """
    result = []
    for root, _, files in os.walk(path or Path.cwd()):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(Path(root, name))
    return result


def findup(
    path: StrOrBytesPath = None,
    kind: Literal["exists", "is_dir", "is_file"] = "is_file",
    name: str | Path = ".env",
    uppermost: bool = False,
) -> Path | None:
    """Find up if name exists or is file or directory.

    Examples:
        >>> import email
        >>> import email.mime
        >>> from pathlib import Path
        >>> import nodeps
        >>> from nodeps import chdir, findup, parent
        >>>
        >>>
        >>> file = Path(email.mime.__file__)
        >>>
        >>> with chdir(parent(nodeps.__file__)):
        ...     pyproject_toml = findup(nodeps.__file__, name="pyproject.toml")
        ...     assert pyproject_toml.is_file()
        >>>
        >>> with chdir(parent(email.mime.__file__)):
        ...     email_mime_py = findup(name="__init__.py")
        ...     assert email_mime_py.is_file()
        ...     assert email_mime_py == Path(email.mime.__file__)
        ...     email_py = findup(name="__init__.py", uppermost=True)
        ...     assert email_py.is_file()
        ...     assert email_py == Path(email.__file__)
        >>>
        >>> assert findup(kind="is_dir", name=nodeps.__name__) == Path(nodeps.__name__).parent.resolve()
        >>>
        >>> assert findup(file, kind="exists", name="__init__.py") == file.parent / "__init__.py"
        >>> assert findup(file, name="__init__.py") == file.parent / "__init__.py"
        >>> assert findup(file, name="__init__.py", uppermost=True) == file.parent.parent / "__init__.py"

    Args:
        path: CWD if None or Path.
        kind: Exists, file or directory.
        name: File or directory name.
        uppermost: Find uppermost found if True (return the latest found if more than one) or first if False.

    Returns:
        Path if found.
    """
    name = name.name if isinstance(name, Path) else name
    start = parent(path or Path.cwd())
    latest = None
    while True:
        if getattr(find := start / name, kind)():
            if not uppermost:
                return find
            latest = find
        if (start := start.parent) == Path("/"):
            return latest


def firstfound(data: Iterable, apply: Callable) -> Any:
    """Returns first value in data if apply is True.

    Examples:
        >>> from nodeps import firstfound
        >>>
        >>> assert firstfound([1, 2, 3], lambda x: x == 2) == 2
        >>> assert firstfound([1, 2, 3], lambda x: x == 4) is None

    Args:
        data: iterable.
        apply: function to apply.

    Returns:
        Value if found.
    """
    for i in data:
        if apply(i):
            return i
    return None


def flatten(
    data: tuple | list | set,
    recurse: bool = False,
    unique: bool = False,
    sort: bool = True,
) -> tuple | list | set:
    """Flattens an Iterable.

    Examples:
        >>> from nodeps import flatten
        >>>
        >>> assert flatten([1, 2, 3, [1, 5, 7, [2, 4, 1, ], 7, 6, ]]) == [1, 2, 3, 1, 5, 7, [2, 4, 1], 7, 6]
        >>> assert flatten([1, 2, 3, [1, 5, 7, [2, 4, 1, ], 7, 6, ]], recurse=True) == [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 7]
        >>> assert flatten((1, 2, 3, [1, 5, 7, [2, 4, 1, ], 7, 6, ]), unique=True) == (1, 2, 3, 4, 5, 6, 7)

    Args:
        data: iterable
        recurse: recurse
        unique: when recurse
        sort: sort

    Returns:
        Union[list, Iterable]:
    """
    if unique:
        recurse = True

    cls = data.__class__

    flat = []
    _ = [
        flat.extend(flatten(item, recurse, unique) if recurse else item)
        if isinstance(item, list)
        else flat.append(item)
        for item in data
        if item
    ]
    value = set(flat) if unique else flat
    if sort:
        try:
            value = cls(sorted(value))
        except TypeError:
            value = cls(value)
    return value


def framesimple(data: inspect.FrameInfo | types.FrameType | types.TracebackType) -> FrameSimple | None:
    """Returns :class:`nodeps.FrameSimple`.

    Examples:
        >>> import inspect
        >>> from nodeps import Path
        >>> from nodeps import framesimple
        >>>
        >>> frameinfo = inspect.stack()[0]
        >>> finfo = framesimple(frameinfo)
        >>> ftype = framesimple(frameinfo.frame)
        >>> assert frameinfo.frame.f_code == finfo.code
        >>> assert frameinfo.frame == finfo.frame
        >>> assert frameinfo.filename == str(finfo.path)
        >>> assert frameinfo.lineno == finfo.lineno

    Returns:
        :class:`FrameSimple`.
    """
    if isinstance(data, inspect.FrameInfo):
        frame = data.frame
        back = frame.f_back
        lineno = data.lineno
    elif isinstance(data, types.FrameType):
        frame = data
        back = data.f_back
        lineno = data.f_lineno
    elif isinstance(data, types.TracebackType):
        frame = data.tb_frame
        back = data.tb_next
        lineno = data.tb_lineno
    else:
        return None

    code = frame.f_code
    f_globals = frame.f_globals
    f_locals = frame.f_locals
    function = code.co_name
    v = f_globals | f_locals
    name = v.get("__name__") or function
    return FrameSimple(
        back=back,
        code=code,
        frame=frame,
        function=function,
        globals=f_globals,
        lineno=lineno,
        locals=f_locals,
        name=name,
        package=v.get("__package__") or name.split(".")[0],
        path=sourcepath(data),
        vars=v,
    )


def from_latin9(*args) -> str:
    """Converts string from latin9 hex.

    Examples:
        >>> from nodeps import from_latin9
        >>>
        >>> from_latin9("f1")
        'ñ'
        >>>
        >>> from_latin9("4a6f73e920416e746f6e696f205075e972746f6c6173204d6f6e7461f1e973")
        'José Antonio Puértolas Montañés'
        >>>
        >>> from_latin9("f1", "6f")
        'ño'

    Args:
        args: strings to convert to latin9

    Returns:
        str
    """
    rv = ""
    if len(args) == 1:
        pairs = split_pairs(args[0])
        for pair in pairs:
            rv += bytes.fromhex("".join(pair)).decode("latin9")
    else:
        for char in args:
            rv += bytes.fromhex(char).decode("latin9")
    return rv


def fromiter(data, *args):
    """Gets attributes from Iterable of objects and returns dict with.

    Examples:
        >>> from types import SimpleNamespace as Simple
        >>> from nodeps import fromiter
        >>>
        >>> assert fromiter([Simple(a=1), Simple(b=1), Simple(a=2)], 'a', 'b', 'c') == {'a': [1, 2], 'b': [1]}
        >>> assert fromiter([Simple(a=1), Simple(b=1), Simple(a=2)], ('a', 'b', ), 'c') == {'a': [1, 2], 'b': [1]}
        >>> assert fromiter([Simple(a=1), Simple(b=1), Simple(a=2)], 'a b c') == {'a': [1, 2], 'b': [1]}

    Args:
        data: object.
        *args: attributes.

    Returns:
        Tuple
    """
    value = {k: [getattr(C, k) for C in data if hasattr(C, k)] for i in args for k in toiter(i)}
    return {k: v for k, v in value.items() if v}


def getpths() -> dict[str, Path] | None:
    """Get list of pths under ``sitedir``.

    Examples:
        >>> from nodeps import getpths
        >>>
        >>> pths = getpths()
        >>> assert "distutils-precedence" in pths

    Returns:
        Dictionary with pth name and file
    """
    try:
        s = getsitedir()
        names = os.listdir(s)
    except OSError:
        return None
    return {re.sub("(-[0-9].*|.pth)", "", name): Path(s / name) for name in names if name.endswith(".pth")}


def getsitedir(index: bool = 2) -> Path:
    """Get site directory from stack if imported by :mod:`site` in a ``.pth`` file or :mod:`sysconfig`.

    Examples:
        >>> from nodeps import getsitedir
        >>> assert "packages" in str(getsitedir())

    Args:
        index: 1 if directly needed by this function (default: 2), for caller to this function

    Returns:
        Path instance with site directory
    """
    if (s := sys._getframe(index).f_locals.get("sitedir")) is None:
        s = sysconfig.get_paths()["purelib"]
    return Path(s)


def group_user(name: int | str = USER) -> GroupUser:
    """Group and User for Name (id if name is str and vice versa).

    Examples:
        >>> import os
        >>> import pathlib
        >>>
        >>> from nodeps import group_user
        >>> from nodeps import PW_USER, PW_ROOT
        >>>
        >>> s = pathlib.Path().stat()
        >>> gr = group_user()
        >>> assert gr.group == s.st_gid and gr.user == s.st_uid
        >>> gr = group_user(name=PW_USER.pw_uid)
        >>> actual_gname = gr.group
        >>> assert gr.group != PW_ROOT.pw_name and gr.user == PW_USER.pw_name
        >>> gr = group_user('root')
        >>> assert gr.group != s.st_gid and gr.user == 0
        >>> gr = group_user(name=0)
        >>> assert gr.group != actual_gname and gr.user == 'root'

    Args:
        name: usename or id (default: `data.ACTUAL.pw_name`)

    Returns:
        GroupUser.
    """
    if isinstance(name, str):
        struct = (
            struct
            if name  # noqa: PLR1714
            == (struct := PW_USER).pw_name
            or name == (struct := PW_ROOT).pw_name
            else pwd.getpwnam(name)
        )
        return GroupUser(group=struct.pw_gid, user=struct.pw_uid)
    struct = (
        struct
        if (
            name  # noqa: PLR1714
            == (struct := PW_USER).pw_uid
            or name == (struct := PW_ROOT).pw_uid
        )
        else pwd.getpwuid(name)
    )
    return GroupUser(group=grp.getgrgid(struct.pw_gid).gr_name, user=struct.pw_name)


def ins(obj: Any, *, _console: Console | None = None, title: str | None = None, _help: bool = False,
        methods: bool = True, docs: bool = False, private: bool = True,
        dunder: bool = False, sort: bool = True, _all: bool = False, value: bool = True, ):
    """Wrapper :func:`rich.inspect` for :class:`rich._inspect.Inspect`.

    Changing defaults to: ``docs=False, methods=True, private=True``.

    Inspect any Python object.

    Examples:
        >>> from nodeps import ins
        >>>
        >>> # to see summarized info.
        >>> ins(ins)  # doctest: +SKIP
        >>> # to not see methods.
        >>> ins(ins, methods=False)  # doctest: +SKIP
        >>> # to see full (non-abbreviated) help.
        >>> ins(ins, help=True)  # doctest: +SKIP
        >>> # to not see private attributes (single underscore).
        >>> ins(ins, private=False)  # doctest: +SKIP
        >>> # to see attributes beginning with double underscore.
        >>> ins(ins, dunder=True)  # doctest: +SKIP
        >>> # to see all attributes.
        >>> ins(ins, _all=True)  # doctest: +SKIP
        '

    Args:
        obj (Any): An object to inspect.
        _console (Console, optional): Rich Console.
        title (str, optional): Title to display over inspect result, or None use type. Defaults to None.
        _help (bool, optional): Show full help text rather than just first paragraph. Defaults to False.
        methods (bool, optional): Enable inspection of callables. Defaults to False.
        docs (bool, optional): Also render doc strings. Defaults to True.
        private (bool, optional): Show private attributes (beginning with underscore). Defaults to False.
        dunder (bool, optional): Show attributes starting with double underscore. Defaults to False.
        sort (bool, optional): Sort attributes alphabetically. Defaults to True.
        _all (bool, optional): Show all attributes. Defaults to False.
        value (bool, optional): Pretty print value. Defaults to True.
    """
    rich.inspect(obj=obj, console=_console or CONSOLE, title=title, help=_help, methods=methods, docs=docs,
                 private=private, dunder=dunder, sort=sort, all=_all, value=value)


def is_idlelib() -> bool:
    """Is idle repl."""
    return hasattr(sys.stdin, "__module__") and sys.stdin.__module__.startswith("idlelib")


def is_repl(syspath: bool = False) -> bool:
    """Check if it is a repl.

    Args:
        syspath: set sys.path with cwd and cwd/src
    """
    rv = any([hasattr(sys, 'ps1'), 'pythonconsole' in sys.stdout.__class__.__module__, is_idlelib()])
    if rv and syspath:
        cwd = Path.cwd()
        cwd.sys()
        (cwd / "src").sys()
    return rv


def is_terminal(self: Console | OpenIO | None = None) -> bool:
    """Patch for rich console is terminal.

    Examples:
        >>> import time
        >>> from rich.console import Console
        >>> from rich.json import JSON
        >>> from rich import print_json
        >>>
        >>> c = Console()
        >>> with c.status("Working...", spinner="material"):  # doctest: +SKIP
        ...    time.sleep(2)
        >>>
        >>> c.log(JSON('["foo", "bar"]'))  # doctest: +SKIP
        >>>
        >>> print_json('["foo", "bar"]')  # doctest: +SKIP
        >>>
        >>> c.log("Hello, World!")  # doctest: +SKIP
        >>> c.print([1, 2, 3])  # doctest: +SKIP
        >>> c.print("[blue underline]Looks like a link")  # doctest: +SKIP
        >>> c.print(locals())  # doctest: +SKIP
        >>> c.print("FOO", style="white on blue")  # doctest: +SKIP
        >>>
        >>> blue_console = Console(style="white on blue")  # doctest: +SKIP
        >>> blue_console.print("I'm blue. Da ba dee da ba di.")  # doctest: +SKIP
        >>>
        >>> c.input("What is [i]your[/i] [bold red]name[/]? :smiley: ")  # doctest: +SKIP

    References:
        Test with: `print("[italic red]Hello[/italic red] World!", locals())`

        `Rich Inspect <https://rich.readthedocs.io/en/stable/traceback.html?highlight=sitecustomize>`_

        ``rich.traceback.install(suppress=[click])``

        To see the spinners: `python -m rich.spinner`
        To print json from the comamand line: `python -m rich.json cats.json`

        `Rich Console <https://rich.readthedocs.io/en/stable/console.html>`_

        Input: `console.input("What is [i]your[/i] [bold red]name[/]? :smiley: ")`
    """
    if hasattr(self, "_force_terminal") and self._force_terminal is not None:
        return self._force_terminal

    if is_idlelib():
        return False

    if hasattr(self, "is_jupyter") and self.is_jupyter:
        return False

    if hasattr(self, "_force_terminal") and self._environ.get("FORCE_COLOR"):
        self._force_terminal = True
        return True

    try:
        return any([is_repl(), hasattr(self, "isatty") and self.isatty(),
                    hasattr(self, "file") and hasattr(self.file, "isatty") and self.file.isatty()])
    except ValueError:
        return False


def iscoro(data: Any) -> bool:
    """Is coro?."""
    return any(
        [
            inspect.isasyncgen(data),
            inspect.isasyncgenfunction(data),
            asyncio.iscoroutine(data),
            inspect.iscoroutinefunction(data),
        ]
    )


def load_ipython_extension1(  # noqa: PLR0912, PLR0915
    ipython: InteractiveShell | None = None, magic: bool = False
) -> Config | None:
    """IPython extension.

    We are entering twice at startup: from $PYTHONSTARTUP and ipython is None
        and from $IPYTHONDIR to load nodeps extension.

    The `ipython` argument is the currently active `InteractiveShell`
    instance, which can be used in any way. This allows you to register
    new magics or aliases, for example.

    https://ipython.readthedocs.io/en/stable/config/extensions/index.html

    Before extension is loaded:
        - almost no globals
        - and only nodeps in sys.modules
    """
    if ipython is None:
        with contextlib.suppress(NameError):
            ipython: InteractiveShell = get_ipython()  # type: ignore[attr-defined]  # noqa: F821

    from_pycharm_console = "ipython-input" in sys._getframe(1).f_code.co_filename

    if magic and ipython:
        ipython.run_line_magic("reload_ext", NODEPS_PROJECT_NAME)
        return None

    if ipython:
        config = ipython.config
        ipython.prompts = MyPrompt(ipython)
        loaded = ipython.extension_manager.loaded
        if NODEPS_PROJECT_NAME not in loaded:
            extensions = [item.removeprefix("IPython.extensions.") for item in loaded]
            for extension in IPYTHON_EXTENSIONS:
                if extension not in extensions and extension != NODEPS_PROJECT_NAME:
                    ipython.extension_manager.load_extension(extension)
                    # print(extension)
                    # ipython.run_line_magic("load_ext", extension)

            from IPython.core.magic import Magics, line_magic, magics_class

            @magics_class
            class NodepsMagic(Magics):
                """Nodeps magic class."""

                @line_magic
                def nodeps(self, _):
                    """Nodeps magic."""
                    self.shell.run_line_magic("reload_ext", NODEPS_PROJECT_NAME)
                    self.shell.run_line_magic("autoreload", "3")
                    self.shell.run_code(f"import {NODEPS_PROJECT_NAME}")
                    self.shell.run_code(f"print({NODEPS_PROJECT_NAME})")

            ipython.register_magics(NodepsMagic)

        if NODEPS_PROJECT_NAME not in sys.modules:
            imported = importlib.import_module(NODEPS_PROJECT_NAME)
        module = None
        if env := os.environ.get("VIRTUAL_ENV"):
            module = Path(env).parent.name
            ipython.ex(f"from {module} import *")

        ipython.ex("'%autoreload 2'")
        ipython.extension_manager.shell.run_line_magic("autoreload", "3")
        if module != NODEPS_PROJECT_NAME:
            ipython.ex(f"import {NODEPS_PROJECT_NAME}")
        # rich.pretty.install(CONSOLE, expand_all=True)
        warnings.filterwarnings("ignore", ".*To exit:.*", UserWarning)
    else:
        try:
            config = get_config()  # type: ignore[attr-defined]
        except NameError:
            from traitlets.config import Config

            config = Config()

        config.TerminalIPythonApp.extensions = IPYTHON_EXTENSIONS

    config.InteractiveShellApp.exec_lines = ["%autoreload 3", f"import {NODEPS_PROJECT_NAME}"]
    config.BaseIPythonApplication.verbose_crash = True
    config.TerminalIPythonApp.display_banner = False
    config.TerminalIPythonApp.exec_PYTHONSTARTUP = True
    config.InteractiveShell.automagic = True
    config.InteractiveShell.banner1 = ""
    config.InteractiveShell.banner2 = ""
    config.InteractiveShell.sphinxify_docstring = True
    config.TerminalInteractiveShell.auto_match = True
    config.TerminalInteractiveShell.autoformatter = "black"
    config.TerminalInteractiveShell.banner1 = ""
    config.TerminalInteractiveShell.banner2 = ""
    config.TerminalInteractiveShell.confirm_exit = False
    config.TerminalInteractiveShell.highlighting_style = "monokai"
    if not from_pycharm_console and not magic:  # debug in console goes thu Prompt
        config.TerminalInteractiveShell.prompts_class = MyPrompt
    config.TerminalInteractiveShell.term_title = True
    config.PlainTextFormatter.max_seq_length = 0
    config.Completer.auto_close_dict_keys = True
    config.StoreMagics.autorestore = True
    config.InteractiveShell.color_info = True
    config.InteractiveShell.colors = "Linux"
    config.TerminalInteractiveShell.true_color = True

    if from_pycharm_console:
        load_ipython_extension(ipython, magic=True)

    import asyncio.base_events
    asyncio.base_events.BaseEventLoop.slow_callback_duration = 1

    if ipython is None:
        return config
    return None


def map_with_args(
    data: Any, func: Callable, /, *args, pred: Callable = lambda x: bool(x), split: str = " ", **kwargs
) -> list:
    """Apply pred/filter to data and map with args and kwargs.

    Examples:
        >>> from nodeps import map_with_args
        >>>
        >>> # noinspection PyUnresolvedReferences
        >>> def f(i, *ar, **kw):
        ...     return f'{i}: {[a(i) for a in ar]}, {", ".join([f"{k}: {v(i)}" for k, v in kw.items()])}'
        >>> map_with_args('0.1.2', f, int, list, pred=lambda x: x != '0', split='.', int=int, str=str)
        ["1: [1, ['1']], int: 1, str: 1", "2: [2, ['2']], int: 2, str: 2"]

    Args:
        data: data.
        func: final function to map.
        *args: args to final map function.
        pred: pred to filter data before map.
        split: split for data str.
        **kwargs: kwargs to final map function.

    Returns:
        List with results.
    """
    return [func(item, *args, **kwargs) for item in yield_if(data, pred=pred, split=split)]


def mip() -> str | None:
    """My Public IP.

    Examples:
        >>> from nodeps import mip
        >>>
        >>> mip()  # doctest: +ELLIPSIS
        '...............'
    """
    return urllib.request.urlopen("https://checkip.amazonaws.com", timeout=2).read().strip().decode()  # noqa: S310

def parse_str(  # noqa: PLR0911
    data: Any | None = None,
) -> bool | GitUrl | Path | ParseResult | IPv4Address | IPv6Address | int | str | None:
    """Parses str or data.__str__().

    Parses:
        - bool: 1, 0, True, False, yes, no, on, off (case insensitive)
        - int: integer only numeric characters but 1 and 0
        - ipaddress: ipv4/ipv6 address
        - url: if "://" or "@" is found it will be parsed as url
        - path: if "." or start with "/" or "~" or "." and does contain ":"
        - others as string

    Arguments:
        data: variable name to parse from environment (default: USER)

    Examples:
        >>> from nodeps import Path
        >>> from nodeps import parse_str
        >>>
        >>> assert parse_str() is None
        >>>
        >>> assert parse_str("1") is True
        >>> assert parse_str("0") is False
        >>> assert parse_str("TrUe") is True
        >>> assert parse_str("OFF") is False
        >>>
        >>> u = "https://github.com/user/repo"
        >>> assert parse_str(u).url == u
        >>> u = "git@github.com:user/repo"
        >>> assert parse_str(u).url == u
        >>> u = "https://github.com"
        >>> assert parse_str(u).geturl() == u
        >>> u = "git@github.com"
        >>> assert parse_str(u).geturl() == u
        >>>
        >>> assert parse_str("~/foo") == Path('~/foo')
        >>> assert parse_str("/foo") == Path('/foo')
        >>> assert parse_str("./foo") == Path('foo')
        >>> assert parse_str(".") == Path('.')
        >>> assert parse_str(Path()) == Path()
        >>>
        >>> assert parse_str("0.0.0.0").exploded == "0.0.0.0"
        >>> assert parse_str("::1").exploded.endswith(":0001")
        >>>
        >>> assert parse_str("2") == 2
        >>> assert parse_str("2.0") == "2.0"
        >>> assert parse_str("/usr/share/man:") == "/usr/share/man:"
        >>> if not os.environ.get("CI"):
        ...     assert isinstance(parse_str(os.environ.get("PATH")), str)

    Returns:
        None
    """
    if data is not None:
        if not isinstance(data, str):
            data = str(data)

        if data.lower() in ["1", "true", "yes", "on"]:
            return True
        if data.lower() in ["0", "false", "no", "off"]:
            return False
        if "://" in data or "@" in data:
            return p if (p := GitUrl(data)).valid else urllib.parse.urlparse(data)
        if (
            (
                data and data[0] in ["/", "~"] or (len(data) >= 2 and f"{data[0]}{data[1]}" == "./")  # noqa: PLR2004
            )
            and ":" not in data
        ) or data == ".":
            return Path(data)
        try:
            return ipaddress.ip_address(data)
        except ValueError:
            if data.isnumeric():
                return int(data)
    return data


def returncode(c: str | list[str], shell: bool = True) -> int:
    """Runs command in shell and returns returncode showing stdout and stderr.

    No exception is raised

    Examples:
        >>> from nodeps import returncode
        >>>
        >>> assert returncode("ls /bin/ls") == 0
        >>> assert returncode("ls foo") == 1

    Arguments:
        c: command to run
        shell: run in shell (default: True)

    Returns:
        return code

    """
    return subprocess.call(c, shell=shell)


def sourcepath(data: Any) -> Path:
    """Get path of object.

    Examples:
        >>> import asyncio
        >>> import nodeps
        >>> from nodeps import Path
        >>> from nodeps import sourcepath
        >>>
        >>> finfo = inspect.stack()[0]
        >>> globs_locs = (finfo.frame.f_globals | finfo.frame.f_locals).copy()
        >>> assert sourcepath(sourcepath) == Path(nodeps.__file__)
        >>> assert sourcepath(asyncio.__file__) == Path(asyncio.__file__)
        >>> assert sourcepath(dict(a=1)) == Path("{'a': 1}")

    Returns:
        Path.
    """
    if isinstance(data, MutableMapping):
        f = data.get("__file__")
    elif isinstance(data, inspect.FrameInfo):
        f = data.filename
    else:
        try:
            f = inspect.getsourcefile(data) or inspect.getfile(data)
        except TypeError:
            f = None
    return Path(f or str(data))


def siteimported() -> str | None:
    """True if imported by :mod:`site` in a ``.pth`` file."""
    s = None
    _frame = sys._getframe()
    while _frame and (s := _frame.f_locals.get("sitedir")) is None:
        _frame = _frame.f_back
    return s


def split_pairs(text):
    """Split text in pairs for even length.

    Examples:
        >>> from nodeps import split_pairs
        >>>
        >>> split_pairs("123456")
        [('1', '2'), ('3', '4'), ('5', '6')]

    Args:
        text: text to split in pairs

    Returns:
        text
    """
    return list(zip(text[0::2], text[1::2], strict=True))


def stdout(
        shell: AnyStr,
        keepends: bool = False,
        split: bool = False,
        cwd: Path | str | None = None
) -> list[str] | str | None:
    """Return stdout of executing cmd in a shell or None if error.

    Execute the string 'cmd' in a shell with 'subprocess.getstatusoutput' and
    return a stdout if success. The locale encoding is used
    to decode the output and process newlines.

    A trailing newline is stripped from the output.

    Examples:
        >>> from nodeps import stdout
        >>>
        >>> stdout("ls /bin/ls")
        '/bin/ls'
        >>> stdout("true")
        ''
        >>> stdout("ls foo")
        >>> stdout("ls /bin/ls", split=True)
        ['/bin/ls']

    Args:
        shell: command to be executed
        keepends: line breaks when ``split`` if true, are not included in the resulting list unless keepends
            is given and true.
        split: return a list of the stdout lines in the string, breaking at line boundaries.(default: False)
        cwd: cwd

    Returns:
        Stdout or None if error.
    """
    with Path(cwd or "").cd():
        exitcode, data = subprocess.getstatusoutput(shell)

    if exitcode == 0:
        if split:
            return data.splitlines(keepends=keepends)
        return data
    return None


@contextlib.contextmanager
def stdquiet() -> tuple[TextIO, TextIO]:
    """Redirect stdout/stderr to StringIO objects to prevent console output from distutils commands.

    Returns:
        Stdout, Stderr
    """
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    new_stdout = sys.stdout = io.StringIO()
    new_stderr = sys.stderr = io.StringIO()
    try:
        yield new_stdout, new_stderr
    finally:
        new_stdout.seek(0)
        new_stderr.seek(0)
        sys.stdout = old_stdout
        sys.stderr = old_stderr


def suppress(
    func: Callable[P, T],
    *args: P.args,
    exception: ExcType | None = Exception,
    **kwargs: P.kwargs,
) -> T:
    """Try and supress exception.

    Args:
        func: function to call
        *args: args to pass to func
        exception: exception to suppress (default: Exception)
        **kwargs: kwargs to pass to func

    Returns:
        result of func
    """
    with contextlib.suppress(exception or Exception):
        return func(*args, **kwargs)


def syssudo(user: str = "root") -> subprocess.CompletedProcess | None:
    """Rerun Program with sudo ``sys.executable`` and ``sys.argv`` if user is different that the current user.

    Arguments:
        user: run as user (Default: False)

    Returns:
        CompletedProcess if the current user is not the same as user, None otherwise
    """
    if not ami(user):
        return cmd(["sudo", "-u", user, sys.executable, *sys.argv])
    return None



def timestamp_now(file: Path | str):
    """Set modified and create date of file to now."""
    now = time.time()
    os.utime(file, (now, now))


def to_camel(text: str, replace: bool = True) -> str:
    """Convert to Camel.

    Examples:
        >>> to_camel("__ignore_attr__")
        'IgnoreAttr'
        >>> to_camel("__ignore_attr__", replace=False)  # doctest: +SKIP
        '__Ignore_Attr__'

    Args:
        text: text to convert.
        replace: remove '_'  (default: True)

    Returns:
        Camel text.
    """
    rv = "".join(map(str.title, toiter(text, split="_")))
    return rv.replace("_", "") if replace else rv


def to_latin9(chars: str) -> str:
    """Converts string to latin9 hex.

    Examples:
        >>> from nodeps import AUTHOR
        >>> from nodeps import to_latin9
        >>>
        >>> to_latin9("ñ")
        'f1'
        >>>
        >>> to_latin9(AUTHOR)
        '4a6f73e920416e746f6e696f205075e972746f6c6173204d6f6e7461f1e973'

    Args:
        chars: chars to converto to latin9

    Returns:
        hex str
    """
    rv = ""
    for char in chars:
        rv += char.encode("latin9").hex()
    return rv

def tomodules(obj: Any, suffix: bool = True) -> str:
    """Converts Iterable to A.B.C.

    Examples:
        >>> from nodeps import tomodules
        >>> assert tomodules('a b c') == 'a.b.c'
        >>> assert tomodules('a b c.py') == 'a.b.c'
        >>> assert tomodules('a/b/c.py') == 'a.b.c'
        >>> assert tomodules(['a', 'b', 'c.py']) == 'a.b.c'
        >>> assert tomodules('a/b/c.py', suffix=False) == 'a.b.c.py'
        >>> assert tomodules(['a', 'b', 'c.py'], suffix=False) == 'a.b.c.py'

    Args:
        obj: iterable.
        suffix: remove suffix.

    Returns:
        String A.B.C
    """
    split = "/" if isinstance(obj, str) and "/" in obj else " "
    return ".".join(i.removesuffix(Path(i).suffix if suffix else "") for i in toiter(obj, split=split))


def urljson(
    data: str,
    rm: bool = False,
) -> dict:
    """Url open json.

    Examples:
        >>> import os
        >>> from nodeps import urljson
        >>> from nodeps import GIT
        >>> from nodeps import GITHUB_TOKEN
        >>> from nodeps import NODEPS_PROJECT_NAME
        >>>
        >>> if os.environ.get('GITHUB_TOKEN'):
        ...     github = urljson(f"https://api.github.com/repos/{GIT}/{NODEPS_PROJECT_NAME}")
        ...     assert github['name'] == NODEPS_PROJECT_NAME
        >>>
        >>> pypi = urljson(f"https://pypi.org/pypi/{NODEPS_PROJECT_NAME}/json")
        >>> assert pypi['info']['name'] == NODEPS_PROJECT_NAME

    Args:
        data: url
        rm: use pickle cache or remove it before

    Returns:
        dict:
    """
    if not rm and (rv := Path.pickle(name=data)):
        return rv

    if data.lower().startswith("https"):
        request = urllib.request.Request(data)
    else:
        msg = f"Non-HTTPS URL: {data}"
        raise ValueError(msg)
    if "github" in data:
        request.add_header("Authorization", f"token {GITHUB_TOKEN}")

    with urllib.request.urlopen(request) as response:  # noqa: S310
        return Path.pickle(name=data, data=json.loads(response.read().decode()), rm=rm)


def varname(index=2, lower=True, prefix=None, sep="_"):
    """Caller var name.

    Examples:
        >>> from dataclasses import dataclass
        >>> from nodeps import varname
        >>>
        >>> def function() -> str:
        ...     return varname()
        >>>
        >>> class ClassTest:
        ...     def __init__(self):
        ...         self.name = varname()
        ...
        ...     @property
        ...     def prop(self):
        ...         return varname()
        ...
        ...     # noinspection PyMethodMayBeStatic
        ...     def method(self):
        ...         return varname()
        >>>
        >>> @dataclass
        ... class DataClassTest:
        ...     def __post_init__(self):
        ...         self.name = varname()
        >>>
        >>> name = varname(1)
        >>> Function = function()
        >>> classtest = ClassTest()
        >>> method = classtest.method()
        >>> prop = classtest.prop
        >>> dataclasstest = DataClassTest()
        >>>
        >>> def test_var():
        ...     assert name == 'name'
        >>>
        >>> def test_function():
        ...     assert Function == function.__name__.lower()
        >>>
        >>> def test_class():
        ...     assert classtest.name == ClassTest.__name__.lower()
        >>>
        >>> def test_method():
        ...     assert classtest.method() == ClassTest.__name__.lower()
        ...     assert method == 'method'
        >>> def test_property():
        ...     assert classtest.prop == ClassTest.__name__.lower()
        ...     assert prop == 'prop'
        >>> def test_dataclass():
        ...     assert dataclasstest.name == DataClassTest.__name__.lower()

        .. code-block:: python

            class A:

                def __init__(self):

                    self.instance = varname()

            a = A()

            var = varname(1)

    Args:
        index: index.
        lower: lower.
        prefix: prefix to add.
        sep: split.

    Returns:
        Optional[str]: Var name.
    """
    with contextlib.suppress(IndexError, KeyError):
        _stack = inspect.stack()
        f = _stack[index - 1].function
        index = index + 1 if f == "__post_init__" else index
        if (line := textwrap.dedent(_stack[index].code_context[0])) and (
            var := re.sub(f"(.| ){f}.*", "", line.split(" = ")[0].replace("assert ", "").split(" ")[0])
        ):
            return (prefix if prefix else "") + (var.lower() if lower else var).split(sep=sep)[0]
    return None



def yield_if(
    data: Any,
    pred: Callable = lambda x: bool(x),
    split: str = " ",
    apply: Union[Callable, tuple[Callable, ...]] | None = None,  # noqa: UP007
) -> Generator:
    """Yield value if condition is met and apply function if predicate.

    Examples:
        >>> from nodeps import yield_if
        >>>
        >>> assert list(yield_if([True, None])) == [True]
        >>> assert list(yield_if('test1.test2', pred=lambda x: x.endswith('2'), split='.')) == ['test2']
        >>> assert list(yield_if('test1.test2', pred=lambda x: x.endswith('2'), split='.', \
        apply=lambda x: x.removeprefix('test'))) == ['2']
        >>> assert list(yield_if('test1.test2', pred=lambda x: x.endswith('2'), split='.', \
        apply=(lambda x: x.removeprefix('test'), lambda x: int(x)))) == [2]


    Args:
        data: data
        pred: predicate (default: if value)
        split: split char for str.
        apply: functions to apply if predicate is met.

    Returns:
        Yield values if condition is met and apply functions if provided.
    """
    for item in toiter(data, split=split):
        if pred(item):
            if apply:
                for func in toiter(apply):
                    item = func(item)  # noqa: PLW2901
            yield item


def yield_last(data: Any, split: str = " ") -> Iterator[tuple[bool, Any, None]]:
    """Yield value if condition is met and apply function if predicate.

    Examples:
        >>> from nodeps import yield_last
        >>>
        >>> assert list(yield_last([True, None])) == [(False, True, None), (True, None, None)]
        >>> assert list(yield_last('first last')) == [(False, 'first', None), (True, 'last', None)]
        >>> assert list(yield_last('first.last', split='.')) == [(False, 'first', None), (True, 'last', None)]
        >>> assert list(yield_last(dict(first=1, last=2))) == [(False, 'first', 1), (True, 'last', 2)]


    Args:
        data: data.
        split: split char for str.

    Returns:
        Yield value and True when is the last item on iterable
    """
    data = toiter(data, split=split)
    mm = isinstance(data, MutableMapping)
    total = len(data)
    count = 0
    for i in data:
        count += 1
        yield (
            count == total,
            *(
                i,
                data.get(i) if mm else None,
            ),
        )


NOSET = Noset()

if "pip._internal.operations.install.wheel" in sys.modules:
    pip._internal.operations.install.wheel.install_wheel = _pip_install_wheel
    pip._internal.cli.base_command.Command.main = _pip_base_command
    pip._internal.req.req_install.InstallRequirement.uninstall = _pip_uninstall_req

if "rich.console" in sys.modules:
    # noinspection PyPropertyAccess,PyUnboundLocalVariable
    rich.console.Console.is_terminal = property(is_terminal)

if "setuptools.command.build_py" in sys.modules:
    setuptools.command.build_py._IncludePackageDataAbuse.warn = _setuptools_build_quiet

venv.CORE_VENV_DEPS = ["build", "ipython", "pip", "setuptools", "wheel"]
venv.EnvBuilder = EnvBuilder

is_repl(syspath=True)
