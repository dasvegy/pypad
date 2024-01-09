import tkinter as tk
from tkinter import ttk

# -- Screen Size -- #
SCREEN_SIZE = "420x480"

# -- Fonts -- #
TitleFont = ("JetBrains Mono", 14)
NormalFont = ("JetBrains Mono", 12)
SmallFont = ("JetBrains Mono", 10)

# -- Colors -- #
BACKGROUND_COLOR = "#1a1a19"
FOREGROUND_COLOR = "#d1d1d1"

# -Normal- #
BLACK = '#333332'
RED = '#ff968c'
GREEN = '#61957f'
YELLOW = '#ffc591'
BLUE = '#8db4d4'
MAGENTA = '#de9bc8'
CYAN = '#7bb099'
WHITE = '#d1d1d1'
BUTTON_RED = '#bd493e'
BUTTON_RED_2 = '#c75c52'

# -Bright- #
BRIGHT_BLACK = '#4c4c4b'
BRIGHT_RED = '#ffafa5'
BRIGHT_GREEN = '#7aae98'
BRIGHT_YELLOW = '#ffdeaa'
BRIGHT_BLUE = '#a6cded'
BRIGHT_MAGENTA = '#f7b4e1'
BRIGHT_CYAN = '#94c9b2'
BRIGHT_WHITE = '#eaeaea'
BRIGHTBRIGHT_WHITE = '#f9f9f9'

button_style = {
    'font': NormalFont,
    'background': BLACK,
    'foreground': BRIGHTBRIGHT_WHITE,
    'activebackground': RED,
    'highlightthickness': 0,
    'border': 0,
    'width': 5
}


class MyGUI:
    def file_safe(self):
        pass

    def exit(self):
        quit()

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(SCREEN_SIZE)
        self.root.title("vegy's YT Downloader")
        self.root.resizable(False, False)
        self.root.configure(background=BACKGROUND_COLOR)

        self.menubuttonframe = tk.Frame(self.root, background=BACKGROUND_COLOR)
        self.menubuttonframe.pack(padx=5, pady=5)

        self.menubutton_file = tk.Button(self.menubuttonframe, text="File", command=self.file_safe, **button_style)
        self.menubutton_file.pack(padx=1, side=tk.LEFT)

        self.menubutton_edit = tk.Button(self.menubuttonframe, text="Edit", command=self.file_safe, **button_style)
        self.menubutton_edit.pack(padx=1, side=tk.LEFT)

        self.menubutton_quit = tk.Button(self.menubuttonframe, text="Quit", command=self.exit, **button_style)
        self.menubutton_quit.pack(padx=1, side=tk.RIGHT)

        self.menubutton_search = tk.Button(self.menubuttonframe, text="Search", command=self.file_safe, **button_style)
        self.menubutton_search.pack(padx=1, side=tk.RIGHT)

        self.textbox = tk.Text(self.root, width=3000, height=3000, bg=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR, font=NormalFont)
        self.textbox.pack()

        # -- MainLoop -- #
        self.root.mainloop()


MyGUI()
