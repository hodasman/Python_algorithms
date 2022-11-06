from uuid import uuid4
import hashlib
import json

def validate_password():
    salt2 = input('enter login for sign in: ')
    password2 = input('enter password for sign in: ')
    res2 = hashlib.sha256(password2.encode() + salt2.encode()).hexdigest()
    with open('passwd.json', 'r', encoding='utf-8') as f:
        dct = json.load(f)
        if dct[salt2] == res2:
            print( 'all right')
        else:
            print('password or login invalid')
            return validate_password()

def add_password():
    salt = input('enter login: ')
    password = input('enter password: ')

    res = hashlib.sha256(password.encode() + salt.encode()).hexdigest()
    with open('passwd.json', 'r', encoding='utf-8') as f:
        dct = json.load(f)
        dct[salt] = res
        with open('passwd.json', 'w', encoding='utf-8') as f:
            json.dump(dct, f)
    print(f'Хеш {res} записан в базу данных логин: {salt}')


add_password()

