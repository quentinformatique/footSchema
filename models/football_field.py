class FootballField:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def get_player(self, x, y):
        for player in self.players:
            player_x, player_y = player.get_position()
            if player_x == x and player_y == y:
                return player
        return None
