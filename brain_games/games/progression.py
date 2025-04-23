import random
from brain_games.game_logic import run_game

RULE = "What number is missing in the progression?"


def generate_round():
    start = random.randint(1, 10)
    step = random.randint(2, 5)
    progression = [start + step * i for i in range(10)]

    missing_index = random.randint(0, 9)
    correct_answer = progression[missing_index]

    progression[missing_index] = ".."
    question = " ".join(map(str, progression))
    return question, str(correct_answer)


def main():
    run_game(RULE, generate_round)
