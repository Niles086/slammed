from kivy.storage.jsonstore import JsonStore

class UserProfile:
    def __init__(self, username):
        self.username = username

class Game:
    def __init__(self, name, rules):
        self.name = name
        self.rules = rules

store = JsonStore('games.json')

def save_game(game):
    store.put(game.name, rules=game.rules)

def load_games():
    games = []
    for game in store:
        games.append(Game(game, store.get(game)['rules']))
    return games
