import random

RULE = "What number is missing in the progression?"

def generate_round():
    # Crear la progresión aritmética
    start = random.randint(1, 10)
    step = random.randint(2, 5)
    progression = [start + step * i for i in range(10)]

    # Elegir una posición aleatoria para el número faltante
    missing_index = random.randint(0, 9)
    correct_answer = progression[missing_index]

    # Reemplazar el número faltante con dos puntos
    progression[missing_index] = ".."
    question = " ".join(map(str, progression))

    return question, str(correct_answer)

def main():
    run_game(RULE, generate_round)