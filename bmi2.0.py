print("WELCOME TO BMI CALCULATOR 2.0!")
height = float(input("ENTER YOUR HEIGHT: "))
weight = int(input("ENTER YOUR WEIGHT: "))
bmi = weight/height**2
if bmi < 16:
    print(f"YOUR BMI IS {bmi:.2f}, YOU ARE Underweight (Severe thinness)")
elif bmi < 17:
    print(f"YOUR BMI IS {bmi:.2f}, Underweight (Moderate thinness)")
elif bmi < 18.5:
    print(f"YOUR BMI IS {bmi:.2f}, Underweight (Mild thinness)")
elif bmi < 25:
    print(f"YOUR BMI IS {bmi:.2f}, Normal range")
elif bmi < 30:
    print(f"YOUR BMI IS {bmi:.2f}, Overweight (Pre-obese)")
elif bmi < 35:
    print(f"YOUR BMI IS {bmi:.2f}, Obese (Class I)")
elif bmi < 40:
    print(f"YOUR BMI IS {bmi:.2f}, Obese (Class II)")
elif bmi >= 40:
    print(f"YOUR BMI IS {bmi:.2f}, Obese (Class III)")                             
