import os
from functools import reduce


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    file_counts = [(1 if dir != directory else 0, len(files)) for dir, dirs, files in os.walk(directory)]
    return reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), file_counts)