Firstnum = input("First ")
Secondnum = input("Second ")
Output = int(Firstnum) / int(Secondnum)
print("Output: " + str(Output))
Exit = input("Do you want to exit the program y/n ")
if Exit == "n":
    exec(open('main.py').read())
else:
    exit