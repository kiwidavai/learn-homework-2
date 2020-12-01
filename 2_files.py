"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as referat:
        context = referat.read()
        print(len(context))
        count = context.replace('\n',' ').split(' ')
        print(len(count))
        context_with_exclamation_mark = context.replace('.', '!')
        # print(context_with_exclamation_mark)
    with open('referat2.txt', 'w', encoding='utf-8') as referat2:
        referat2.write(context_with_exclamation_mark)
        

if __name__ == "__main__":
    main()
