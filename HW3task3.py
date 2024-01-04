#Создайте словарь со списком вещей для похода в качестве ключа и 
# их массой в качестве значения. Определите какие вещи влезут в 
# рюкзак передав его максимальную грузоподъёмность. Достаточно 
# вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

def common_sum (dict_of_items, set_of_items):
    sum = 0
    for key, value in dict_of_items.items():
        if not key in set_of_items:
            sum+=value
    return sum
    
    
def find_max (temp_dict, set_of_items, list_fail):
    while temp_dict:
        max_value = max(temp_dict, key=(lambda k: dict_of_items[k]))
        if max_value in set_of_items or max_value in list_fail:
            temp_dict.pop(max_value)
        else:
            list_fail.append(max_value)
            break
    return max_value


dict_of_items = dict\
(Котелок=3, Палатка=4.1, Гитара=2.7, Мангал=2, Шампура=0.3, Тушенка=0.8, Мясо=5, Вода=9, Сухпаек=3, Спички=0.1)

set_of_items = set()
list_fail = []
size_bag = float(input("Введите грузоподъемность рюкзака в кг: "))
if common_sum(dict_of_items, set_of_items) <= size_bag:
    for k in dict_of_items:
        set_of_items.add(k)
else:
    while size_bag >= min(dict_of_items.values()):
        temp_dict = dict_of_items.copy()
        current_item = find_max(temp_dict, set_of_items, list_fail)
        if dict_of_items[current_item] <= size_bag:
            set_of_items.add(current_item)
            size_bag-=dict_of_items[current_item]
        else:
            list_fail.append(current_item)
print("Из имеющегося набора можно взять -", set_of_items)