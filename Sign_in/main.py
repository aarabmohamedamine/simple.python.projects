
def valid_choice():
    choices = [i for i in range(1,5)]
    while True:
        try :
            choice = int(input(":"))
            if choice in choices:
                return choice
        except ValueError:
            print('Must me a number')

def display_menu():
    print('Welcom to amine.com')
    print('-'*40)
    print('please enter your choice.')
    print('1.Create acount.')
    print('2.Log in ')
    print('3.Search for account.')
    print('4.change password .')

