import prompt

def welcome_user():
    name = prompt.string('¿Puedes darme tu nombre? ')
    print(f'¡Hola, {name}!')

def main():
    print("Welcome to the Brain Games!")
    welcome_user()

if __name__ == "__main__":
    main()
