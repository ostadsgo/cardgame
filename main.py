import tkinter as tk
import tkinter.ttk as ttk

from deck import Deck


class InfoFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.info = tk.StringVar()
        self._widgets(self)

    def _widgets(self):
        ttk.Label(self, textvariable=self.info)
        for child in self.winfo_children():
            child.pack(expand=True, fill=tk.BOTH)

    def get_info(self):
        return self.info.get()

    def set_info(self, text):
        self.info.set(text)


class InputFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.cardnum = tk.IntVar()
        self._widgets()

    def _widgets(self):
        ttk.Label(self, text="Enter card number: 1 to 81")
        ttk.Entry(self, textvariable=self.cardnum)
        for child in self.winfo_children():
            child.pack(expand=True, fill=tk.BOTH)

    def get_cardnum(self):
        return self.cardnum

    def set_cardnum(self, value):
        if value > 6:
            self.cardnum = value
            return self.cardnum
        raise ValueError("Card number must be grather or equal to 6.")


class OptionFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.option = tk.StringVar()
        self._widgets()

    def _widgets(self):
        ttk.Radiobutton(self, text="Single play", variable=self.option, value="single")
        ttk.Radiobutton(self, text="Double play", variable=self.option, value="double")
        ttk.Radiobutton(
            self, text="Computer play", variable=self.option, value="computer"
        )
        ttk.Radiobutton(
            self, text="Highest Chance", variable=self.option, value="highest"
        )
        for child in self.winfo_children():
            child.pack(expand=True, fill=tk.BOTH)

    def get_option(self):
        return self.option.get()


class ActionFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._widgets()

    def _widgets(self):
        ttk.Button(self, text="Play", command=self.play)
        for child in self.winfo_children():
            child.pack(expand=True, fill=tk.BOTH)

    def play(self):
        pass


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
        # top part: input from user
        inpt = InputFrame(self)

        # center part
        option = OptionFrame(self)

        # Bottom part
        action = ActionFrame(self)

        for child in self.winfo_children():
            child.pack(expand=True, fill=tk.BOTH, pady=10)


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Card Game")
        mainframe = MainFrame(self, padding=(40, 20))
        mainframe.pack(expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
