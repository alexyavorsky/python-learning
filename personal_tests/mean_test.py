test_list = [1, 2, 3, 4, 4.2, 6.3433, 7, 8, 9, 10]

if len(test_list) % 2 == 0:
    mean = sum(test_list[len(test_list) // 2 - 1:len(test_list) // 2 + 1]) / 2
else:
    mean = test_list[len(test_list) // 2]

print(f"{mean:.2f}")
print(round(mean, 2))