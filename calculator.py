print("BASIC CALCULATOR APP")

while 1 == 1:
    wres = input("Enter procedure: ")
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    if(wres == "Add"):
        res = a + b
        print(res)
    elif(wres == "Subtract"):
        res = a - b
        print(res)
    elif(wres == "Multiply"):
        res = a * b
        print(res)
    elif(wres == "Divide"):
        res = a / b
        print(res)
    elif(wres == "Quit"):
        print("Quitting Calculator")
        break
    else:
        print("Input not valid. Try Again.")
        continue
    
