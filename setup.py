from setuptools import setup, find_packages
import os


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


def get_version():
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "git_check", "version.py"
    )
    g = {}
    with open(path) as fp:
        exec(fp.read(), g)
    return g["__version__"]


setup(
    name="git-check",
    version=get_version(),
    description="A tool to help cleanup Git repos",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Jack Jackson",
    license_files=("LICENSE",),
    packages=find_packages(exclude=("tests",)),
    python_requires=">=3.8",
    install_requires=[
        "click>=8.1",
        "dataconf>=2.2.1",
        "setuptools",
        "pip",
    ],
    entry_points="""
        [console_scripts]
        git-check=git_check.cli:cli
    """,
    setup_requires=["pytest-runner"],
    extras_require={
        "test": [
            "pytest>=5.2.2",
            "black==23.7.0",
        ],
        "rich": ["rich"],
    },
    tests_require=["git-check[test]"],
    classifiers=[
    ],
)