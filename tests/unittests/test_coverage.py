"""Test the pytest_gitcov.coverage module
"""
import pytest

from unittest.mock import patch
from unittest.mock import sentinel
from unittest.mock import MagicMock

from hamcrest import assert_that
from hamcrest import equal_to

from pytest_gitcov.coverage import get_coverage_data_from_file
from pytest_gitcov.coverage import get_coverage_timestamp

@pytest.mark.skip
#@patch('pytest_gitcov.coverage.CoverageData')
def test_get_coverage_from_file(mock_CoverageData):
    """Check flow"""
    mock_CoverageData.return_value = sentinel.cov_data

    cov_data = get_coverage_data_from_file(path=sentinel.path)

    mock_CoverageData.called_with(sentinel.path)
    assert_that(cov_data, equal_to(sentinel.cov_data))


@patch('pytest_gitcov.coverage.os')
def test_get_coverage_timestamp(mock_os):
    """Timestamp of coverage data"""
    cov_data = MagicMock()

    cov_data.base_filename.return_value = sentinel.path
    mock_os.path.getmtime.return_value = sentinel.timestamp

    timestamp = get_coverage_timestamp(cov_data)

    mock_os.path.getmtime.called_with(path=sentinel.path)
    assert_that(timestamp, equal_to(sentinel.timestamp))
