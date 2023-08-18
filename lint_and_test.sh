set -ex

python3 -m mypy git_check tests
python3 -m black git_check tests
python3 -m pytest .
