"""
    Module with GUI intefrace
"""


from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

import numpy as np
from utils import gen_p
from plot import plot_all

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

from numpy import arange, sin, pi



# default_font = tkFont.nametofont("TkDefaultFont")
# default_font.configure(size=48)


class Application(Frame):
    """ Main app class for tk"""
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        # init function with empty data

        self._z = ([],[])
        self._S = ([],[])
        self._p = ([],[])

        self.x = ([],[])

        # Base size
        normal_width = 1920
        normal_height = 1080

        # Get screen size
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Get percentage of screen size from Base size
        percentage_width = screen_width / (normal_width / 100)
        percentage_height = screen_height / (normal_height / 100)

        # Make a scaling factor, this is bases on average percentage from
        # width and height.
        scale_factor = ((percentage_width + percentage_height) / 2) / 100

        # Set the fontsize based on scale_factor,
        # if the fontsize is less than minimum_size
        # it is set to the minimum size
        fontsize = int(14 * scale_factor)
        minimum_size = 8
        if fontsize < minimum_size:
            fontsize = minimum_size

        self.master.option_add("*Font", "{}".format(fontsize))
        style = Style()
        style.configure("TButton", font="{}".format(14))
        self.createWidgets()

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value
        self.update_plot()

    @property
    def S(self):
        return self._S

    @S.setter
    def S(self, value):
        self._S = value
        self.update_plot()

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, value):
        self._p = value
        self.update_plot()

    def createWidgets(self):
        Label(self, text="z(t)").grid(row=0, column=0)
        Button(self, text="open file", command=lambda: self.read_file("z")).grid(row=0, column=1)

        Label(self, text="S(t)").grid(row=1, column=0)
        Button(self, text="open file", command=lambda: self.read_file("S")).grid(row=1, column=1)

        Label(self, text="p(w)").grid(row=2, column=0)
        Button(self, text="open file", command=lambda: self.read_file("p")).grid(row=2, column=1)

        Label(self, text="p(w) = wA(B - w)").grid(row=3, column=0, columnspan=2, sticky=W)

        Label(self, text="A=").grid(row=4, column=0, sticky=E)
        self.a = Entry(self)
        self.a.grid(row=4, column=1)
        self.a.config(width=10)

        Label(self, text="B=").grid(row=5, column=0, sticky=E)
        self.b = Entry(self)
        self.b.grid(row=5, column=1)
        self.b.config(width=10)

        Button(self, text="generate p(w)", command=self.gen_p).grid(row=6, column=0, columnspan=2, sticky=W)

        Button(self, text="save p(w)", command=lambda: self.savetofile(self.p)).grid(row=7, column=0, columnspan=2, sticky=W)



        self.figure = plt.figure()

        self.canvas = FigureCanvasTkAgg(self.figure, self)

        self.canvas.get_tk_widget().grid(row=1, column=3, rowspan=6, padx=5)
        toolbar_frame = Frame(self)
        toolbar_frame.grid(row=0,column=3, sticky=W, padx=5)
        NavigationToolbar2TkAgg(self.canvas, toolbar_frame)

        self.update_plot()

    def open_file(self):
        """
        Open file with dialog
        """
        ftypes = [('CSV', '*.csv'), ('All files', '*')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            return fl

    def savetofile(self, values):
        """
        Open file with dialog
        """
        ftypes = [('CSV', '*.csv'), ('All files', '*')]
        dlg = filedialog.SaveAs(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            try:
                np.savetxt(fl, values, delimiter=',')
            except:
                messagebox.showerror("Error", "Ошибка сохранения файла")


    def read_file(self, attr):
        fl = self.open_file()
        if fl:
            try:
                setattr(self, attr, np.loadtxt(fl, delimiter=','))
                print(getattr(self, attr))
            except:
                messagebox.showerror("Error", "Ошибка открытия файла")

    def gen_p(self):
        A = int(self.a.get())
        B = int(self.b.get())
        self.p = gen_p(A, B, -100, 100)
        print(self.p)

    def update_plot(self):
        plt.clf()
        plot_all(self.z, self.x, self.S, self.p)
        self.canvas.draw()

def main():
    app = Application()
    app.master.title("My Do-Nothing Application")
    app.mainloop()

if __name__ == "__main__":
    main()
