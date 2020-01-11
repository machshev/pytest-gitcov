"""Report on commit coverage
"""
from typing import (
    Dict,
    List,
    Any,
    Optional,
    TYPE_CHECKING,
)

from pytest_gitcov.git import files_in_commit

from pytest_gitcov.coverage import (
    get_coverage_data_from_file,
    get_coverage_timestamp,
    get_line_num_covered_for_file,
    files_covered,
)

if TYPE_CHECKING:
    from coverage import CoverageData


def calculate_commit_coverage(
        cov_data: 'CoverageData',
        commit_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Calculate the test coverage for the lines changed in the
    given git commit Id

    Args:
        cov_data (CoverageData): coverage data object
        commit_id (str): id of the commit to calculate coverage on
    """
    git_files = list(files_in_commit(commit_id))
    cov_files = list(files_covered(cov_data))

    covered_files = {}

    for path in git_files:
        # Is the file in the coverage report
        # Files outside coverage report are excluded
        if path in cov_files:
            line_nums = get_line_num_covered_for_file(
                cov_data=cov_data,
                path=path,
            )

            covered_files[path] = sorted(line_nums)

    return covered_files


def generate_report(covered_files: Dict) -> str:
    """Generate the report

    Args:
        covered_files (dict): git coverage data

    Returns:
        str: report as a string
    """
    report = (
        '\ngit Coverage Report\n'
        '-------------------\n'
    )

    if covered_files:
        for path, line_nums in covered_files.items():
            report += f'{path}\nCovered: {line_nums}\n'

    return report
