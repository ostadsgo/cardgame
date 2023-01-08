import tkinter as tk
from tkinter import ttk


class Card(ttk.Checkbutton):
    """Every card has an image."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.hand = self.master.hand
        self.game = self.master.game
        self.name = ""
        # card variables
        self.status = tk.BooleanVar()
        self.config(variable=self.status, command=self.onclick)

    def set_image(self, imgname):
        # Card image
        photo = tk.PhotoImage(file=imgname)
        self.image = photo
        # display image on checkbutton
        self.config(image=photo)

    def onclick(self):
        selected_cards = self.hand.selected_cards_name()
        if len(selected_cards) == 3:
            score = self.game.calculate_score(selected_cards)
            self.hand.remove()
            self.hand.next()
            self.hand.show()
