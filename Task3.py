# Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
#  Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
#  Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no
bilet = int(input('Введите номер билета из 6 цифр: '))
sum1 = 0
sum2= 0
for i in range(6):
    if i <3:
        sum1 += bilet%10
    else:
        sum2 += bilet%10
    bilet//=10
if sum1 == sum2:
    print('Номер билета счастливый!')
else:
    print('БИЛЕТ НЕСЧАСТЛИВЫЙ')


