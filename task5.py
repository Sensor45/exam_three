
number = input('Введите любое целое положительное число: ')

sum_numbers = 0

for digit in number:
    sum_numbers += int(digit)

print("Сумма цифр:", sum_numbers)
