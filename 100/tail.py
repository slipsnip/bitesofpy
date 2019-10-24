import re


def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    with open(filepath) as file_fd:
        lines = ''.join(file_fd.readlines())
        lines = lines.splitlines()[-n:]
        return lines
