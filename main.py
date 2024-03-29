import os.path
import tkinter as tk
import datetime
import tkinter.filedialog
import tkinter.filedialog
from tkinter import ttk

# -- Screen Size -- #
SCREEN_SIZE = "420x480"
MINI_WINDOW_SIZE = "325x150"

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
}


class MyGUI:

    def file_save_diary(self):
        if os.path.isdir("days") == True:
            pass
        else:
            os.mkdir("days")

        try:
            today = datetime.datetime.now()
            thetext = self.textbox.get("1.0", 'end-1c')
            file = open(f"days/{today.strftime('%d.%m.%Y')}.txt", "x")
            file.write(thetext)
        except:
            self.error_file_save()

        tkinter.filedialog.asksaveasfilename(initialfile='Untitled.txt',
                                             defaultextension=".txt",
                                             filetypes=[("All Files", "*.*"),
                                                        ("Text Documents", ".txt")])

    def openFile(self):
        self.file = tkinter.filedialog.askopenfilename(defaultextension=".txt",
                                                       filetypes=[("All Files", "*.*"),
                                                                  ("Text Documents", "*.txt")])

        if self.file == "":
            self.file = None
        else:
            self.root.title(os.path.basename(self.file) + " - PyPad")
            self.textbox.delete("1.0", 'end-1c')

            file = open(self.file, "r")
            self.textbox.insert(1.0, file.read())
            file.close()

    def file_save(self):
        if self.file is None:
            self.file = tkinter.filedialog.asksaveasfilename(initialfile='Untitled.txt',
                                                             defaultextension=".txt",
                                                             filetypes=[("All Files", "*.*"),
                                                                        ("Text Documents", ".txt")])

            if self.file == "":
                self.file = None
            else:
                file = open(self.file, "w")
                file.write(self.textbox.get("1.0", 'end-1c'))
                file.close()
                # window title
                self.root.title(os.path.basename(self.file) + " - PyPad")

        else:
            file = open(self.file, "w")
            file.write(self.textbox.get("1.0", 'end-1c'))
            file.close()

    def error_file_save(self):
        print("Error, File already exsists")

    def exit(self):
        self.root.destroy()
        quit()

    def search(self):
        text = self.textbox.get("1.0", 'end-1c')
        textsearch = None
        # text.find(f"{textsearch}")

    def change_color_on_hover(self, event):
        event.widget.config(background=BUTTON_RED_2, foreground=BLACK)

    def restore_color_on_hover(self, event):
        event.widget.config(background=BLACK, foreground=BRIGHTBRIGHT_WHITE)

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(SCREEN_SIZE)
        self.root.title("PyPad")
        # self.root.resizable(False, False)
        self.root.configure(background=BACKGROUND_COLOR)
        # self.icon = tk.PhotoImage(file="assets/icon.png")
        # self.root.iconphoto(False, self.icon)

        self.file = None
        file = None

        # -- MenuButtons -- #
        self.menubuttonframe = tk.Frame(self.root, background=BACKGROUND_COLOR)
        self.menubuttonframe.pack(padx=3, pady=3, anchor=tk.W)

        self.menubutton_file = tk.Button(self.menubuttonframe, text="File", command=self.file_save, width=5,
                                         **button_style)
        self.menubutton_file.pack(padx=1, side=tk.LEFT)
        self.menubutton_file.bind("<Enter>", self.change_color_on_hover)
        self.menubutton_file.bind("<Leave>", self.restore_color_on_hover)

        self.menubutton_edit = tk.Button(self.menubuttonframe, text="Edit", command=self.exit, width=5,
                                         **button_style)
        self.menubutton_edit.pack(padx=1, side=tk.LEFT)
        self.menubutton_edit.bind("<Enter>", self.change_color_on_hover)
        self.menubutton_edit.bind("<Leave>", self.restore_color_on_hover)

        self.menubutton_search = tk.Button(self.menubuttonframe, text="Search", command=self.exit, width=7,
                                           **button_style)
        self.menubutton_search.pack(padx=1, side=tk.LEFT)
        self.menubutton_search.bind("<Enter>", self.change_color_on_hover)
        self.menubutton_search.bind("<Leave>", self.restore_color_on_hover)

        self.menubutton_diary = tk.Button(self.menubuttonframe, text="Diary", command=self.file_save_diary, width=7,
                                          **button_style)
        self.menubutton_diary.pack(padx=1, side=tk.LEFT)
        self.menubutton_diary.bind("<Enter>", self.change_color_on_hover)
        self.menubutton_diary.bind("<Leave>", self.restore_color_on_hover)

        self.menubutton_quit = tk.Button(self.menubuttonframe, text="Quit", command=self.exit, width=5,
                                         **button_style)
        self.menubutton_quit.pack(padx=1, side=tk.LEFT)
        self.menubutton_quit.bind("<Enter>", self.change_color_on_hover)
        self.menubutton_quit.bind("<Leave>", self.restore_color_on_hover)

        # -- TextBox -- #
        self.textbox = tk.Text(self.root, width=3000, height=3000, bg=BLACK, foreground=FOREGROUND_COLOR,
                               font=NormalFont, borderwidth=0, border=0)
        self.textbox.pack()

        # -- MainLoop -- #
        self.root.mainloop()


MyGUI()
