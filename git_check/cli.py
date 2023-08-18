from pathlib import Path
from typing import Optional

import click

from .commands.list_repos import list_repos_command
from .config import AppConfig
from .version import __version__


@click.group()
@click.version_option(version=__version__)
@click.option("--config_path", default=None, type=click.Path())
def cli(config_path: click.Path):
    """
    A tool to help cleanup Git repos
    """
    AppConfig.init(Path(config_path.name) if config_path else None)


@click.command()
def list_repos():
    for repo in list_repos_command():
        click.echo(repo)


cli.add_command(list_repos)
