"""
BMI Calculator Program
Author: Kangana Patel
Description: Calculates Body Mass Index and classifies result.
"""

def calculate_bmi(weight_kg, height_m):
    """
    Calculates BMI value.

    Parameters:
        weight_kg (float): Weight in kilograms
        height_m (float): Height in meters

    Returns:
        float: Calculated BMI
    """
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi_value):
    """
    Classifies BMI category.

    Parameters:
        bmi_value (float): Calculated BMI

    Returns:
        str: BMI category
    """
    if bmi_value < 18.5:
        return "Underweight"
    elif 18.5 <= bmi_value < 25:
        return "Normal weight"
    elif 25 <= bmi_value < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    """
    Main function to execute BMI program.
    """
    weight_kg = float(input("Enter weight in kilograms: "))
    height_m = float(input("Enter height in meters: "))

    bmi_value = calculate_bmi(weight_kg, height_m)
    bmi_category = classify_bmi(bmi_value)

    print(f"Your BMI is: {bmi_value:.2f}")
    print(f"BMI Category: {bmi_category}")


if __name__ == "__main__":
    main()
c
