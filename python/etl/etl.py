def transform(legacy_data):
    new_data = {}
    for key in legacy_data.keys():
        for iterator in legacy_data[key]:
            new_data[iterator.lower()] = key
    return new_data
