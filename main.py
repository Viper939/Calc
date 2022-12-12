from Add import *
from Sub import *
from Mul import *
from Div import *

while True:
    print("Input The Operation You want to run(Add = + Subtraction = - Multiplication = * Divistion = / )")
    Op = input("Operation: ")
    
    if Op == "+":
        add()
    if Op == "-":
        sub()
    if Op == "*":
        mul()
    if Op == "/":
        div()