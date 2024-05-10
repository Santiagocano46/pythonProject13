class Frame:
    def __init__(self):
        self.rolls = []

    def add_roll(self, pins):
        self.rolls.append(pins)

    def is_strike(self):
        return len(self.rolls) == 1 and self.rolls[0] == 10

    def is_spare(self):
        return len(self.rolls) == 2 and sum(self.rolls) == 10

    def score(self, next_frame=None, next_next_frame=None):
        if self.is_strike():
            if next_frame:
                score = 10 + next_frame.score()
                if next_frame.is_strike() and next_next_frame:
                    score += next_next_frame.rolls[0]
                return score
            else:
                return 10
        elif self.is_spare():
            if next_frame:
                return 10 + next_frame.rolls[0]
            else:
                return 10
        else:
            return sum(self.rolls)


class BowlingGame:
    def __init__(self, players):
        self.players = players
        self.frames = {player: [Frame() for _ in range(10)] for player in players}
        self.current_frame = {player: 0 for player in players}

    def roll(self, pins, player):
        self.frames[player][self.current_frame[player]].add_roll(pins)
        if self.frames[player][self.current_frame[player]].is_strike() or \
                len(self.frames[player][self.current_frame[player]].rolls) == 2:
            self.current_frame[player] += 1
            if self.current_frame[player] >= 10:
                self.current_frame[player] = 0

    def score(self):
        total_scores = {player: 0 for player in self.players}
        for player in self.players:
            for i, frame in enumerate(self.frames[player]):
                if i < 8:
                    total_scores[player] += frame.score(self.frames[player][i+1], self.frames[player][i+2])
                elif i == 8:
                    total_scores[player] += frame.score(self.frames[player][i+1])
                else:
                    total_scores[player] += frame.score()
        return total_scores


# Registro de jugadores
def register_players():
    players = []
    while True:
        player_name = input("Ingrese el nombre del jugador (o 'listo' para terminar): ").strip()
        if player_name.lower() == 'listo':
            break
        players.append(player_name)
    return players


# Ejemplo de uso
players = register_players()
game = BowlingGame(players)

while True:
    for player in players:
        print(f"Turno de {player}:")
        while True:
            try:
                pins = int(input("Ingrese la cantidad de pines derribados (0-10): "))
                if 0 <= pins <= 10:
                    game.roll(pins, player)  # Agregar el puntaje para el jugador actual
                    break
                else:
                    print("Ingrese un valor entre 0 y 10.")
            except ValueError:
                print("Ingrese un valor numérico.")

    print("Puntajes:")
    scores = game.score()
    for player in players:
        print(f"{player}: {scores[player]}")

    continuar = input("¿Desea continuar jugando (s/n)? ").strip().lower()
    if continuar != 's':
        break

