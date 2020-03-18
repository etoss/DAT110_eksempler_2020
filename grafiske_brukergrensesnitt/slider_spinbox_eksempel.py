import tkinter


class Demo:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.meny = tkinter.Spinbox(self.hovedvindu,
                                    values=("En", "To", "Tre"))
        self.meny.pack()
        self.slider = tkinter.Scale(self.hovedvindu, from_=0, to=100, orient=tkinter.HORIZONTAL)
        self.slider.pack()
        tkinter.mainloop()


if __name__ == "__main__":
    gui = Demo()
