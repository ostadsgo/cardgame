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
        self.deck = master
        self.hands = []
        self.hand = []  # current hand

    def cardnum(self, inp):
        """Return card number based on user response `inp`"""
        handnum = inp // self.HAND_SIZE
        self.cardnum = handnum * self.HAND_SIZE
        return self.cardnum

    def make(self, cards):
        self.hands = [cards[index - 6 : index] for index in range(6, len(cards) + 1, 6)]
        return self.hands

    def selected_cards(self):
        return list(filter(lambda card: card.status.get(), self.hand))

    def selected_cards_name(self):
        return [card.name for card in self.selected_cards()]

    def next(self):
        # if hands is not empty
        if self.hands:
            self.hand = self.hands.pop(0)
            return self.hand
        msgbox.showinfo("No Card", "There is not card; game is finished.")
        self.deck.start_menu()

    def show(self):
        for card in self.hand:
            card.pack(expand=True, fill=tk.BOTH)

    def remove(self):
        for card in self.hand:
            card.destroy()


class Deck(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.hand = Hand(self)
        self.game = Game()
        # Make sure user request card number is multiple of 6
        self.input = self.master.input.get_input()
        self.cardnum = self.hand.cardnum(self.input)
        # update score info
        self.info = self.master.info
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

    def show(self):
        self.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.hand.next()
        self.hand.show()

    def update_score(self):
        self.info.set_info(self.game.total_score())

    def start_menu(self):
        """Back to main menu"""
        self.pack_forget()
        self.master.start_show()
