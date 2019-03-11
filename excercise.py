dict_of_numbers = {}

for num in range(1, 51):
    if num % 2 == 0 and num % 7 == 0:
        dict_of_numbers[num] = num * 2
    elif num % 7 == 0:
        dict_of_numbers[num] = num - 1
    elif num % 2 == 0:
        dict_of_numbers[num] = num + 1
    else:
        dict_of_numbers[num] = num

print(dict_of_numbers)
