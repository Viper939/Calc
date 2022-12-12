print("Input The Operation You want to run(Add = + Subtraction = - Multiplication = * Divistion = / )")
Op = input("Operation: ")
if Op == "+":
    exec(open('Add.py').read())
if Op == "-":
    exec(open('Sub.py').read())
if Op == "*":
    exec(open('Mul.py').read())
if Op == "/":
    exec(open('Div.py').read())