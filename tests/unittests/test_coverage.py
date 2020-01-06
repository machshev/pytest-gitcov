"""Test the pytest_gitcov.coverage module
"""

from unittest.mock import patch
from unittest.mock import sentinel

from hamcrest import assert_that
from hamcrest import equal_to

from pytest_gitcov.coverage import get_coverage_from_file


@patch('pytest_gitcov.coverage.CoverageData')
def test_get_coverage_from_file(mock_CoverageData):
    """Check flow"""
    mock_CoverageData.return_value = sentinel.cov_data

    cov_data = get_coverage_from_file(path=sentinel.path)

    mock_CoverageData.called_with(sentinel.path)
    assert_that(cov_data, equal_to(sentinel.cov_data))
