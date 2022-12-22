import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from os import listdir
from random import choice, shuffle, sample
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
        # display image on checkbutton
        self.config(image=photo, variable=self.status, command=self.onclick)

    def selected_cards(self):
        """Filter the cards that selected."""
        return list(filter(lambda card: card.status.get(), self.master.cards))

    def onclick(self):
        # get list of cards that user selected(checked card's checkbutton)
        selected_cards = self.selected_cards()
        name_of_selected_cards = [card.name for card in selected_cards]
        # decide user's point based on selected cards.
        if len(selected_cards) == 3:
            hand_score = self.master.game.calculate_score(name_of_selected_cards)
            self.update_info()
            # destroy selected cards after playing one hand.
            self.destroy_card()
            # Make new 3 cards
            self.master.make_card(number=3)

    def update_info(self):
        cards_left = len(self.master.all_images)
        total_score = self.master.game.total_score()
        self.master.info.set(f"Total Score: {total_score}  Cards Left: {cards_left}")

    def destroy_card(self):
        for card in self.selected_cards():
            card.destroy()
            self.master.cards.remove(card)


class CardContainer(ttk.Frame):
    # Cards number in a hand
    HAND_SIZE = 6

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.info = self.master.info
        self.highest_chance = self.master.highest.get()
        self.user_response = self.master.cards_number.get()
        self.hands_number = self.user_response // self.HAND_SIZE
        self.cards_number = self.hands_number * self.HAND_SIZE
        # list for store all cards on the CardContainer
        self.cards = []
        # all image's name
        self.all_images = listdir("./images")
        # name of iamges
        self.images = self.all_images[: self.cards_number]
        shuffle(self.images)
        # a Game object to decide players socre after choosing 3 cards.
        self.game = Game()
        # add info label
        self.info.set(f"Total Score: 0  Cards Left: {len(self.images)}")
        # play
        self.play()

    def play(self):
        """Check if user desired to play with highest changes to win."""
        if self.highest_chance:
            hands = self.hands(self.images, 3)
            hands_score = self.game.hands_score(hands)
            highest_scored = self.game.sort_hand(hands_score)
            print(highest_scored)

    def hands(self, images, size=6):
        return [
            self.images[index - size : index]
            for index in range(size, self.cards_number + 1, size)
        ]

    def create_card(self, image):
        file = f"images/{image}"
        card = Card(self, file)
        card.pack(expand=True, fill=tk.BOTH)
        self.cards.append(card)
        card.name = image
        self.images.remove(image)

    def create_cards(self, images, size=6):
        """Create a hand of cards."""
        for image in images:
            self.create_card(image)

    def remove(self, cards):
        """Remove all cards on the CardContainer."""
        for card in cards:
            card.destroy()
