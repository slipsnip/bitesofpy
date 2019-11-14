from typing import Generator


def version_gt_(lhs, rhs):
    lhs, rhs = [operand.split('.') for operand in [lhs, rhs]]
    lhs = list(map(int, lhs))
    rhs = list(map(int, rhs))
    i = 0
    while(True):
        try:
            if lhs[i] == rhs[i]:
                i += 1
                continue
            if lhs[i] > rhs[i]:
                return True
            if lhs[i] < rhs[i]:
                return False
        except IndexError:
            break
        i += 1
        if i == 4:
            return False

    # if greater than ; True
    # if equal to , check next
    # if less than ; False


def changed_dependencies(old_reqs: str, new_reqs: str) -> Generator[str, None, None]:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
#  major.minor[.build[.revision]]
    old, new = [reqs.strip().splitlines() for reqs in [old_reqs, new_reqs]]
    for i in range(len(old)):
        pkg, old_ver = old[i].split('==')
        new_ver = new[i].split('==')[-1]
        if version_gt_(new_ver, old_ver):
            yield pkg
