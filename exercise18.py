class Game:
    def __init__(self, level=None):
        self._level = level if level else 0

    @property
    def mod_level(self):
        return self._level
    
    @mod_level.setter
    def mod_level(self, value):
        if not isinstance(value, int):
            raise TypeError('The value of level must be of type int.')
        if value < 0:
            self._level = 0
        elif value > 100:
            self._level = 100
        else:
            self._level = value


games = [Game(), Game(10), Game(-10), Game(120)]

for game in games:
    print(game.mod_level)    
