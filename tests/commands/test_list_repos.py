from pathlib import Path
from unittest.mock import patch

import pytest
import yaml

from git_check.commands.list_repos import list_repos_command
from git_check.config import AppConfig


def test_trivial_self_test(mock_config):
    project_root = Path(__file__).parent.parent.parent
    mock_config.conf.core.scan_dirs = [str(project_root)]
    repos = list_repos_command()
    assert [repo.path for repo in repos] == [project_root]


# TODO - this can be a bit slow if there are many repos in the directory
# Mark it as such and only run it during "slow" runs
# def test_self_test_from_parent(mock_config):
#     project_root = Path(__file__).parent.parent.parent
#     mock_config.conf.core.scan_dirs = [str(project_root.parent)]
#     repos = list_repos_command()
#     assert project_root in [repo.path for repo in repos]


@pytest.mark.parametrize(
    "test_root",
    [
        test_case
        for test_case in Path(__file__)
        .parent.parent.joinpath("test_filesystems")
        .joinpath("test_list_repos")
        .iterdir()
        if test_case.is_dir()
    ],
)
def test_cases(test_root: Path, mock_config):
    test_configuration = yaml.safe_load(
        test_root.joinpath("test_configuration.yaml").read_text()
    )

    def join_to_test_root(suffix: str) -> Path:
        return test_root.joinpath(suffix).absolute()

    mock_config.conf.core.scan_dirs = [
        str(join_to_test_root(scan_dir)) for scan_dir in test_configuration["scan_dirs"]
    ]
    repos = list_repos_command()
    assert [repo.path for repo in repos] == [
        join_to_test_root(expected_path)
        for expected_path in test_configuration["expected_paths"]
    ]


@pytest.fixture
def mock_config():
    AppConfig.is_inited = True
    with patch("git_check.commands.list_repos.AppConfig") as mock_config:
        mock_config.conf.core.max_scan_depth = 3
        yield mock_config
