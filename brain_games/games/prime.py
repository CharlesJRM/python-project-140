import random
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Función que verifica si un número es primo"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    """Genera una ronda para el juego"""
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return str(number), correct_answer


def main():
    run_game(RULE, generate_round)
