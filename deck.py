import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from random import shuffle
from os import listdir

from card import Card
from game import Game


class Hand(ttk.Frame):
    HAND_SIZE = 6

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

    def number(self, number):
        """Return number of hand based on user response `number`"""
        hand_number = number // self.HAND_SIZE
        self.card_number = hand_number * self.HAND_SIZE
        return self.card_number

    def make(self, n):
        x = self.number(n)
        return [
            self.images[index - self.size : index]
            for index in range(self.size, x + 1, self.size)
        ]


class Deck(ttk.Frame):
    # Cards number in a hand
    HAND_SIZE = 6

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        # tkinter variables
        self.info = self.master.info
        self.highest_chance = self.master.highest.get()
        self.user_response = self.master.card_number.get()
        # Create hands based on user input.
        self.hand = Hand()
        self.hands = self.hand.make(self.user_response)

        self.cards = []
        # all image's name
        self.all_images = listdir("./images")
        shuffle(self.all_images)
        # truncate all_images to the number user requested
        self.images = self.all_images[: self.cards_number]
        # a Game object to decide players socre after choosing 3 cards.
        self.game = Game()
        self.play()

    def play(self):
        s = f"Total Score: {self.game.total_score()}\nCards Left: {len(self.images)}"
        self.info.set(s)
        self.next_hand()

    def create_cards(self, hand):
        """Create hand of cards."""
        for image in hand:
            file = f"images/{image}"
            card = Card(self, file, image)
            card.pack(expand=True, fill=tk.BOTH)
            self.cards.append(card)
            self.images.remove(image)

    def next_hand(self, index=0):
        if self.hands:
            self.create_cards(self.hands[index])
            self.hands.pop(0)
            return

    def remove_cards(self):
        for card in self.cards:
            card.destroy()
        self.cards = []

    def selected_cards(self):
        return list(filter(lambda card: card.status.get(), self.cards))

    def selected_cards_name(self):
        return [card.name for card in self.selected_cards()]
