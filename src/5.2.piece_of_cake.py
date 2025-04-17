def piece_of_cake(*, prices, optionals, **kwargs):
    total = 0
    for item, quantity in kwargs.items():
        if item in optionals:
            continue
        if item not in prices:
            continue
        total += (quantity / 100) * prices[item]
    return total
