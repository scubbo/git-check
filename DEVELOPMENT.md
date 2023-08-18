# Running from local

From [here](https://click.palletsprojects.com/en/8.1.x/setuptools/#testing-the-script):

```
$ source venv/bin/activate
$ pip install -e .
$ git-check [...]
```
# Testing

You cannot just run `pytest`, as that won't have the necessary dependencies installed. Instead, run (having already sourced the venv activation):

```
$ pip install -e ".[test]" # This installs the "optional" dependencies defined in `extras_require` in `setup.py`
$ python3 -m pytest
```