from random import choice,sample
import random
import string as str
#password and account number generator  

def lenght_validation():
    while True:
        try:
            lenght = int(input('enter the lenght of the generated password: '))
            if lenght > 0:
                return lenght
        except ValueError:
            print('Must be a number .')


def password_generator():
    char = str.ascii_letters + str.digits
    lenght = random.randint(5,10)
    return "".join(sample(char,lenght))

def id_generator():
    return ''.join(sample(str.digits,6))


class user:
    def __init__(self,name):
        self.name = name
        self.id = id_generator()
        self.password = password_generator()

    def get_info(self):
        print(f'user name : {self.name}')
        print(f'user id : {self.id}')
        print(f'user password : {self.password}')

    




