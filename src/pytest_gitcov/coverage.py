"""Coverage parsing
"""
import os

from typing import Iterable

from coverage import CoverageData


def get_coverage_from_file(path: str = '.coverage') -> CoverageData:
    """Get the coverage data from a file

    Coverage is generally stored in a '.covarage' file in
    sqllite format, which can be loaded for post processing.

    Args:
        path (str): path to the coverage file

    Raises:
        AssertionError: raised when coverage data object is empty

    Returns:
        CoverageData: previously recorded test coverage
    """
    cov_data = CoverageData(basename=path)

    assert cov_data, 'CoverageData is loaded'

    return cov_data


def get_coverage_timestamp(cov_data: CoverageData) -> float:
    """Get the time modified for the coverage data

    Args:
        cov_data (CoverageData): coverage data object

    Returns:
        float: time stamp of the last modification of coverage file
    """
    path = cov_data.base_filename()
    timestamp = os.path.getmtime(path)

    return timestamp


def files_covered(cov_data: CoverageData) -> Iterable[str]:
    """Generate a list of file

    Args:
        cov_data (CoverageData): coverage data object

    Yields:
        str: path for each of the files with coverage by tests
    """
    for path in cov_data.measured_files():
        if path.endswith('.py'):
            yield path
