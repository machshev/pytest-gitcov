"""Coverage parsing
"""
import os

from typing import Iterable
from typing import List
from typing import Tuple
from typing import TYPE_CHECKING

from coverage import CoverageData

if TYPE_CHECKING:
    from coverage import Coverage


def get_coverage_run_source(coverage: 'Coverage') -> Tuple[str]:
    """Get the run:source from coverage config

    Args:
        coverage (Coverage): coverage instace to query for
            the configuration.

    Returns:
        list(str): list of the source directories coverage
            is run against
    """
    return (
        os.path.abspath(path)
        for path
        in coverage.get_option('run:source')
    )


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

def get_line_num_covered_for_file(
        cov_data: CoverageData,
        path: str
) -> List[int]:
    """Get a list of the line numbers covered for a given file

    Args:
        path (str): absolute path for the file to get coverge of

    Returns:
        list(int): a list of the line numbers covered
    """
    line_nums = cov_data.lines(path)
    arcs = cov_data.arcs(path)

    if arcs:
        for start, end in arcs:
            line_nums.append(abs(start))
            line_nums.append(abs(end))

        return list(set(line_nums))

    return []
