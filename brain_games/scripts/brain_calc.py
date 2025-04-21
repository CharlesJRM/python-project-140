from brain_games.game_logic import run_game
from brain_games.games import calc   # Importamos la lógica del juego desde la carpeta games

def main():
    run_game(calc)   # Llamamos a la función run_game pasándole la lógica del juego

if __name__ == "__main__":
    main()
