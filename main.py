import sqlite3
from random import randint

global db
global sql
db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    pasword TEXT,
    cash BIGINT
)""")

db.commit()


def reg():
    user_login = input("Login: ")
    user_pasword = input("Pasword: ")

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?,?,?)", (user_login, user_pasword, 0))
        db.commit()
    else:
        print('Такая запись уже имеется')

    for value in sql.execute("SELECT * FROM users"):
        print(value)

def delete_db():
    sql.execute(f'DELETE FROM users WHERE login = "{user_login}"')
    db.commit()

    print("Запись удалена")


def casino():
    global user_login
    user_login = input("log in: ")
    number = randint(1, 2)

    for i in sql.execute(f"SELECT cash FROM users WHERE login = '{user_login}'"):
        balans = i[0]

    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
    if sql.fetchone() is None:
        print("Такого логина не существует. Зарегистрируйтесь!")
        reg()
        print("/n")
    else:
        if number == 1:
            sql.execute(f'UPDATE users SET cash = {1000 + balans} WHERE login = "{user_login}"')
            db.commit()
        else:
            print("Вы програли")
            delete_db()

def enter():
    for i in sql.execute('SELECT login, cash FROM users'):
        print(i)


def main():
    casino()
    enter()


main()

