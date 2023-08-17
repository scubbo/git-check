from pathlib import Path
from pytest import raises
from unittest.mock import patch

from git_check.config import AppConfig

def test_default_parse(tmp_path: Path):
    with patch('git_check.config.Path.home', lambda: tmp_path):
        conf_dir = tmp_path / ".git-check"
        conf_dir.mkdir()
        conf_path = conf_dir / "config.yaml"
        conf_path.write_text('''
    core:
        scan_dirs:
            - abc
            - def
    ''')
        AppConfig.init(conf_path)
        assert AppConfig.conf.core.scan_dirs == ['abc', 'def']


def test_specific_parse(tmp_path: Path):
    conf_path = tmp_path / "my_cool_config.yaml"
    conf_path.write_text('''
core:
    scan_dirs:
        - ghi
        - jkl
''')
    AppConfig.init(conf_path)
    assert AppConfig.conf.core.scan_dirs == ['ghi', 'jkl']


def test_cannot_access_before_init(tmp_path: Path):
    with patch('git_check.config.Path.home', lambda: tmp_path):
        with raises(Exception) as exc:
            print(AppConfig.conf.core)
        assert exc.value.args[0] == "Must call `AppConfig.init` before accessing values!"


def teardown_function():
    AppConfig.conf = None
    AppConfig.is_inited = False
