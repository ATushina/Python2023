#Программа загадывает число от 0 до 1000. 
# Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
# Для генерации случайного числа используйте код: from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
rand_num = randint(0,1000)
print("Загадано число от 0 до 1000. Угадайте число за 10 попыток!")
for i in range(9, -1, -1):
    user_num = int(input("Введите число: "))
    if user_num == rand_num:
        print("Вы угадали!")
        break
    elif i == 0:
        print(f"Вы не угадали, загаданное число было {rand_num}")
    elif user_num > rand_num:
        print(f"Меньше, осталось попыток :{i}")
    else:
        print(f"Больше, осталось попыток :{i}")