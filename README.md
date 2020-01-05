# pytest-gitcov
Extension for pytest to report on the coverage for the lines modified in a given commit or commit range. The vision is to be able to run pytests on a code base before submitting a pull request or code review. This would then show you the lines of code that were modified by you but not covered by unit-tests.

Issues this plugin is trying to resolve:
 - Ideally the whole code base will have reasonable coverage. Pragmatically though this is rarely the case, and so a whole repo coverage report means little in terms of one developers merge request. The hope is that using this plugin you can shine a light on the code you have touched. Making it easier to spot gaps in unit tests due to code you have written, or modified and identify a gap someone else left and should really be filled.
 - Just reporting a list of line ranges covered on the terminal is not much help. I can't remember the line numebers for the functions I've just changed, and working out where the gaps are is time consuming. The HTML report is a lot better for this, but I'd like to have something quick and simple for the terminal. 

# The plan
This is still in very early stages of development and doesn't really do much yet.

So far it just dumps a report at the end of a test run. Report contains the raw info available in the .coverage file (SQLLite3 DB) prsed using the `coverage.CoverageData` proxy (https://coverage.readthedocs.io/en/coverage-5.0/api_coveragedata.html#coverage.CoverageData).

The plan is to use `git diff --name-status HEAD~1` or `git diff --name-only HEAD~1` to get a list of files changed. Then use `git blame` and get the lines of each file changed the in current commit (perhaps with some context as well +/- 3 lines, or maybe later a whole function).

Then it *should* be a simple case of finding the lines in the commit, but not in the coverage report.

Outcome:
 - plugin for pytest that reports on current HEAD commit
 - stand-alone git-py-coverage script to run on the last .coverage report. This could be used to generate another report without having to 
