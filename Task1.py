#  Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
sum = 0
n1 = int(input('Введите число: '))
n = n1
while n > 0:
    sum+= n%10
    n //= 10
print(f'Сумма цифр числа {n1} = {sum}')