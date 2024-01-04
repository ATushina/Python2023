#Дан список повторяющихся элементов. 
# #Вернуть список с дублирующимися элементами. 
#В результирующем списке не должно быть дубликатов.

my_list = [15, 5, 15, 3, 5, "today", "tomorrow", "peace", "no", "yes", "today", 3]
my_list_2 = []

for item in my_list:
    if item not in my_list_2:
        if my_list.count(item) > 1:
            my_list_2.append(item)
    
print(my_list_2)