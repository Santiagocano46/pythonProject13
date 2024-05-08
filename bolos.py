class Frame:
    def __init__(self):
        self.rolls = []

    def add_roll(self, pins):
        self.rolls.append(pins)

    def is_strike(self):
        return len(self.rolls) == 1 and sum(self.rolls) == 10

    def is_spare(self):
        return len(self.rolls) == 2 and sum(self.rolls) == 10

    def score(self):
        return sum(self.rolls)


class Player:
    def __init__(self, name):
        self.name = name
        self.frames = [Frame() for _ in range(10)]
        self.current_frame = 0

    def roll(self, pins):
        self.frames[self.current_frame].add_roll(pins)
        if self.current_frame < 9 and (self.frames[self.current_frame].is_strike() or len(self.frames[self.current_frame].rolls) == 2):
            self.current_frame += 1

    def score(self):
        total_score = 0
        for i, frame in enumerate(self.frames):
            total_score += frame.score()
            if frame.is_strike() and i < 8:
                if self.frames[i+1].is_strike():
                    total_score += self.frames[i+1].rolls[0] + self.frames[i+2].rolls[0]
                else:
                    total_score += sum(self.frames[i+1].rolls)
            elif frame.is_spare() and i < 9:
                total_score += self.frames[i+1].rolls[0]
        return total_score


class BowlingGame:
    def __init__(self):
        self.players = []

    def add_player(self, name):
        self.players.append(Player(name))

    def roll(self, player_index, pins):
        self.players[player_index].roll(pins)

    def score(self, player_index):
        return self.players[player_index].score()


def display_menu():
    print("Bienvenido al juego de bolos!")
    print("1. Registrar jugador")
    print("2. Ingresar puntajes")
    print("3. Calcular puntajes")
    print("4. Salir")


# Función para registrar un nuevo jugador
def register_player(bowling_game):
    name = input("Ingrese el nombre del jugador: ")
    bowling_game.add_player(name)
    print(f"{name} ha sido registrado.")


# Función para ingresar puntajes
def enter_scores(bowling_game):
    player_index = int(input("Ingrese el número de jugador: ")) - 1
    if player_index < 0 or player_index >= len(bowling_game.players):
        print("Número de jugador inválido.")
        return
    print("Ingrese los puntajes para cada frame (utilice -1 para indicar un lanzamiento nulo):")
    for frame_number in range(1, 11):
        roll1 = int(input(f"Frame {frame_number}, lanzamiento 1: "))
        if roll1 == -1:
            continue
        bowling_game.roll(player_index, roll1)
        if roll1 < 10:
            roll2 = int(input(f"Frame {frame_number}, lanzamiento 2: "))
            if roll2 == -1:
                continue
            bowling_game.roll(player_index, roll2)


# Función para calcular los puntajes
def calculate_scores(bowling_game):
    for i, player in enumerate(bowling_game.players):
        print(f"Puntaje del jugador {i + 1} ({player.name}): {bowling_game.score(i)}")


# Main loop
def main():
    game = BowlingGame()
    while True:
        display_menu()
        choice = input("Ingrese su elección: ")
        if choice == "1":
            register_player(game)
        elif choice == "2":
            enter_scores(game)
        elif choice == "3":
            calculate_scores(game)
        elif choice == "4":
            print("¡Gracias por jugar!")
            break
        else:
            print("Elección no válida. Por favor, ingrese un número del 1 al 4.")


if __name__ == "__main__":
    main()

