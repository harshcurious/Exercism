def primes(limit):
    prime = []
    if limit < 2:
        return prime
    if limit == 2:
        return [2]
    numbers = list(range(2, limit+1))
    while numbers != []:
        p = numbers.pop(0)
        print(p)
        prime.append(p)
        i = 2
        while (p*i) <= limit:
            if p*i in numbers:
                numbers.remove(p*i)
            i += 1
        print(numbers)
        print(prime)
    return prime


# Testing
# print(primes(10))
