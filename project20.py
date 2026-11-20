print("Welcome to the bill maker module")
no1 = 2
no2 = 2
no4 = 6
def sitting(no1, no2, no4):
    d = int(input("Enter the number of people in your group: "))
    seated = False

    if d < 1 or d > 4:
        print("Not possible. Each group must have 1 to 4 people.")

    elif d == 1:
        if no1 > 0:
            table_no = 3 - no1
            no1 -= 1
            print(f"You have occupied single-person table S{table_no}.")
            print(f"Remaining single-person tables: {no1}")
            seated = True
        else:
            print("Sorry, all single-person tables are occupied.")

    elif d == 2:
        if no2 > 0:
            table_no = 3 - no2
            no2 -= 1
            print(f"You have occupied two-person table T{table_no}.")
            print(f"Remaining two-person tables: {no2}")
            seated = True
        else:
            print("Sorry, all two-person tables are occupied.")

    elif d == 3 or d == 4:
        if no4 > 0:
            table_no = 7 - no4
            no4 -= 1
            print(f"You have occupied four-person table F{table_no}.")
            print(f"Remaining four-person tables: {no4}")
            seated = True
        else:
            print("Sorry, all four-person tables are occupied.")

    return no1, no2, no4, seated

def order_counter():
    itemno = int(input("Enter the number of items you had ordered: "))
    itemorder = 0
    additemcost = 0.0

    while itemno >= 1:
        itemorder += 1
        cost = float(input(f"Enter the cost of item number {itemorder}: "))
        additemcost += cost
        itemno -= 1

    tax = additemcost * 0.05
    x = int(input("What % of tip do you want to give? "))
    tip = additemcost * (x / 100)
    total_cost = additemcost + tax + tip

    return total_cost, tax


def bill_maker():
    cno = input("Enter your customer number: ")
    total_cost, tax = order_counter()

    print(f"\nCustomer number: {cno}")
    print(f"Your total bill amount is: {total_cost:.2f}")
    print(f"Tax amount is: {tax:.2f}")
    print("Thank you for shopping with us!")
    greeting(total_cost)


def greeting(total_cost):
    print("Have a nice day!")

    if total_cost > 100:
        print("You are eligible for a discount of 5% on your next purchase!")
        print("Please visit our store again to avail the discount.")
        print("Take this card to remind us of the discount next time.")
    else:
        print("Please visit our store again soon.")

no1 = 2
no2 = 2
no4 = 6
another = "yes"

while another == "yes":
    no1, no2, no4, seated = sitting(no1, no2, no4)

    if seated:
        bill_maker()

    another = input(
        "\nIs there another customer? (yes/no): "
    ).strip().lower()

print("Bill maker closed.")


