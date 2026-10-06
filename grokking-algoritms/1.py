def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid

        if guess < item:
            low = mid + 1

        if guess > item:
            high = mid - 1
    return None

my_list = [1, 3, 5, 6, 8, 9, 10, 13, 15, 634, 6543]

print(binary_search(my_list, -1))