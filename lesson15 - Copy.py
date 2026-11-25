print("===========================================\n")
print("hello you are welcome to my lemonade stand")
print("===========================================\n")
x = str(input("what is you name sir/madam ? \n"))
print("This is a menu - \n Lemonade : 40 \n -- Suppementory --\n Lemon tea : 20 \n sugar cane juice : 20 ")

def bill(bl1 , bl2):
    total = bl1 * 40 + bl2 * 20
    print("Your total bill is:", total)
    return total

def purchase():
    n = int(input("Enter the number of lemonades you want"))
    dr2 = int(input("Enter the number of suplementory drinks you want"))
    total = bill(n, dr2)
    return total, n, dr2


def thankyou(total):
    print("Thank you for visiting our lemonade stand!")
    if total >= 100:
        print("You are eligible for a 10% discount on your next purchase!")
    else: 
        print("We hope to see you again soon!")


total, n, dr2 = purchase()
print("Your total bill is:", total)
print(f"price per type of brevrage is : \n Lemonade : {40*n} \n supplementory drinks : {20*dr2}")
thankyou(total)
  