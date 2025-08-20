height = int(input("ENTER YOUR HEIGHT: "))
bill = 0
if height >= 120:
    age = int(input("ENTER YOUR AGE: "))
    if age <= 12:
        bill = 5
        print("children tickets are $5")
    elif age <= 18:
        bill = 7
        print("youth tickets are $7")
    elif age>=45 and age<=55:
        bill = 0
        print("ENJOY THE FREE RIDE!")    
    else:
        bill = 12
        print("adult tickets are $12")

    wants_photo = input("DO YOU WANT PHOTO Y OR N: ")
    if wants_photo.lower() == 'y':
        bill += 3
    
        
    print(f"YOUR TOTAL BILL IS ${bill}")    
else:
    print("sorry, you have to grow taller!")               