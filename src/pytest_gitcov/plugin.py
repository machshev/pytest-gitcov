"""Plugin to pytest to report on coverage for the code
changed in the last commit.
"""
from typing import TYPE_CHECKING

from pytest_gitcov.report import (
    calculate_commit_coverage,
    generate_report,
)

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
    cov_data = get_coverage_from_cov_plugin(config)

    covered_files = calculate_commit_coverage(
        cov_data=cov_data,
    )

    report = generate_report(covered_files)
    terminalreporter.write(report)
