def slices(series, length):
    if length > len(series) or length <= 0:
        raise ValueError(series, length)
    sub = []
    for i in range(len(series) - length + 1):
        sub.append(series[i:i+length])
    return sub
