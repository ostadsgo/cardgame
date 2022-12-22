class Game:
    """Game logic"""

    def __init__(self, cards=None):
        self._total_score = 0

    def total_score(self):
        return self._total_score

    def parse_cards(self, cards):
        """Chop card name to sepreated list."""
        keys = ["numbers", "symbols", "colors", "fillings"]
        data = {key: [] for key in keys}

        for card in cards:
            number, symbol, _, color, filling = card.split()
            values = [number, symbol, color, filling]
            for key, value in zip(keys, values):
                data[key].append(value)
        return data

    def get_uniques(self, data):
        """Iterate over `data` dict and make value of it to be unique."""
        return {key: set(value) for key, value in data.items()}

    def calculate_score(self, cards):
        """How score calculated:
        Same color: 1 point
        number of symbol in the image be equal: 1 point
        Exact same symbol: 1 point
        Exact same filling (pattern of the image): 1 point
        If none of the above happend decrease 1 points
        `card` list of selected card by the user or computer!
        """
        score = 0
        data = self.parse_cards(cards)
        uniques = self.get_uniques(data)
        sum_lenghts = sum(len(val) for val in uniques.values())
        for item in uniques.values():
            if sum_lenghts == 12:
                score += 3
                break
            elif len(item) == 1:  # found a similler specifity like color
                score += 2
                break
        else:
            score -= 1

        self._total_score += score
        return score

    def make_hands(self, cards):
        """Get list of cards and created hands of them.
        Each hand is set of 6 cards.
        """
        return [cards[i - 3 : i] for i in range(3, len(cards) + 3, 3)]

    def hands_score(self, hands):
        """A hand is set of 6 cards."""
        d = []
        for hand in hands:
            score = self.calculate_score(hand)
            d.append({"hand": hand, "score": score})
        return d

    def sort_hand(self, hands_scores):
        """Get a hand (images name) to rank, sort by high score"""
        return sorted(hands_scores, key=lambda row: row["score"], reverse=True)

    def computer_play(self):
        pass
