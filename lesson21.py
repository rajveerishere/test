print("wecolme to the vending machine")
print("wen-deeng machine")
print("Accepts only coins of \n 1$ \n 2$ \n 5$ \n 10$")
print("Chocolate = 2$")
coco = 2
while True:
    x = int(input("enter the number of chocolates that you want"))
    y = x * coco
    print(f"your bill is {y}")
    z = int(input("enter the number of 10$ coins you want to insert"))
    if z*10 >= y:
        print("your order is confirmed")
        break
    else:
        a = y - z*10
        print(f"you need to insert {a} more dollars")
        b = int(input("enter the number of 5$ coins you want to insert"))
        if b*5 >= a:
            print("your order is confirmed")
            break
        else:
            c = a - b*5
            print(f"you need to insert {c} more dollars")
            d = int(input("enter the number of 2$ coins you want to insert"))
            if d*2 >= c:
                print("your order is confirmed")
                break
            else:
                e = c - d*2
                print(f"you need to insert {e} more dollars")
                f = int(input("enter the number of 1$ coins you want to insert"))
                if f >= e:
                    print("your order is confirmed")
                    break
                else:
                    print("you have not inserted enough money, please try again")
                    continue
print(f"you have inserted {z} 10$ coins, {b} 5$ coins, {d} 2$ coins and {f} 1$ coins")
def change(x):
    if x > 0:
        print(f"your change is {x}")
    else:
        print("you have not inserted enough money, please try again")
def greeting():
    print("Thank you for using our vending machine , have a nice day")
    if y < z*10 + b*5 + d*2 + f:
        change(z*10 + b*5 + d*2 + f - y)
    if y > 20:
        print("you have ordered more than 10 chocolates, you will get a free chocolate")





