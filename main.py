import tkinter as tk
import tkinter.ttk as ttk

from deck import Deck


class InputFrame(ttk.Frmae):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.cardnum = tk.IntVar()
        pack_cfg = {"expand": True, "fill": tk.BOTH}
        ttk.Label(self, text="Enter card number: 1 to 81").pack(**pack_cfg)
        ttk.Entry(self, textvariable=self.cardnum).pack(**pack_cfg)

    def get_cardnum(self):
        return self.cardnum

    def set_cardnum(self, value):
        if value > 6:
            self.cardnum = value
            return self.cardnum
        raise ValueError("Card number must be grather or equal to 6.")


class Option(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class Action(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class StartFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.info = self.master.info
        self.card_number = tk.IntVar()
        self.highest = tk.BooleanVar()
        self.card_number.set(12)
        self._widgets()

    def _widgets(self):
        ttk.Label(self, text="Enter number of cards between 1 to 81:").pack()
        ttk.Entry(self, textvariable=self.card_number)
        ttk.Button(self, text="Play", command=self.play)
        ttk.Button(self, text="Play With Computer", command=self.play_computer)
        ttk.Checkbutton(self, text="Highest chance", variable=self.highest)
        for child in self.winfo_children():
            child.pack(padx=10, pady=5, expand=True, fill=tk.BOTH)

    def show(self):
        self.pack(expand=True, fill=tk.BOTH)

    def hide(self):
        self.pack_forget()

    def play(self):
        self.hide()
        deck = Deck(self.master, relief=tk.SOLID, padding=(40, 20))
        deck.pack(expand=True, fill=tk.BOTH)

    def play_computer(self):
        pass


# Main frame: everything goes here.
class MainFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.info = tk.StringVar()
        ttk.Label(self, textvariable=self.info).pack(expand=True, fill=tk.BOTH)
        start_page = StartFrame(self)
        self.highest = start_page.highest
        self.card_number = start_page.card_number
        start_page.show()


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Card Game")
        mainframe = MainFrame(self, padding=(40, 20))
        mainframe.pack(expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
