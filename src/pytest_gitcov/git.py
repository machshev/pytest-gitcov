"""Git wrapper
"""
import os
import subprocess

from typing import Iterable
from typing import Optional


def files_in_commit(commit: Optional[str] = None) -> Iterable[str]:
    """Generate a list of file modifed in a commit

    If the commit id is not passed then the default is HEAD

    Args:
        commit (str): the ID of the commit to analyse

    Yields:
        str: path for each of the files with coverage by tests
    """
    cmd = ['git', 'diff', '--name-status']
    if commit is not None:
        cmd.append(f'{commit}..{commit}~1')

    output = subprocess.check_output(cmd)

    for line in output.decode('utf-8').split('\n'):
        if line == '':
            break

        path = line.split('\t')[-1]

        if not path.endswith('.py'):
            continue

        abs_path = os.path.abspath(path)

        yield abs_path
