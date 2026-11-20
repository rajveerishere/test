print("this is cuber")
print("Make sure to enter a number that is divisible by 3")
x = int(input("Please enter the number you want to cube : "))
def cube(x):
    print ("This is cube of the number",x*x*x)

def div3(x):
    if x % 3 == 0 :
        cube(x)
    else:
        print("The number given by you is not divisible by 3 , which is not aligning with our terms and conditions")

div3(x)