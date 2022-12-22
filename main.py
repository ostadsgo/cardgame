import tkinter as tk
from tkinter import ttk

from deck import Deck


# Main frame: everything goes here.
class MainFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Style widget
        self.style = ttk.Style()
        # self.style.configure("StartPage.TFrame", background="#f2f0cb")
        # start_page frame
        self.start_page = ttk.Frame(self, relief=tk.GROOVE, padding=(40, 20))
        self.start_page.pack(expand=True, fill=tk.BOTH)
        # Variable to get number of cards from user
        self.cards_number = tk.IntVar()
        self.cards_number.set(22)
        self.info = tk.StringVar()
        self.highest = tk.BooleanVar()
        ttk.Label(self.master, textvariable=self.info).pack()
        # show start page to get response from user
        self.show_start_page()

    def show_start_page(self):
        # Widgets for start page
        ttk.Label(self.start_page, text="Enter number of cards between 1 to 81:").pack()
        ttk.Entry(self.start_page, textvariable=self.cards_number)
        ttk.Button(self.start_page, text="Play", command=self.play)
        ttk.Button(
            self.start_page, text="Play With Computer", command=self.play_computer
        )
        ttk.Checkbutton(self.start_page, text="Highest chance", variable=self.highest)

        # pack all widgets defined on the start_page frame.
        for child in self.start_page.winfo_children():
            child.pack(padx=10, pady=5, expand=True, fill=tk.BOTH)

    def hide_start_page(self):
        self.start_page.pack_forget()

    def play(self):
        self.hide_start_page()
        deck = Deck(self, relief=tk.SOLID, padding=(40, 20))
        deck.pack()

    def play_computer(self):
        pass


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Card Game")
        mainframe = MainFrame(self, padding=(40, 20))
        mainframe.pack(expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
