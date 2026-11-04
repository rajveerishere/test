print("welcome to ART store")
print("we have a wide variety of art supplies for you to choose from")
print("please select from the following options:")
print("1. Paints - $5")
print("2. Brushes - $2")
print("3. Canvas - $6")
print("4. Oil colours - $2")
print("5. Pencils - $1")

paint_price = 5
brush_price = 2
canvas_price = 6
oil_colours_price = 2
pencil_price = 1

customer_name = input("What is your name, sir/madam? \n")

def items():
    answer = input("Do you want to buy paints? (yes/no) \n")
    if answer.lower() == "yes":
        pq = int(input("How many paint bottles do you want to buy? \n"))
    else:
        pq = 0

    answer = input("Do you want to buy brushes? (yes/no) \n")
    if answer.lower() == "yes":
        bq = int(input("How many brushes do you want to buy? \n"))
    else:
        bq = 0

    answer = input("Do you want to buy canvas? (yes/no) \n")
    if answer.lower() == "yes":
        cq = int(input("How many canvases do you want to buy? \n"))
    else:
        cq = 0

    answer = input("Do you want to buy oil colours? (yes/no) \n")
    if answer.lower() == "yes":
        oq = int(input("How many oil colours do you want to buy? \n"))
    else:
        oq = 0

    answer = input("Do you want to buy pencils? (yes/no) \n")
    if answer.lower() == "yes":
        pencilq = int(input("How many pencils do you want to buy? \n"))
    else:
        pencilq = 0

    return pq, bq, cq, oq, pencilq


def cost(pq, bq, cq, oq, pencilq):
    pc = pq * paint_price
    bc = bq * brush_price
    cc = cq * canvas_price
    oc = oq * oil_colours_price
    pencilc = pencilq * pencil_price

    totalc = pc + bc + cc + oc + pencilc
    return totalc, pc, bc, cc, oc, pencilc


def greet(customer_name, totalc):
    print(f"Thank you for shopping with us, {customer_name}.")
    if totalc > 60:
        print("Seems like you are a keen painter!")
    else:
        print("We hope you enjoy your art supplies!")


def display(totalc, pc, bc, cc, oc, pencilc):
    print(f"Your total cost is ${totalc}")
    print(f"Cost of paints: ${pc}")
    print(f"Cost of brushes: ${bc}")
    print(f"Cost of canvas: ${cc}")
    print(f"Cost of oil colours: ${oc}")
    print(f"Cost of pencils: ${pencilc}")


def bill(customer_name, pq, bq, cq, oq, pencilq, totalc, pc, bc, cc, oc, pencilc):
    print(f"Your total bill is ${totalc}")

    print(f"Your quantity for each item is:")
    print(f"Paints: {pq}")
    print(f"Brushes: {bq}")
    print(f"Canvas: {cq}")
    print(f"Oil colours: {oq}")
    print(f"Pencils: {pencilq}")

    print(f"Your cost for each item is:")
    print(f"Paints: ${pc}")
    print(f"Brushes: ${bc}")
    print(f"Canvas: ${cc}")
    print(f"Oil colours: ${oc}")
    print(f"Pencils: ${pencilc}")

    if totalc > 60:
        discount = totalc * 0.10
        final_cost = totalc - discount
        print("You have spent more than $60, so you are eligible for a 10% discount.")
        print(f"Your total bill after discount is ${final_cost:.2f}")
    else:
        final_cost = totalc
        print(f"Your final bill is ${final_cost:.2f}")

    print(f"Have a nice day, Mr./Ms. {customer_name}!")
    return final_cost


print("===========================================")

pq, bq, cq, oq, pencilq = items()
totalc, pc, bc, cc, oc, pencilc = cost(
    pq, bq, cq, oq, pencilq
)

greet(customer_name, totalc)
display(totalc, pc, bc, cc, oc, pencilc)
final_cost = bill(
    customer_name, pq, bq, cq, oq, pencilq, totalc, pc, bc, cc, oc, pencilc
)

print("===========================================")




        