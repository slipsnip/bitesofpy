from collections import defaultdict
from operator import itemgetter


names = 'bob julian tim martin rod sara joyce nick beverly kevin'.split()
ids = range(len(names))
users = dict(zip(ids, names))  # 0: bob, 1: julian, etc

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
               (3, 4), (4, 5), (5, 6), (5, 7), (5, 9),
               (6, 8), (7, 8), (8, 9)]


def get_friend_with_most_friends(friendships, users=users):
    """Receives the friendships list of user ID pairs,
       parse it to see who has most friends, return a tuple
       of (name_friend_with_most_friends, his_or_her_friends)"""
    breakpoint
    dd = defaultdict(list)
    for fs in friendships:
        dd[fs[0]].append(fs[1])
        dd[fs[1]].append(fs[0])
    most_popular = max(dd, key=lambda f: len(dd[f]))
    friends = [users[id] for id in dd[most_popular]]
    return (users[most_popular], friends)
    

