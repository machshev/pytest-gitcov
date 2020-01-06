"""Plugin to pytest to report on coverage for the code
changed in the last commit.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from coverage import CoverageData


def get_coverage_from_cov_plugin(config) -> 'CoverageData':
    """Get the coverage from pytest_cov plugin

    Args:
        config: pytest configuration object

    Raises:
        AssertionError: raised when coverage data object is empty

    Returns:
        CoverageData: test coverage from this test run
    """
    cov_plugin = config.pluginmanager.getplugin('_cov')
    cov_data = cov_plugin.cov_controller.cov.get_data()

    assert cov_data, 'CoverageData is loaded'

    return cov_data

# TODO: add pytest option to give the commit dif details

def pytest_terminal_summary(terminalreporter, config):
    terminalreporter.write('HEY! This is GITCOV....\n')

    cov_data = get_coverage_from_cov_plugin(config)

    # TODO: convert the following to an external function so it can be
    # used from command line tool as well

    # TODO: get list of files from commit
    for filename in cov_data.measured_files():
        # TODO: check the filename is in the commit range specified

        # TODO: Rationalise this info into a simple line numbers list.
        lines = cov_data.lines(filename)
        arcs = cov_data.arcs(filename)

        # TODO: Yield the information as a dict/tuple
        # TODO: generic function to use the dict/tuple to compile report as str
        terminalreporter.write(
            f'{filename}\n{lines}:{arcs}\n\n',
        )
