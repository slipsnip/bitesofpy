from pathlib import PosixPath
from difflib import (SequenceMatcher, get_close_matches)
from operator import (itemgetter, attrgetter)

SIMILAR = (0.6)


def get_matching_files(directory: PosixPath, filter_str: str) -> list:
    """Get all file names in "directory" and (case insensitive) match the ones
       that exactly match "filter_str"

       In case there is no exact match, return closely matching files.
       If there are no closely matching files either, return an empty list.
       (Return file names, not full paths).

       For example:

       d = Path('.')
       files in dir: bite1 test output

       get_matching_files(d, 'bite1') => ['bite1']
       get_matching_files(d, 'Bite') => ['bite1']
       get_matching_files(d, 'pybites') => ['bite1']
       get_matching_files(d, 'test') => ['test']
       get_matching_files(d, 'test2') => ['test']
       get_matching_files(d, 'output') => ['output']
       get_matching_files(d, 'o$tput') => ['output']
       get_matching_files(d, 'nonsense') => []
    """
    files = list(file.name for file in directory.iterdir())
    matches = get_close_matches(filter_str, files, cutoff=1.0)
    return get_close_matches(filter_str, files) if not matches else matches
