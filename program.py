from app.calculator import CalcFunctions

calc_functions = CalcFunctions()

while True:
    func = str(input("What function would you like? Add, Subtract, Multiply or Divide?\n Type "
                     "'Exit' to finish.\n")).capitalize()
    if func == "Add":
        print(calc_functions.add())
    elif func == "Subtract":
        print(calc_functions.subtract())
    elif func == "Multiply":
        print(calc_functions.multiply())
    elif func == "Divide":
        print(calc_functions.divide())
    elif func == "Exit":
        break
    else:
        print("Unrecognised input, please try again")
