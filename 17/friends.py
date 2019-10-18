from typing import (List, Tuple)
from itertools import (permutations, combinations)

def friends_teams(friends: List[str],
                  team_size: List[int] = 2,
                  order_does_matter: bool = False) -> Tuple[str, ...]:
    if order_does_matter:
        return permutations(friends, team_size)
    else:
        return combinations(friends, team_size)
