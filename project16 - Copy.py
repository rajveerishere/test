print("welcome to ART store")
print("we have a wide variety of art supplies for you to choose from")
print("please select from the following options:")
print("1. Paints - $5")
print("2. Brushes - $2")
print("3. Canvas - $6")
print("4. oil Colours - $2")
print("5. pencils - $1")
can = 5
brushes = 2
canvas = 6
oil_colours = 2
pencils = 1
x = str(input("what is you name sir/madam ? \n"))
def items():
    paint_quantity = brush_quantity = canvas_quantity = oil_colour_quantity = pencil_quantity = 0
    q = str(input("do you want to buy paints? (yes/no) \n"))
    if q == "yes":
        pq = int(input("how many paint bottles do you want to buy ? \n"))
        
    q = str(input("do you want to buy brushes? (yes/no) \n"))
    if q == "yes":
        bq = int(input("how many brushes do you want to buy ? \n"))
        
    q = str(input("do you want to buy canvas? (yes/no) \n"))
    if q == "yes":
        cq = int(input("how many canvases do you want to buy ? \n"))
        
    q = str(input("do you want to buy oil colours? (yes/no) \n"))
    if q == "yes":
        oq = int(input("how many oil colours do you want to buy ? \n"))
        
    q = str(input("do you want to buy pencils? (yes/no) \n"))
    if q == "yes": 
        pencilq = int(input("how many pencils do you want to buy ? \n"))
    return pq, bq, cq, oq, pencilq

def cost (pq, bq, cq, oq, pencilq):
    total_cost = (pq * can) + (bq * brushes) + (cq * canvas) + (oq * oil_colours) + (pencilq * pencils)
    pc = (pq * can)
    bc = (bq * brushes)
    cc = (cq * canvas)
    oc = (oq * oil_colours)
    pencilc = (pencilq * pencils)
    return total_cost , pc , bc , cc , oc , pencilc
def greet(total_cost):
    print(f"Thank you , \n for shopping with us {x}")
    if total_cost > 60:
        print("seems to be a keen painter!")
    else:
        print("we hope you enjoy your art supplies!")
def display(total_cost , pc , bc , cc , oc , pencilc):
    print(f"your total cost is ${total_cost}")
    print(f"cost of paints: ${pc}")
    print(f"cost of brushes: ${bc}")
    print(f"cost of canvas: ${cc}")
    print(f"cost of oil colours: ${oc}")
    print(f"cost of pencils: ${pencilc}")
def bill(pq, bq, cq, oq, pencilq,total_cost , pc , bc , cc , oc , pencilc):
    print(f"your total bill is ${total_cost}")
    if total_cost > 60:
        discount = total_cost * 0.1
        total_cost -= discount
        r = [f"your quanity for each item is: \n paints: {pq} \n brushes: {bq} \n canvas: {cq} \n oil colours: {oq} \n pencils: {pencilq}"]
        f = [print(f"your total bill is ${total_cost}\n") ]
        j = [print(f"your cost forr each item is: \n paints: ${pc} \n brushes: ${bc} \n canvas: ${cc} \n oil colours: ${oc} \n pencils: ${pencilc}\n") ]
        h = [  print("you have spent more than $60, you are eligible for a 10% discount") ]
        m = [      print(f"your total bill after discount is ${total_cost}\n") ]
        t = [        print(f"have a nice day MR/MRS {x}!") ]
    return h,m,t 
print("===========================================")
items()
cost()
greet()
display()
bill()



        