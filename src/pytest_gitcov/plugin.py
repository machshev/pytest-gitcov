"""Plugin to pytest to report on coverage for the code
changed in the last commit.
"""

# TODO: remove and replace with real pytests on the generic functions
def some_function(a: int) -> int:
    """This is a dummy function to give something to test"""
    b = a -3

    return (4+b+7)/a

# TODO: add pytest option to give the commit dif details

def pytest_terminal_summary(terminalreporter, config):
    terminalreporter.write('HEY! This is GITCOV....\n')

    cov_plugin = config.pluginmanager.getplugin('_cov')

    # TODO: use the cov_plugin to get the covarage data file name
    # TODO: common function that gets coverage data object
    cov_data = cov_plugin.cov_controller.cov.get_data()
    cov_data.read()

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
