options1 = {'a':'Add item', 'l':'List items', 'q':'Log out'}
options2 = {'r':'Try again', 'q':'Quit'}

def main():
    users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
    data  = {"nisse":["luva", "vante"],  "stina":[], "bosse":["gräs", "mjölk"]}
    return


def login(user):
    username = input('\nUsername: ')
    password = input('Password: ')

    if username in user:
        if password == user[username]:
            return username
        else:
            m = menu('\nInvalid username or password\n', "Option: ", options2)
            if m == 'r':
                login(user)
            elif m == 'q':
                return None
    else:
        m = menu('\nInvalid username or password\n', "Option: ", options2)
        if m == 'r':
            login(user)
        elif m == 'q':
            return None


def user_actions(user, items):
    print(f'Welcome {user}\n\nThese are your items\n')
    n = 0
    for the_items in items:
        n += 1
        print(f'  {n}) {the_items}')
    
    while True:
        print()
        m = menu('Select an action', 'Option: ', options1)
        
        if m == 'a':
            add('Add item: ', items)
        elif m == 'l':
             view('These are your items', items)
        elif m == 'q':
            print(f"Goodbye {user}, your items: {items}")
            return None
    

def menu(title, prompt, options):
    print(f'{title}\n')
    for n in options:
        print(f'  {n}) {options[n]}')
    print()

    while True:
        select = str(input(f'{prompt}' ))
        print()
        if select in options:
            return select
            break
        else:
            print('Invalid option\n')

def add(prompt, strings):
    add = input(prompt)
    strings.append(add)
    
def view(description, strings):
    print(f'\n{description}\n')
    n = 0
    for x in strings:
        n += 1
        print(f'  {n}) {x}')