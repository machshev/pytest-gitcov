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

# The plan
The idea is to print a useful report to the terminal as the last output from pytest, at the end of a test run. This is achevied using a plugin for pytest.

Once the coverage data has been generated with a run of `pytest`. Then it should also be possible to regenerage the report from a stand-alone script (currently `git-py-coverage`). This would use the same coverage data without having to rerun the tests, reporting against either the same commit range or a different commit range.

## Coverage data
When pytest_cov plugin initialises, it creates a coverage object (see the `Coverage` class from the `coverage` package). Pytest allows us to get the pytest_cov plugin object and from that we can access the `coverage.CoverageData` object (https://coverage.readthedocs.io/en/coverage-5.0/api_coveragedata.html#coverage.CoverageData) which is a proxy for SQLite3 DB where the coverage information gathered during the pytest run. This is stored by default in the `.coverage` file in the current working directory - i.e. where you ran pytest from.

We can get access to this coverage data by `coverage.CoverageData` proxy at any point later. Just point it to the relevant `.coverage` DB file, and call the `.read()` method to establish a connection.

Coverage data is available per file as a list of line numbers per file. Although blank lines are not included, only lines that have been executed during the test run. Function signitures, docstrings, blank lines, and comments are not included in coverage line numbers list. However the line number of the first line of the function/method signiture and the line number of the return is available as a tuple pair refered to as an 'arc'.

## Lines modified in a commit
We need two things:
 - list of files modified by the commit range - we can use `git diff --name-status` or `git diff --name-only` to get this.
 - resulting line numbers - for this we can use `git blame` and return the line numbers with the commit hash we are interested in.

It would be nice to be able to get all this information from one command, but can't find one.

## Meaningfull coverage
The line numbers from the coverage plugin are not meaningful on their own... there is no point reporting every blank line or comment that has not been 'executed'. We need to determine if the lines missed are due to branching statements, such as `if` statements, `break` or `continue` in loops, `assert` or `raise` statements that have triggered an exception... and so on.

The easiest way of doing this would be to use the python source parser to inspect the file.

### AST trees
Using `ast.parse` we can get an AST tree of the source file. Iterating over the top level nodes in the module we can identify the line numbers at the start and end of each node (`.lineno` and `.end_lineno`). From this we can see which blocks of code our line numbers are contained in, as well as identify all the branch blocks and code that should have been executed in our tests.

## Report
For the report I'm currently thinking we would show the summary catagorised by file and function name. Command line args could be used to specify the scope of the reporting... just the functions modified, or all the functions in the file modified.

For statements in a function that should have been covered, then give an idea of:
 - scale of miss - line count (or AST node count?), perhaps as a percentage or both.
 - reason for miss - branch due to return, loop breakout, or assertion.

Overall score - where 100% would be every executable statement covered, 0% would be none covered.
