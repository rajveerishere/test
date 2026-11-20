print("This is factorial maker")
x = int(input("Enter the number which you want factorial of :" ))
def factorial(x):
    if x == 0 or x == 1 :
        return 1 
    return x  * factorial(x - 1)







print("The factorial of ", x ,"is" , factorial(x))