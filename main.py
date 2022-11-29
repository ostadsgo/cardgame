import tkinter as tk
from tkinter import ttk

from card import CardContainer, Card


class MainFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.info = tk.StringVar()
        self.info.set("Total Points: 0\nCards Left: 81")
        # Cards
        card_container = CardContainer(self)
        card_container.pack(expand=True, fill=tk.BOTH)

        info = ttk.Label(self, textvariable=self.info)
        info.pack(expand=True, fill=tk.BOTH)


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Card Game")
        # Create mainframe
        mainframe = MainFrame(self, padding=(10, 20))
        mainframe.pack(expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
