import csv
import json

# работаем со списком книг
with open('../data/books.csv', 'r') as book_f:
    books = csv.DictReader(book_f,
                           delimiter=',')  # c помощью DictReader преобразуем первую строку в ключи, т.к. они там есть
    books_spicok = []  # далее создаем нужный нам список в засимости от требований по ДЗ
    for book in books:
        books_spicok.append(
            {'title': book['Title'], 'author': book['Author'], 'pages': book['Pages'], 'genre': book['Genre']})
#    for row in books_spicok:
#        print(row)

# Работаем со списком читателей
with open("../data/users.json", "r") as user_f:
    # users = json.load(user_f)
    str1 = user_f.read()
    users = json.loads(str1)
    users_spisok = []
    for user in users:
        users_spisok.append(
            {'name': user['name'], 'gender': user['gender'], 'address': user['address'], 'age': user['age'],
             'books': []})
#    for user in users_spisok:
#        print(user)
# раздаем книги
i = 0
while len(books_spicok) > 0:
    book = books_spicok[0]
    users_spisok[i]['books'].append(book)
    books_spicok.remove(book)
    if i != len(users_spisok) - 1:
        i += 1
    else:
        i = 0

#    for user in users_spisok:
#        print(user)

# сохраняем результат в нужный файл
with open('../data/result.json', 'w') as file:
    file.write(json.dumps(users_spisok, indent=4))
