import tkinter as tk
from tkinter import ttk


class Card(ttk.Checkbutton):
    """Every card has an image."""

    def __init__(self, master, file, name, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        # card variables
        self.status = tk.BooleanVar()
        self.name = name
        # Card image
        photo = tk.PhotoImage(file=file)
        self.image = photo
        # display image on checkbutton
        self.config(image=photo, variable=self.status, command=self.onclick)

    def onclick(self):
        # get list of cards that user selected(checked card's checkbutton)
        selected_cards = self.master.selected_cards()
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
