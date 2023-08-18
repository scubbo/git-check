Each of these directories can be the base (or can contain multiple bases) to test `list_repos_command`.

To configure the test, each directory should contain a file called `test_configuration.yaml`, containing:

* `scan_dirs`: `List[str]` of the directories that should be scanned
* `expected_paths`: `List[str]` of the paths that should be returned

(All paths defined relative to the containing directory)
