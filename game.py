class Game:
    """Game logic"""

    def __init__(self, cards=None):
        self.cards = cards
        self.score = 0

    def set_cards(self, cards):
        self.cards = cards

    def parse_cards(self):
        keys = ["numbers", "symbols", "colors", "fillings"]
        data = {key: [] for key in keys}

        for card in self.cards:
            number, symbol, _, color, filling = card.name.split()
            values = [number, symbol, color, filling]
            for key, value in zip(keys, values):
                data[key].append(value)
        return data

    def get_uniques(self, data):
        return {key: set(value) for key, value in data.items()}

    def calculate_score(self):
        """How score calculated:
        Same color: 1 point
        number of symbol in the image be equal: 1 point
        Exact same symbol: 1 point
        Exact same filling (pattern of the image): 1 point
        If none of the above happend decrease 2 points
        """
        data = self.parse_cards()
        uniques = self.get_uniques(data)
        for val in uniques.values():
            if len(val) == 1:
                self.score += 2
                break
        else:  # no breaks
            self.score -= 2

        for val in uniques.values():
            # player couldn't found all diffrence
            if len(val) < 3:
                break
        else:  # player found all diffrent
            self.score += 3

        return self.score
