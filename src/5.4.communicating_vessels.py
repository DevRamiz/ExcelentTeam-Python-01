def interleave(*iterables):
    result = []
    for items in zip(*iterables):
        result.extend(items)
    longest = max(iterables, key=len, default=[])
    rest_start = len(min(iterables, key=len, default=[]))
    for iterable in iterables:
        result.extend(iterable[rest_start:])
    return result

def generator_interleave(*iterables):
    iterators = [iter(it) for it in iterables]
    while iterators:
        next_round = []
        for it in iterators:
            try:
                yield next(it)
                next_round.append(it)
            except StopIteration:
                continue
        iterators = next_round
