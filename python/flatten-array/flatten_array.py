def flatten(iterable):
    l = []
    for iterator in iterable:
        if hasattr(iterator, '__iter__'):
            # Checking if `iterator` is iterable.
            if any([hasattr(element, '__iter__') for element in iterator]):
                # Checking if there are any sublists; *flattening* if there are.
                iterator = flatten(iterator)
            # Getting rid of `None` values using list comprehension
            l.extend([i for i in iterator if i])
        else:
            if iterator != None:
                l.append(iterator)

    # print(iterable, l)
    return l


# # inputs = [0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]
# inputs = [0, 2, [[2, 3], 8, [[100]], None, [[None]]], -2]
# print(flatten(inputs))
