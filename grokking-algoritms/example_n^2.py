example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

empty_list = []

for left in example_list:
    for right in example_list:
        s = str(left) + str(right)
        empty_list.append(s)

print(len(empty_list))