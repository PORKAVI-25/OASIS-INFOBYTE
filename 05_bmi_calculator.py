def calculate_bmi(weight_kg, height_m):
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be greater than zero.")
    return weight_kg / (height_m ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal weight"
    if bmi < 30:
        return "Overweight"
    return "Obesity range"

def main():
    print("=== BMI Calculator ===")
    try:
        weight = float(input("Weight in kilograms: "))
        height = float(input("Height in metres (for example, 1.65): "))
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is {bmi:.2f}")
        print("Category:", classify_bmi(bmi))
        print("Note: BMI is a general screening measure, not a diagnosis.")
    except ValueError as error:
        print("Input error:", error)

if __name__ == "__main__":
    main()
