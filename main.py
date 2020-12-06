from tkinter import *
import GaloisField as gf


class GUI(Frame):

    def __init__(self):
        super().__init__()
        self.inputType = StringVar()
        self.polynomial2_entry = Entry()
        self.operation = StringVar()
        self.polynomial1 = StringVar()
        self.polynomial2 = StringVar()
        self.degree = IntVar()
        self.outputType = StringVar()
        self.result_label = Label()

        self.master.title("Polynomial Arithmetic")
        self.pack(fill=BOTH, expand=True, padx=20, pady=5)

        # Title Frame
        title_frame = Frame(self)
        title_frame.pack(fill=X)

        title_label = Label(title_frame,
                            text="Polynomial Arithmetic Calculator",
                            font=("Arial Bold", 15))
        title_label.pack(padx=10, pady=10)

        # Input Type Frame
        input_type_frame = Frame(self)
        input_type_frame.pack(fill=X)

        input_type_label = Label(input_type_frame, text="Input Type:")
        input_type_label.pack(side=LEFT, padx=5, pady=5)

        binary_input_radiobutton = Radiobutton(input_type_frame,
                                               text="Binary",
                                               variable=self.inputType,
                                               value="binary")
        binary_input_radiobutton.pack(side=LEFT, padx=5, pady=5)
        binary_input_radiobutton.invoke()

        hex_input_radiobutton = Radiobutton(input_type_frame,
                                            text="Hex", variable=self.inputType,
                                            value="hex")
        hex_input_radiobutton.pack(side=LEFT, padx=5, pady=5)

        # Operation Frame
        operation_frame = Frame(self)
        operation_frame.pack(fill=X)

        operation_label = Label(operation_frame, text="Operation:")
        operation_label.pack(side=LEFT, padx=5, pady=5)

        add_radiobutton = Radiobutton(operation_frame,
                                      text="Add",
                                      variable=self.operation,
                                      value="addition",
                                      command=self.enable_poly2)
        add_radiobutton.pack(side=LEFT, padx=5, pady=5)
        add_radiobutton.invoke()

        subtract_radiobutton = Radiobutton(operation_frame,
                                           text="Subtract",
                                           variable=self.operation,
                                           value="subtraction",
                                           command=self.enable_poly2)
        subtract_radiobutton.pack(side=LEFT, padx=5, pady=5)

        multiply_radiobutton = Radiobutton(operation_frame,
                                           text="Multiply",
                                           variable=self.operation,
                                           value="multiply",
                                           command=self.enable_poly2)
        multiply_radiobutton.pack(side=LEFT, padx=5, pady=5)

        divide_radiobutton = Radiobutton(operation_frame,
                                         text="Divide",
                                         variable=self.operation,
                                         value="divide",
                                         command=self.enable_poly2)
        divide_radiobutton.pack(side=LEFT, padx=5, pady=5)

        invert_radiobutton = Radiobutton(operation_frame,
                                         text="Invert",
                                         variable=self.operation,
                                         value="inverse",
                                         command=self.disable_poly2)
        invert_radiobutton.pack(side=LEFT, padx=5, pady=5)

        reduce_radiobutton = Radiobutton(operation_frame,
                                         text="Reduce",
                                         variable=self.operation,
                                         value="reduction",
                                         command=self.disable_poly2)
        reduce_radiobutton.pack(side=LEFT, padx=5, pady=5)

        # Polynomial 1 Frame
        polynomial1_frame = Frame(self)
        polynomial1_frame.pack(fill=X)

        polynomial1_label = Label(polynomial1_frame, text="Polynomial 1:")
        polynomial1_label.pack(side=LEFT, padx=5, pady=5)

        polynomial1_entry = Entry(polynomial1_frame, textvar=self.polynomial1)
        polynomial1_entry.pack(fill=X, padx=5, pady=5, expand=True)

        # Polynomial 2 Frame
        polynomial2_frame = Frame(self)
        polynomial2_frame.pack(fill=X)

        polynomial2_label = Label(polynomial2_frame, text="Polynomial 2:")
        polynomial2_label.pack(side=LEFT, padx=5, pady=5)

        self.polynomial2_entry = Entry(polynomial2_frame, textvar=self.polynomial2)
        self.polynomial2_entry.pack(fill=X, padx=5, pady=5, expand=True)

        # Degree Frame
        degree_frame = Frame(self)
        degree_frame.pack(pady=10, anchor=W, padx=5)

        degree_label = Label(degree_frame,
                             text="Irreducible Polynomial:",
                             font=("Arial Bold", 10))
        degree_label.pack(pady=(10, 5), anchor=W)

        degree2_radio_button = Radiobutton(degree_frame,
                                           text="Degree 2: x^2 + x^1 + 1",
                                           variable=self.degree,
                                           value=2)
        degree2_radio_button.pack(anchor=W, padx=5)
        degree2_radio_button.invoke()

        degree3_radio_button = Radiobutton(degree_frame,
                                           text="Degree 3: x^3 + x^2 + 1",
                                           variable=self.degree,
                                           value=3)
        degree3_radio_button.pack(anchor=W, padx=5)

        degree4_radio_button = Radiobutton(degree_frame,
                                           text="Degree 4: x^4 + x^3 + 1",
                                           variable=self.degree,
                                           value=4)
        degree4_radio_button.pack(anchor=W, padx=5)

        degree5_radio_button = Radiobutton(degree_frame,
                                           text="Degree 5: x^5 + x^2 + 1",
                                           variable=self.degree,
                                           value=5)
        degree5_radio_button.pack(anchor=W, padx=5)

        degree6_radio_button = Radiobutton(degree_frame,
                                           text="Degree 6: x^6 + x^1 + 1",
                                           variable=self.degree,
                                           value=6)
        degree6_radio_button.pack(anchor=W, padx=5)

        degree7_radio_button = Radiobutton(degree_frame,
                                           text="Degree 7: x^7 + x^1 + 1",
                                           variable=self.degree,
                                           value=7)
        degree7_radio_button.pack(anchor=W, padx=5)

        degree8_radio_button = Radiobutton(degree_frame,
                                           text="Degree 8: x^8 + x^4 + x^3 + x^1 + 1",
                                           variable=self.degree,
                                           value=8)
        degree8_radio_button.pack(anchor=W, padx=5)

        # Output Type Frame
        output_type_frame = Frame(self)
        output_type_frame.pack(fill=X)

        output_type_label = Label(output_type_frame, text="Output Type:")
        output_type_label.pack(side=LEFT, padx=5, pady=5)

        binary_output_radiobutton = Radiobutton(output_type_frame,
                                                text="Binary",
                                                variable=self.outputType,
                                                value="binary")
        binary_output_radiobutton.pack(side=LEFT, padx=5, pady=5)
        binary_output_radiobutton.invoke()

        hex_output_radiobutton = Radiobutton(output_type_frame,
                                             text="Hex",
                                             variable=self.outputType,
                                             value="hex")
        hex_output_radiobutton.pack(side=LEFT, padx=5, pady=5)

        poly_output_radiobutton = Radiobutton(output_type_frame,
                                              text="Show Polynomial",
                                              variable=self.outputType,
                                              value="poly")
        poly_output_radiobutton.pack(side=LEFT, padx=5, pady=5)

        # Result Frame
        result_frame = Frame(self)
        result_frame.pack(pady=10)

        calculate_button = Button(result_frame,
                                  text="Result",
                                  command=self.calculate)
        calculate_button.pack()

        self.result_label = Label(result_frame, text="RESULT APPEARS HERE")
        self.result_label.pack(pady=10)

    def enable_poly2(self):
        self.polynomial2_entry.config(state="normal")

    def disable_poly2(self):
        self.polynomial2_entry.config(state="disabled")

    def calculate(self):
        mod = self.degree.get()
        res = "Error!"
        if self.inputType.get() == "binary":
            if self.polynomial1.get():
                p1 = gf.bin2hex(gf.strbin2bin(self.polynomial1.get()))
            if self.polynomial2.get():
                p2 = gf.bin2hex(gf.strbin2bin(self.polynomial2.get()))
        else:
            p1 = gf.strhex2hex(self.polynomial1.get())
            p2 = gf.strhex2hex(self.polynomial2.get())

        if self.operation.get() == "addition" or self.operation.get() == "subtraction":
            res = gf.Add(p1, p2, mod)
        elif self.operation.get() == "multiply":
            res = gf.Multiplication(p1, p2, mod)
        elif self.operation.get() == "divide":
            res = gf.Division(p1, p2, mod)
        elif self.operation.get() == "inverse":
            res = gf.Invert(p1, mod)
        elif self.operation.get() == "reduction":
            res = gf.moduloreduction(p1, mod)

        if self.outputType.get() == "poly":
            self.result_label.config(text=gf.ShowPolynomial(res))
        elif self.outputType.get() == "binary":
            self.result_label.config(text=gf.hex2bin(res))
        else:
            self.result_label.config(text=res)


def main():
    root = Tk()
    GUI()
    root.mainloop()


if __name__ == '__main__':
    main()
