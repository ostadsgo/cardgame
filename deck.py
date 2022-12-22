import tkinter as tk

from os import listdir
from tkinter import ttk
from random import shuffle

from card import Card
from game import Game


class Deck(ttk.Frame):
    # Cards number in a hand
    HAND_SIZE = 6

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        # tkinter variables
        self.info = self.master.info
        self.highest_chance = self.master.highest.get()
        self.user_response = self.master.cards_number.get()
        # calculate number of cards; make number of cards be multiple of 3
        self.hands_number = self.user_response // self.HAND_SIZE
        self.cards_number = self.hands_number * self.HAND_SIZE
        # list for store all cards on the CardContainer
        self.cards = []
        self.hands = []
        # all image's name
        self.all_images = listdir("./images")
        shuffle(self.all_images)
        # truncate all_images to the number user requested
        self.images = self.all_images[: self.cards_number]
        # a Game object to decide players socre after choosing 3 cards.
        self.game = Game()
        # play
        # self.play()

    def play(self):
        # set data to info variable (update label text)
        self.info.set(f"Total Score: 0  Cards Left: {len(self.images)}")

        """Check if user desired to play with highest changes to win."""
        # highest chance to win
        if self.highest_chance:
            hands = self.make_hands(self.images, 3)
            hands_score = self.game.hands_score(hands)
            highest_scored = self.game.sort_hand(hands_score)
            hands = [item["hand"] for item in highest_scored]
            images = [card for hand in hands for card in hand]
            hands = self.make_hands(images, 6)
            for hand in hands:
                self.create_cards(hand)
                print(hands)
            return

        # normal play
        hands = self.make_hands(self.images, 6)
        first_hand, *rest_of_hands = hands
        # print(first_hand, "\n", rest_of_hands)
        self.create_cards(first_hand)

    def make_hands(self, images, size=6):
        return [
            self.images[index - size : index]
            for index in range(size, self.cards_number + 1, size)
        ]

    def create_cards(self, hand):
        """Create hand of cards."""
        for image in hand:
            file = f"images/{image}"
            card = Card(self, file, image)
            card.pack(expand=True, fill=tk.BOTH)
            self.cards.append(card)

    def next_hand(self):
        """Create a hand of cards."""
        for hand in self.hands:
            self.create_cards(hand)
        # delete list of images that used
        self.hands.pop(0)

    def remove_cards(self, cards):
        for card in cards:
            card.destroy()

    def selected_cards(self):
        return list(filter(lambda card: card.status.get(), self.cards))

    def name_of_selected_cards(self):
        return [card.name for card in self.selected_cards]
