#Напишите функцию, которая принимает на вход строку - 
# абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: 
# путь, имя файла, расширение файла.



import os

def file_info(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension

filename = str("D:/GB/PYTHON/python3/hw1/task1.py")
print(file_info(filename))

