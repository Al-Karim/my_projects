import json

def get_username():
    """Получает имя пользователя, если оно есть"""
    filename = 'user.json'
    try:
        with open(filename) as f:
            user = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user


def greet_user():
    """Приветствие Пользователя"""

    username = get_username()
    if username:
        print("Good morning " + username + "!")
    else:
        username = input("Введите ваше имя: ")
        filename = 'user.json'
        with open(filename, 'w') as fl:
            json.dump(username, fl)
            print("Мы запомнили ваше имя, как " + username + "!")

greet_user()
