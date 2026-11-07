# BMI Calculator (command line version)
# OIBSIP - Python Programming Track - Task 2


def get_number(message):
    # keeps asking until the user types a valid positive number
    while True:
        value = input(message)
        try:
            number = float(value)
        except ValueError:
            print("Error: please enter a number only (example: 65 or 1.7)")
            continue

        if number <= 0:
            print("Error: the value must be greater than zero")
            continue

        return number


def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=" * 35)
    print("         BMI CALCULATOR")
    print("=" * 35)

    while True:
        weight = get_number("Enter your weight in kg: ")
        height = get_number("Enter your height in metres (e.g. 1.65): ")

        # people sometimes type height in cm by mistake
        if height > 3:
            print("That height looks too big. Please enter it in metres, not cm.")
            continue

        bmi = calculate_bmi(weight, height)
        category = get_category(bmi)

        print()
        print("Your BMI is:", round(bmi, 2))
        print("Category   :", category)
        print()

        again = input("Do you want to calculate again? (y/n): ").strip().lower()
        if again != "y":
            break
        print()

    print("Thank you for using the BMI Calculator!")


if __name__ == "__main__":
    main()
