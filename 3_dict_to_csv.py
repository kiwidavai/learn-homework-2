"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

lists = [
            {'name': 'Nikita', 'age': 26, 'job': 'master'},
            {'name': 'Alex', 'age': 30, 'job': 'engineer'},
            {'name': 'Bob', 'age': 45, 'job': 'dantist'},
            {'name': 'Jack', 'age': 21, 'job': 'programmer'}
]

def main():
    with open ('lists.csv', 'w', encoding='utf-8') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in lists:
            writer.writerow(user)
        

if __name__ == "__main__":
    main()
