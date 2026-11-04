print("this is a pattern generator module \n we will use nested loops for it")
x = int(input("enter the number of rows you want in your pattern \n"))
y = int(input("enter the number of columns you want in your pattern \n"))
z = int(input("enter the number of times you want to repeat your pattern \n"))
a = str(input("enter the character you want to use in your pattern \n"))
def pattern(x,y,z,a):
    for i in range(z):
        z = z-1
        for i in range(x):
            for j in range(y):
                y = y - 1
                print(a,end="")
            print()
pattern(x,y,z,a)