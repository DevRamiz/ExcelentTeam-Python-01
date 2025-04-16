def group_by(key_function, items):
    grouped = {}
    for item in items:
        key = key_function(item)
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(item)
    return grouped
