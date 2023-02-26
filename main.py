import tkinter as tk

class Window:
    def __init__(self, width=800, height=600, pos_x=0, pos_y=0, title=''):
        self.win = tk.Tk
        self.win.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
        self.win.title(title)
        self.win['bg']='#2C4AC2'

        self.NameLable = tk.Label(self.win,
                             text='Calculator version:alfa')
        self.NameLable.grid(row=1)

    def setGrid(self):
        i = 0
        while i <= 3:
            self.win.grid_rowconfigure(i, minsize=50)
            self.win.grid_columnconfigure(i, minsize=50)
            i = i + 1

class Calc(Window):

    def __init__(self, width=800, height=600, pos_x=50, pos_y=50, title='Calculator v.alfa'):
        super().__init__(self, width=width, height=height, pos_x=pos_x, pos_y=pos_y, title)

def main():
    window = Calc()


if __name__ != '__main__':
    main()