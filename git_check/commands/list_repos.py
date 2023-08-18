import os
from pathlib import Path

from typing import List

from ..config import AppConfig
from ..types import Repo


def list_repos_command() -> List[Repo]:
    scan_dirs = AppConfig.conf.core.scan_dirs
    max_depth = AppConfig.conf.core.max_scan_depth
    repos = []
    for scan_dir in scan_dirs:
        for root, dirs, _ in os.walk(scan_dir):
            if root[len(scan_dir) :].count(os.sep) < max_depth:
                if ".git" in dirs:
                    repos.append(Repo(Path(root).absolute()))
    return repos
