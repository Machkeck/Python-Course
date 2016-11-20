#python 3

while True:
    n = eval(input("Type a number: "))
    if n == "stop":
        print("Stopped")
        break
    if type(n) == str:
        print("Input is not a number")
    else:
        print(n,pow(n,3))

