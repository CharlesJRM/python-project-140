import prompt


def welcome_user():
    name = prompt.string('¿May I have your name?')
    print(f'Hi, {name}!')


def main():
    print("Welcome to the Brain Games!")
    welcome_user()


if __name__ == "__main__":
    main()
