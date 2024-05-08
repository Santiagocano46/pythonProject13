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


# Ejemplo de uso
game = BowlingGame()
game.add_player("Player 1")

# Se simula un juego de ejemplo
rolls = [10, 5, 5, 9, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]  # Ejemplo de tiradas para un juego completo
current_player = 0
for roll in rolls:
    game.roll(current_player, roll)
    if roll != 10:  # Si no es un strike, cambia de jugador
        current_player = (current_player + 1) % len(game.players)

# Obtener y mostrar los puntajes finales
for i, player in enumerate(game.players):
    print(f"Puntaje del jugador {i + 1} ({player.name}): {game.score(i)}")
