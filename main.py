import tkinter as tk
from functools import partial

class Window:
    def __init__(self, width, height, pos_x, pos_y, title):
        self.win = tk.Tk()
        self.win.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
        self.win.title(title)
        self.win['bg']='#2C4AC2'

        self.NameLable = tk.Label(self.win,
                             text='Calculator version:alfa')
        self.NameLable.grid(row=1)

        self.setGrid()

    def setGrid(self):
        i = 0
        while i <= 3:
            self.win.grid_rowconfigure(i, minsize=50)
            self.win.grid_columnconfigure(i, minsize=50)
            i = i + 1

class Calc(Window):

    def __init__(self, width=410, height=440, pos_x=50, pos_y=50, title='Calculator v.release 1.0'):
        super().__init__(width=width, height=height, pos_x=pos_x, pos_y=pos_y, title=title)
        self.addElements()

    def addSytmbol(self, name):
        enter_val = self.enter.get()

        if enter_val == '=':
            enter_val = eval(enter_val)
        else:
            self.enter.insert(0, enter_val + name)

    def addlablel(self):
        pass

    def addButton(self, name, row, column):
        btn = tk.Button(self.win,
                        text=name,
                        width=10,
                        height=4,
                        command=partial(self.addSymbol, name))
        btn.grid(row=row,
                 column=column,
                 padx=10,
                 pady=10,
                 bd=5)

        return btn

    def addEntry(self, row, column):
        ent = tk.Entry(self.win,
                       justify='left')
        ent.grid(row=row,
                 column=column,
                 padx=10,
                 pady=10,
                 stick='w')

        return ent

    def addElements(self):
        self.enter = self.addEntry(0, 0)

        button_names = [['1', '2', '3', '+']
                        ['4', '5', '6', '-']
                        ['7', '8', '9', '*']
                        [' ', '0', '.', '/']]

        btn = []

        for row_index, buttons in enumerate(button_names):
            for col_index, button in enumerate(buttons):
                btn = self.addButton(button,
                                     row_index,
                                     col_index)

def main():
    C = Calc()
    C.win.mainloop()

if __name__ == '__main__':
    main()