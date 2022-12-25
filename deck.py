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

    def cardnum(self, inp):
        """Return card number based on user response `inp`"""
        handnum = inp // self.HAND_SIZE
        self.cardnum = handnum * self.HAND_SIZE
        return self.cardnum

    def make(self, cards):
        return [cards[index - 6 : index] for index in range(6, len(cards) + 1, 6)]

    def selected_cards(self):
        return list(filter(lambda card: card.status.get(), self.cards))

    def selected_cards_name(self):
        return [card.name for card in self.selected_cards()]

    def next_hand(self):
        if self.hands:
            hand = self.hands.pop(0)
            self.show_hand(hand)

    def show_hand(self, hand):
        for card in hand:
            card.pack(expand=True, fill=tk.BOTH)


class Deck(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.hand = Hand(self)
        # Make sure user request card number is multiple of 6
        self.input = self.master.input.get_input()
        self.cardnum = self.hand.cardnum(self.input)
        # read all images from computer storage
        self.images = listdir("./images")
        shuffle(self.images)
        self.images = self.images[: self.cardnum]
        # Make cards from images
        self.cards = [self.make_card() for _ in range(self.cardnum)]
        self.hands = self.hand.make(self.cards)

    def make_card(self):
        if self.images:
            imgname = f"./images/{self.images.pop(0)}"
            card = Card(self)
            card.set_image(imgname)
        return card


class Deck1(ttk.Frame):
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
