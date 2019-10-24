import tkinter

expression = ""

class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор")
        self.main_frame = tkinter.Frame(master=self, bg="white", bd=2)
        self.equation = tkinter.StringVar()
        self.expression_field = tkinter.Entry(master=self.main_frame, textvariable=self.equation)
        self.a_entry = tkinter.Entry(master=self.main_frame, width=5, justify=tkinter.CENTER)
        self.button1 = tkinter.Button(master=self.main_frame, text=' 1 ', fg='black', bg='white', command=lambda: self.press(1), height=1, width=7)
        self.button2 = tkinter.Button(master=self.main_frame, text=' 2 ', fg='black', bg='white', command=lambda: self.press(2), height=1, width=7)
        self.button3 = tkinter.Button(master=self.main_frame, text=' 3 ', fg='black', bg='white', command=lambda: self.press(3), height=1, width=7)
        self.button4 = tkinter.Button(master=self.main_frame, text=' 4 ', fg='black', bg='white', command=lambda: self.press(4), height=1, width=7)
        self.button5 = tkinter.Button(master=self.main_frame, text=' 5 ', fg='black', bg='white', command=lambda: self.press(5), height=1, width=7)
        self.button6 = tkinter.Button(master=self.main_frame, text=' 6 ', fg='black', bg='white', command=lambda: self.press(6), height=1, width=7)
        self.button7 = tkinter.Button(master=self.main_frame, text=' 7 ', fg='black', bg='white', command=lambda: self.press(7), height=1, width=7)
        self.button8 = tkinter.Button(master=self.main_frame, text=' 8 ', fg='black', bg='white', command=lambda: self.press(8), height=1, width=7)
        self.button9 = tkinter.Button(master=self.main_frame, text=' 9 ', fg='black', bg='white', command=lambda: self.press(9), height=1, width=7)
        self.button0 = tkinter.Button(master=self.main_frame, text=' 0 ', fg='black', bg='white', command=lambda: self.press(0), height=1, width=7)
        self.plus = tkinter.Button(master=self.main_frame, text=' + ', fg='black', bg='white', command=lambda: self.press('+'), height=1, width=7)
        self.minus = tkinter.Button(master=self.main_frame, text=' - ', fg='black', bg='white', command=lambda: self.press('-'), height=1, width=7)
        self.multiply = tkinter.Button(master=self.main_frame, text=' * ', fg='black', bg='white', command=lambda: self.press('*'), height=1, width=7)
        self.divide = tkinter.Button(master=self.main_frame, text=' / ', fg='black', bg='white', command=lambda: self.press('/'), height=1, width=7)
        self.equal = tkinter.Button(master=self.main_frame, text=' = ', fg='black', bg='white', command=self.equalpress, height=1, width=7)
        self.clear = tkinter.Button(master=self.main_frame, text='Clear', fg='black', bg='white', command=self.clear, height=1, width=7)

    def draw_interface(self):
        self.main_frame.grid(column=0, row=0, sticky="WESN")
        self.expression_field.grid(row=0, columnspan=4)
        self.clear.grid(row=5, column='1')
        self.button1.grid(row=2, column=0)
        self.button2.grid(row=2, column=1)
        self.button3.grid(row=2, column=2)
        self.button4.grid(row=3, column=0)
        self.button5.grid(row=3, column=1)
        self.button6.grid(row=3, column=2)
        self.button7.grid(row=4, column=0)
        self.button8.grid(row=4, column=1)
        self.button9.grid(row=4, column=2)
        self.button0.grid(row=5, column=0)
        self.plus.grid(row=2, column=3)
        self.minus.grid(row=3, column=3)
        self.multiply.grid(row=4, column=3)
        self.divide.grid(row=5, column=3)
        self.equal.grid(row=5, column=2)


    def press(self, num):
        global expression
        expression = expression + str(num)
        self.equation.set(expression)

    def equalpress(self):
        try:
            global expression
            total = str(eval(expression))
            self.equation.set(total)
            expression = ""
        except:
            self.equation.set(" error ")
            expression = ""

    def clear(self):
            global expression
            expression = ""
            self.equation.set("")

    def center(self):
            self.update_idletasks()
            width = self.winfo_screenwidth()
            height = self.winfo_screenheight()
            size = tuple(int(i) for i in self.geometry().split('+')[0].split('x'))
            x = width / 2 - size[0] / 2
            y = height / 2 - size[1] / 2
            self.geometry("%dx%d+%d+%d" % (size + (x, y)))

if __name__ == '__main__':
    app = Application()
    app.draw_interface()
    app.center()
    app.resizable(False, False)
    app.mainloop()
