"""
    Module with GUI intefrace
"""

from tkinter import filedialog
from tkinter import *
import numpy as np
from .utils import gen_p
from .plot import plot_all

root = Tk()

class Application(Frame):
    """ Main app class for tk"""
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        Label(self, text="z(t)").grid(row=0)
        Label(self, text="x(t)").grid(row=2)
        Label(self, text="S(t)").grid(row=4)
        self.z_butt = Button(self, text="open file", command=self.openZ).grid(row=0, column=1)
        self.x_butt = Button(self, text="open file", command=self.openX).grid(row=2, column=1)
        self.S_butt = Button(self, text="open file", command=self.openS).grid(row=4, column=1)
        Label(self, text="p(w) = wA(B - w)").grid(row=6)

        self.a = Entry(self)
        self.b = Entry(self)
        Label(self, text="A").grid(row=7, column=0)
        Label(self, text="B").grid(row=7, column=2)
        self.p_butt = Button(self, text="generate p(w)", command=self.genP).grid(row=8, column=1)
        self.pfile_butt = Button(self, text="open file", command=self.openP).grid(row=8, column=3)
        self.a.grid(row=7, column=1)
        self.b.grid(row=7, column=3)

        self.plot_butt = Button(self, text="Plot all", command=self.plot_all).grid(row=11, column=1)

    def openFile(self):
        """
        Open file with dialog
        """
        ftypes = [('CSV', '*.csv'), ('All files', '*')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            return fl
        else:
            print("error")

    def openZ(self):
        fl = self.openFile()
        if fl:
            self.z = np.loadtxt(fl, delimiter=',')
            print(self.z)

    def openX(self):
        fl = self.openFile()
        if fl:
            self.x = np.loadtxt(fl, delimiter=',')
            print(self.x)

    def openS(self):
        fl = self.openFile()
        if fl:
            self.S = np.loadtxt(fl, delimiter=',')
            print(self.S)

    def openP(self):
        fl = self.openFile()
        if fl:
            self.p = np.loadtxt(fl, delimiter=',')
            print(self.p)

    def genP(self):
        A = int(self.a.get())
        B = int(self.b.get())
        self.p = gen_p(A, B, -100, 100)
        print(self.p)

    def plot_all(self):
        plot_all(self.z, self.x, self.S, self.p)

def main():
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
