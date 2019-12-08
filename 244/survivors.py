import os
from pathlib import Path
from urllib.request import urlretrieve

S3 = "https://bites-data.s3.us-east-2.amazonaws.com/{}"
FILE_NAME = "mutpy.out"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, FILE_NAME)

if not PATH.exists():
    urlretrieve(S3.format(FILE_NAME), PATH)


def _get_data(path=PATH):
    with open(path) as f:
        return [line.rstrip() for line in f.readlines()]


def filter_killed_mutants(mutpy_output: list = None) -> list:
    """Read in the passed in mutpy output and filter out the code snippets of
       mutation tests that were killed. Surviving mutants should be shown in
       full, as well the surrounding output.

       For example, this is a killed mutant:

         - [#  15] DDL account:
      --------------------------------------------------------------------------------
        23:         if not (isinstance(amount, int)):
        24:             raise ValueError('please use int for amount')
        25:         self._transactions.append(amount)
        26:
      - 27:     @property
      - 28:     def balance(self):
      + 27:     def balance(\
      + 28:         self):
        29:         return self.amount + sum(self._transactions)
        30:
        31:     def __len__(self):
        32:         return len(self._transactions)
      --------------------------------------------------------------------------------
      [0.10240 s] killed by test_account.py::test_balance

      You should reduce this to:

         - [#  15] DDL account:
      [0.10240 s] killed by test_account.py::test_balance

      So you mute all that is in between and including th
            mutation.append(line)e 2x:
      --------------------------------------------------------------------------------

      Return the filtered output as a list of lines.
    """
    if mutpy_output is None:
        mutpy_output = _get_data()

    # for each line split()
    # if line is ----, is_mutant_ = invert is_mutant_
    #   mutant.append(line)
    # if by in split_line
    filtered = []
    mutation = []
    in_mutant_ = False
    for line in mutpy_output:
        if line == '-' * 80:
            in_mutant_ = not in_mutant_
            mutation.append(line)
            continue
        if not in_mutant_:
            if len(mutation) > 0:
                line_split = line.split()
                if 'killed' not in line_split and 'incompetent' not in line_split:
                    filtered.extend(mutation)
                    mutation = []
                else:
                    mutation = []
            filtered.append(line)
        else:
            mutation.append(line)
    return filtered
        

