# pytest-gitcov
Extension for pytest to report on the coverage for the lines modified in a given commit or commit range. The vision is to be able to run pytests on a code base before submitting a pull request or code review, to see the lines of code that were modified by you but not covered by unit-tests.

## Issues this plugin is trying to resolve
 - Ideally the whole code base will have reasonable coverage. Realistically though this is rarely the case with a legacy code base. The repository wide coverage report means little in terms of one developers merge request. The hope is that using this plugin you can shine a light on the code you have touched. Making it easier to spot gaps in unit tests due to code you have written, or modified and identify a gap someone else left and should really be filled.
 - Just reporting a list of line ranges covered on the terminal is not much help. I can't remember the line numebers for the functions I've just changed, and working out where the gaps are is time consuming. The HTML report is a lot better for this, but I'd like to have something quick and simple for the terminal.

# Install
Nice and easy:
`pip install pytest-gitcov`

# Usage
This is still in very early stages of development and doesn't really do much yet.

After installing, the plugin is automatically found by pytest. At the moment that means that the plugin always runs with each `pytest` run and you have to uninstall to disable it. Soon there should be an extra argument that can be used to temporarily disable this. For example, respect the existing `pytest-cov` flag (`--no-cov`) as well as a new `--no-gitcov` flag .

There is also a standalone script available to generate a git coverage report on previous `.coverage` DB file, for more info see `git-py-coverage --help`. 
