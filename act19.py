print("This is the bill maker")
x = int(input("Please enter the bill amount you have : "))
y = int(input("Please enter the tip % you want to offer : ")) 
def total_calc(x,y):
    d =((y*0.01)*x) + x
    return d 
ans = total_calc(x,y)
"""hi """
print("your total bill is : ",total_calc(x,y))