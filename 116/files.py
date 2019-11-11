from pathlib import Path
ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    working_dir = Path(dirname)
    for file in working_dir.glob('*'):
        if file.stat().st_size / ONE_KB >= size_in_kb:
            yield file