def cup_of_join(*args, sep=None):
    result = []
    for lst in args:
        result.extend(lst)
        if sep is not None:
            result.append(sep)
    return result

if __name__ == "__main__":
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))
    print(cup_of_join([1, 2], [8], [9, 5, 6]))
    print(cup_of_join([1]))
    print(cup_of_join())
