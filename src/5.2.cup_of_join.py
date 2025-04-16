def cup_of_join(*args, sep='-'):
    result = []
    for i, group in enumerate(args):
        if i > 0:
            result.append(sep)
        result.extend(group)
    if args:
        result.append(sep)
    return result
