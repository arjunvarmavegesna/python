print("WELOCOME TO TIP CALCULATOR!")
bill = float(input("ENTER THE BILL AMOUNT: $"))
tip = int(input("WHAT PERCENTAGE OF TIP 12 15 20: "))
bill_with_tip = tip /100 * bill + bill
persons = int(input("HOW MANY WANT TO SPLIT: "))
total_bill = bill_with_tip / persons
final_bill = round(total_bill, 2)
print(f"BILL WITH TIP: ${bill_with_tip}")
print(f"EACH PERSON SHOULD PAY: ${final_bill}")


