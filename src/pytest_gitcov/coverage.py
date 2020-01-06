"""Coverage parsing
"""

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
    #cov_data.read()

    assert cov_data, 'CoverageData is loaded'

    return cov_data
