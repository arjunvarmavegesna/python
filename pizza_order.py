pizza = input("WHAT SIZE OF PIZZA YOU WANT S M L: ")
add_pepperoni = input("DO YOU WANT TO ADD PEPPERONI Y OR N: ")
extra_cheese = input("DO YOU WANT EXTRA CHEESE Y OR N: ")
bill = 0
if pizza.lower() == 's':
    bill = 15
    if add_pepperoni.lower() == 'y':
        bill += 2
elif pizza.lower() == 'm':
    bill = 20
    if add_pepperoni.lower() == 'y':
        bill += 3
elif pizza.lower() == 'l':
    bill = 25
    if add_pepperoni.lower() == 'y':
        bill += 3

if extra_cheese.lower() == 'y':
    bill += 1

print(f"YOUR BILL IS {bill}")
    