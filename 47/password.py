import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())
"""
is between 6 and 12 chars long (both inclusive)
has at least 1 digit [0-9]
has at least two lowercase chars [a-z]
has at least one uppercase char [A-Z]
has at least one punctuation char (use: PUNCTUATION_CHARS)
Has not been used before (use: used_passwords)
"""

def validate_password(password: str) -> bool:
    test_atleast_one = re.compile(r'^.*(?=.*\d)(?=.*[A-Z])(?=.*[!\"#$%&\'\(\)\*\+\,\./:;<=>?@\[\]\^_`{|}~]).*$')
    if not test_atleast_one.match(password) or \
        len(password) not in range(6,13) or \
        len(re.findall(r'[a-z]', password)) < 2 or \
        password in used_passwords:
        return False
    used_passwords.add(password)
    return True

    
    