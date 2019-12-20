import math

STAR = "+"
LEAF = "*"
TRUNK = "|"


def generate_improved_xmas_tree(rows=10):
    num_leafs = lambda row: row * 2 - 1
    width = num_leafs(rows)
    star = "{0:^{1}}".format(STAR, width)
    tree = '\n'.join(f"{LEAF * num_leafs(row):^{width}}" for row in range(1, rows + 1))
    half = width / 2
    is_good_ = lambda trunk_width: (width - trunk_width) % 2 == 0
    if type(half) == int:  # is whole number
        trunk_width = half
    else:
        trunk_width = math.ceil(half)
        while(not is_good_(trunk_width)):
            trunk_width += 1

    trunk = '\n'.join(f'{TRUNK * trunk_width:^{width}}' for _ in range(2))
    ret = '\n'.join([star, tree, trunk])
    return ret
    
