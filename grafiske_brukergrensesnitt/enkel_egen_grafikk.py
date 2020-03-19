import tkinter


class EnkelEgenGrafikk:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.tegner = tkinter.Canvas(self.hovedvindu, width=800, height=600)
        self.tegner.pack()

        self.tegner.create_line(50, 300, 300, 100, width=4, dash=(20, 10), fill="green") # x1, y1, x2, y2
        self.tegner.create_rectangle(400, 200, 600, 400, fill="blue", outline="red")
        self.tegner.create_oval(100, 400, 250, 500)
        self.tegner.create_arc(400, 400, 550, 500, start=-90, extent=90, style=tkinter.PIESLICE)
        self.tegner.create_polygon(500, 50, 540, 25, 580, 50, 580, 100, 540, 125, 500, 100, fill="red")
        self.tegner.create_text(75, 15, text="Tester tekst i canvas")

        tkinter.mainloop()


if __name__ == "__main__":
    gui = EnkelEgenGrafikk()
