import os
from functools import reduce


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    counts = [(len(dirs), len(files)) for dir, dirs, files in os.walk(directory)]
    return tuple(sum(file_count) for file_count in zip(*counts))