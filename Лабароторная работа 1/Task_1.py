numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum = 0
index = numbers.index(None)
for i in range(len(numbers)):
    if numbers[i] != numbers[index]:
        sum += numbers[i]
numbers[index] = sum/len(numbers)
print("Измененный список:", numbers)