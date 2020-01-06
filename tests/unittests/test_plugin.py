"""Unit tests for the pytest-gitcov plugin
"""
from unittest.mock import patch
from unittest.mock import sentinel
from unittest.mock import MagicMock

from hamcrest import assert_that
from hamcrest import equal_to

from pytest_gitcov.plugin import get_coverage_from_cov_plugin


def test_get_coverage_from_cov_plugin():
    """Check flow"""
    mock_config = MagicMock()
    mock_cov_plugin = MagicMock()

    mock_config.pluginmanager.getplugin.return_value = mock_cov_plugin
    mock_cov = mock_cov_plugin.cov_controller.cov
    mock_cov.get_data.return_value = sentinel.cov_data

    cov_data = get_coverage_from_cov_plugin(mock_config)

    mock_config.pluginmanager.getplugin.called_with('_cov')
    assert_that(cov_data, equal_to(sentinel.cov_data))
