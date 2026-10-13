# from random import shuffle
#
# my_list = list(range(10))
# shuffle(my_list)  # randomed list of digits
#
# sorted_list = []
# my_list = [3, 7, 4, 1, 2, 5, 9, 8, 6]
# while my_list:
#     for i in range(len(my_list)):
#         flag = 1
#         for j in range(i+1, len(my_list)):
#             if my_list[i] > my_list[j]:
#                 flag = 0
#                 break
#         if flag == 1:
#             sorted_list.append(my_list.pop(i))
#             break
# print(sorted_list)

my_list = [3, 7, 4, 1, 2, 5, 9, 8, 6]
sorted_list = []

while my_list:
    min_idx = 0
    for i in range(1, len(my_list)):
        if my_list[i] < my_list[min_idx]:
            min_idx = i
    sorted_list.append(my_list.pop(min_idx))

print(sorted_list)
