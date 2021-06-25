def sum_of_multiples(limit, factors):
    if factors == []:
        return 0
    factors.sort()
    if factors[0] == 0:
        factors.pop(0)
    thesum = 0
    multiples = []
    for factor in factors:
        i = 1
        while (factor * i) < limit:
            if (factor * i) not in multiples:
                multiples.append(factor * i)
                thesum += factor * i
            i += 1
    # print(multiples)
    return thesum


# print(sum_of_multiples(10, [3, 5]))
