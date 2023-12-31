#Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
#Используйте правило для проверки: “Число является простым, 
# если делится нацело только на единицу и на себя”. 
#Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

print()
a = int(input("Введите число от 1 до 100 000: "))
LOWER_LIMIT = 0
UPPER_LIMIT = 100000
while a <= LOWER_LIMIT or a >= UPPER_LIMIT:
    if a <= LOWER_LIMIT or a >= UPPER_LIMIT:
        print("Число не подходит!")
        a = int(input("Введите число от 1 до 100 000: "))
print(f"Проверка числа {a}")

counter = 0
for i in range(1, a + 1):
    if a % i == 0:
        counter += 1
if counter == 2:
    print("Ваше число - простое!")
else:
    print("Ваше число - составное!")