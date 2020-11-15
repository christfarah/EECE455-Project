from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, Y, W
from tkinter.ttk import Frame, Label, Entry, Radiobutton, Button


class GUI(Frame):

    #These Values are tied to their corresponding widgets. They react to changes in input.
    inputType = "binary" #choices: binary, hex
    outputType = "binary" #choices: binary, hex
    degree = "degree2" #choices: degree2...degree8
    operation = "reduction" #choices: reduction, addition, subtraction, multiplication, division, inverse
    polynomial1 = ""
    polynomial2 = ""

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        self.master.title("Polynomial Arithmetic")
        self.pack(fill=BOTH, expand=True, padx = 20, pady = 5)

        #Title Frame
        titleFrame = Frame(self)
        titleFrame.pack(fill=X)

        titleLabel = Label(titleFrame, text="Polynomial Arithmetic Calculator", font=("Arial Bold", 15))
        titleLabel.pack(padx=10, pady=10)

        #Input Type Frane
        inputTypeFrame = Frame(self)
        inputTypeFrame.pack(fill=X)

        inputTypeLabel = Label(inputTypeFrame, text="Input Type:")
        inputTypeLabel.pack(side=LEFT, padx = 5, pady = 5)

        binaryInputRadiobutton = Radiobutton(inputTypeFrame, text="Binary", variable=self.inputType, value="binary")
        binaryInputRadiobutton.pack(side=LEFT, padx = 5, pady = 5)
        binaryInputRadiobutton.invoke()
        
        hexInputRadiobutton = Radiobutton(inputTypeFrame, text="Hex", variable=self.inputType, value="hex")
        hexInputRadiobutton.pack(side=LEFT, padx = 5, pady = 5)

        #Polynomial 1 Frame
        polynomial1Frame = Frame(self)
        polynomial1Frame.pack(fill=X)

        polynomial1Label = Label(polynomial1Frame, text="Polynomial 1:")
        polynomial1Label.pack(side=LEFT, padx=5, pady=5)

        polynomial1Entry = Entry(polynomial1Frame, textvar = self.polynomial1)
        polynomial1Entry.pack(fill=X, padx=5, pady = 5, expand=True)

        #Polynomial 2 Frame
        polynomial2Frame = Frame(self)
        polynomial2Frame.pack(fill=X)
        
        polynomial2Label = Label(polynomial2Frame, text="Polynomial 2:")
        polynomial2Label.pack(side=LEFT, padx=5, pady=5)

        polynomial2Entry = Entry(polynomial2Frame, textvar = self.polynomial2)
        polynomial2Entry.pack(fill=X, padx=5, pady = 5, expand=True)

        #Operation Frame
        operationFrame = Frame(self)
        operationFrame.pack(fill=X)

        operationLabel = Label(operationFrame, text="Operation:")
        operationLabel.pack(side=LEFT, padx = 5, pady = 5)

        reductRadiobutton = Radiobutton(operationFrame, text="Reduce", variable=self.operation, value="reduction")
        reductRadiobutton.pack(side=LEFT, padx = 5, pady = 5)
        reductRadiobutton.invoke()

        addRadiobutton = Radiobutton(operationFrame, text="Add", variable=self.operation, value="addition")
        addRadiobutton.pack(side=LEFT, padx = 5, pady = 5)

        subtractRadiobutton = Radiobutton(operationFrame, text="Subtract", variable=self.operation, value="subtraction")
        subtractRadiobutton.pack(side=LEFT, padx = 5, pady = 5)

        multiplyRadiobutton = Radiobutton(operationFrame, text="Multiply", variable=self.operation, value="multiply")
        multiplyRadiobutton.pack(side=LEFT, padx = 5, pady = 5)

        divideRadiobutton = Radiobutton(operationFrame, text="Divide", variable=self.operation, value="divide")
        divideRadiobutton.pack(side=LEFT, padx = 5, pady = 5)

        invertRadiobutton = Radiobutton(operationFrame, text="Invert", variable=self.operation, value="inverse")
        invertRadiobutton.pack(side=LEFT, padx = 5, pady = 5)

        #Degree Frame
        degreeFrame = Frame(self)
        degreeFrame.pack(pady = 10, anchor = W, padx = 5)

        degreeLabel = Label(degreeFrame, text="Irreducible Polynomial:", font=("Arial Bold", 10))
        degreeLabel.pack(pady = (10,5),anchor = W)

        degree2RadioButton = Radiobutton(degreeFrame, text="Degree 2: x^2 + x^1 + 1", variable=self.degree, value="degree2")
        degree2RadioButton.pack(anchor = W, padx = 5)
        degree2RadioButton.invoke()

        degree3RadioButton = Radiobutton(degreeFrame, text="Degree 3: x^3 + x^2 + 1", variable=self.degree, value="degree3")
        degree3RadioButton.pack(anchor = W, padx = 5)

        degree4RadioButton = Radiobutton(degreeFrame, text="Degree 4: x^4 + x^3 + 1", variable=self.degree, value="degree4")
        degree4RadioButton.pack(anchor = W, padx = 5)

        degree5RadioButton = Radiobutton(degreeFrame, text="Degree 5: x^5 + x^2 + 1", variable=self.degree, value="degree5")
        degree5RadioButton.pack(anchor = W, padx = 5)

        degree6RadioButton = Radiobutton(degreeFrame, text="Degree 6: x^6 + x^1 + 1", variable=self.degree, value="degree6")
        degree6RadioButton.pack(anchor = W, padx = 5)

        degree7RadioButton = Radiobutton(degreeFrame, text="Degree 7: x^7 + x^1 + 1", variable=self.degree, value="degree7")
        degree7RadioButton.pack(anchor = W, padx = 5)

        degree8RadioButton = Radiobutton(degreeFrame, text="Degree 8: x^8 + x^4 + x^3 + x^1 + 1", variable=self.degree, value="degree8")
        degree8RadioButton.pack(anchor = W, padx = 5)

        #Output Type Frane
        outputTypeFrame = Frame(self)
        outputTypeFrame.pack(fill=X)

        outputTypeLabel = Label(outputTypeFrame, text="Output Type:")
        outputTypeLabel.pack(side=LEFT, padx = 5, pady = 5)

        binaryOutputRadiobutton = Radiobutton(outputTypeFrame, text="Binary", variable=self.outputType, value="binary")
        binaryOutputRadiobutton.pack(side=LEFT, padx = 5, pady = 5)
        binaryOutputRadiobutton.invoke()
        
        hexOutputRadiobutton = Radiobutton(outputTypeFrame, text="Hex", variable=self.outputType, value="hex")
        hexOutputRadiobutton.pack(side=LEFT, padx = 5, pady = 5)

        polyOutputRadiobutton = Radiobutton(outputTypeFrame, text="Show Polynomial", variable=self.outputType, value="poly")
        polyOutputRadiobutton.pack(side=LEFT, padx = 5, pady = 5)
        
        #Result Frame
        resultFrame = Frame(self)
        resultFrame.pack(pady = 10)
        
        calculateButton = Button(resultFrame, text="Calculate")
        calculateButton.pack()

        resultLabel = Label(resultFrame, text="RESULT APPEARS HERE")
        resultLabel.pack(pady=10)



def main():

    root = Tk()
    GUI()
    root.mainloop()


if __name__ == '__main__':
    main()
