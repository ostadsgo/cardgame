import tkinter as tk
from tkinter import ttk


class Card(ttk.Checkbutton):
    """Every card has an image."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
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
        selected_cards = self.master.selected_cards_name()
        if len(selected_cards) == 3:
            score = self.master.game.calculate_score(selected_cards)
            self.master.remove_cards()
            self.master.play()
