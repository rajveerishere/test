print("this is a pattern generator module \n we will use nested loops for it")
x = int(input("enter the number of rows you want in your pattern \n"))
z = int(input("enter the number of times you want to repeat your pattern \n"))
a = str(input("enter the character you want to use in your pattern \n"))

def pattern(x,z,a): 
    for i in range(z):
        for k in range(x): 
            for j in range(k + 1): 
                print(a,end="")
            print()
        print() 

pattern(x,z,a) 
