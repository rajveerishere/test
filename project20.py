print("Welcome to the bill maker module")


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

another = "yes"

while another == "yes":
    bill_maker()
    another = input("\nIs there another customer? (yes/no): ").strip().lower()

print("Bill maker closed.")

