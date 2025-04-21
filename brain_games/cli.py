import prompt


def welcome_user():
    name = prompt.string('¿Puedes darme tu nombre? ')
    print(f'Hello, {name}!')
