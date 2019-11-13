def get_profile(name: str, age: int, *sports, **awards):
    if not isinstance(age, int):
        raise ValueError
    if len(sports) > 5:
        raise ValueError
    stats = dict(name=name, age=age)
    if sports:
        stats['sports'] = sorted(list(sports))
    if awards:
        stats['awards'] = dict(awards)

    return stats
    