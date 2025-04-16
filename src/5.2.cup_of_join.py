def cup_of_join(*args, sep=None):
    result = []
    for i, lst in enumerate(args):
        if i > 0 and sep is not None:
            result.append(sep)
        result.extend(lst)
    if sep is not None:
        result.append(sep)
    return result
