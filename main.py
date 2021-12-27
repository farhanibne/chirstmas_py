def triangleShape(n):
    for i in range(n):
        for j in range(n-i):
            print(" ", end="")
        for k in range(2*i+1):
            print("*", end="")
        print()

def polyshape(n):
    for i in range(n):
        for j in range(n-i):
            print(' ',end="")
        print('***')

row = int(input("Enter the number of rows: "))
triangleShape(row)
triangleShape(row)
polyshape(row)