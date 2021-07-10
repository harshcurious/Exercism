def check_triplets(a, b, c):
    '''Checks if a**2 + b**2 = c**2'''
    return a**2 + b**2 == c**2


def triplets_with_sum(number):
    triplets = []
    for a in range(1, number//3):
        for b in range(a+1, (number-a)//2):
            c = number - a - b
            if c > b and check_triplets(a, b, c):
                triplets.append([a, b, c])
    return triplets


if __name__ == "__main__":
    print(triplets_with_sum(12))

# Some better solutions available here: https://www.mathblog.dk/project-euler-39-perimeter-right-angle-triangle/
