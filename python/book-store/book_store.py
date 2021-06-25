def total(basket):
    # # # Pre-processing: converting into a list of five elements
    if basket == []:
        return 0
    # book_list = [#(book1), #(book2), #(book3), #(book4), #(book5)]
    book_list = [0, 0, 0, 0, 0]
    for i in basket:
        book_list[i-1] += 1
    # print(book_list)
    # # # Sorting the book_list to hopefully exploit possible symmetries; all books have the same properties so this is okay
    book_list.sort(reverse=True)
    print(book_list)
    return calculate_all(book_list)


def calculate_all(book_list):
    """
    Returns the value of books reccursively
    """
    if all(map(lambda book: book <= 1, book_list)):
        # # # When the number of each unique book is less than one, directly calculate the cost
        return calculate_bool(book_list)
    else:
        minimize = []
        greater1 = []
        # # # count the books with more than one copy in the basket and store this list of indices into greater1
        for j in range(5):
            if book_list[j] >= 1:
                greater1.append(j)
        if len(greater1) == 1:
            return book_list[0] * 800
        else:

            print(minimize)
            return min(minimize)


def calculate_bool(book_list=[0, 0, 0, 0, 0]):
    """
    Takes book i = 0 or 1 and calculates the cost of books
    """
    s = sum(book_list)
    # # # Should have used a list to keep track of discounts; better usability: easily change the discount values
    if s == 1:
        return 8 * 100
    elif s == 2:
        return 8 * 2 * 0.95 * 100
    elif s == 3:
        return 8 * 3 * 0.9 * 100
    elif s == 4:
        return 8 * 4 * 0.8 * 100
    elif s == 5:
        return 8 * 5 * 0.75 * 100
    elif s == 0:
        # raise Exception("All the entries shouldn't be 0")
        return 0
    # else:
    #     raise Exception("What the hell!!!")


basket = [2, 2]
basket = [1, 2, 3, 4]
basket = [1, 1, 2, 2, 3, 3, 4, 5]
basket = [1, 1, 2, 3, 4, 4, 5, 5]
print(total(basket))
