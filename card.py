import tkinter as tk
from tkinter import ttk
from os import listdir
from random import choice
from game import Game


class Card(ttk.Checkbutton):
    """Every card has an image."""

    def __init__(self, master, file, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        # card variables
        self.status = tk.BooleanVar()
        self.name = tk.StringVar()
        # Card image
        photo = tk.PhotoImage(file=file)
        self.image = photo
        # Card configuration.
        self.config(
            image=photo, variable=self.status, command=self.onclick
        )  # display image on checkbutton

    def selected_cards(self):
        return list(filter(lambda card: card.status.get(), self.master.cards))

    def onclick(self):
        # get list of cards that user selected(checked card's checkbutton)
        selected_cards = self.selected_cards()
        self.master.game.set_cards(selected_cards)
        # decide user's point based on selected cards.
        if len(selected_cards) == 3:
            score = self.master.game.calculate_score()
            cards_left = len(self.master.all_images)
            info = f"Total Points: {self.master.game.total_score}\nCards Left: {cards_left}"
            self.master.info.set(info)
            # destroy selected cards after playing one hand.
            self.destroy_card()
            # Make new 3 cards
            self.master.make_cards(number=3)

    def destroy_card(self):
        for card in self.selected_cards():
            card.destroy()
            self.master.cards.remove(card)


class CardContainer(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.info = master.info
        # list for store all cards on the CardContainer
        self.cards = []
        # all image's name
        self.all_images = listdir("./images")
        # a Game object to decide players socre after choosing 3 cards.
        self.game = Game()
        # create cards for the first time when CardContiner initilized.
        self.make_cards()

    def choose_image(self):
        """choose a random image."""
        return choice(self.all_images)

    def make_cards(self, number=6):
        for _ in range(number):
            imagename = self.choose_image()
            file = f"images/{imagename}"
            card = Card(self, file)
            card.pack()
            self.cards.append(card)
            card.name = imagename
            self.all_images.remove(imagename)
