class Game:
    """Game logic"""

    def __init__(self, cards=None):
        self.cards = cards
        self.total_score = 0

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
        If none of the above happend decrease 1 points
        """
        score = 0
        data = self.parse_cards()
        uniques = self.get_uniques(data)
        key_num = len(uniques.keys())
        val_num = sum({len(val) for val in uniques.values()})
        # if all criteria were different
        if val_num == 12:
            score += 3
        else:
            score -= 1

        # if just one of the criteria be same
        if val_num >= 4:
            score += 2
        print("Score: ", score)
        print(uniques, key_num, val_num)
        self.total_score += score
