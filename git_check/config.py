from dataclasses import dataclass
from pathlib import Path
from typing import List

import dataconf

DEFAULT_CONFIG_FILE_PATH = Path.home().joinpath('.git-check').joinpath('config.yaml')

@dataclass
class CoreConfig:
    # TODO - it'd be nice for this to provide `Path`s - first I'd need to figure out how to
    # tell `dataconf` to parse strings into `Path`s.
    scan_dirs: List[str]

@dataclass
class Config:
    core: CoreConfig

# Metaclass shenanigans to make sure an Exception is thrown if `AppConfig.conf` is accessed before initialization
# https://stackoverflow.com/a/11559173/1040915
# https://stackoverflow.com/a/25607766/1040915
class meta(type):
    def __getattribute__(self, name):
        if not (super().__getattribute__('is_inited') or name == 'init'):
            raise Exception('Must call `AppConfig.init` before accessing values!')
        return super().__getattribute__(name)


class AppConfig(metaclass=meta):
    """
    Usage:

    ```
    import AppConfig
    AppConfig.init(...)

    AppConfig.conf.whatever.key.sequence.you.want
    ```

    This seems like a pretty decent way of providing global availability (see https://stackoverflow.com/questions/6198372/most-pythonic-way-to-provide-global-configuration-variables-in-config-py)
    while also providing IntelliSense/tab-completion and type-safety.
    """
    conf: Config
    is_inited: bool = False

    @classmethod
    def init(cls, config_file_path: Path = None):
        cls.conf = dataconf.file(str((config_file_path or DEFAULT_CONFIG_FILE_PATH).absolute()), Config)
        cls.is_inited = True
