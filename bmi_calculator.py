"""
BMI (Body Mass Index) Calculator
Supports both Imperial (English) units (lbs, ft/in) and Metric units (kg, cm).
"""

from typing import Tuple


def calculate_bmi_imperial(weight_lbs: float, height_inches: float) -> float:
    """Calculate BMI using Imperial / English units.
    
    Formula: (weight in pounds / (height in inches)^2) * 703
    """
    if height_inches <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight_lbs <= 0:
        raise ValueError("Weight must be greater than zero.")
    return (weight_lbs / (height_inches ** 2)) * 703


def calculate_bmi_metric(weight_kg: float, height_cm: float) -> float:
    """Calculate BMI using Metric units.
    
    Formula: weight in kg / (height in meters)^2
    """
    if height_cm <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than zero.")
    height_m = height_cm / 100.0
    return weight_kg / (height_m ** 2)


def get_bmi_category(bmi: float) -> Tuple[str, str]:
    """Return the BMI category and a short health description."""
    if bmi < 18.5:
        return (
            "Underweight",
            "You may need to gain weight. Consult a healthcare provider for personalized advice."
        )
    elif 18.5 <= bmi < 25.0:
        return (
            "Normal weight",
            "You are in a healthy weight range for your height. Keep up the good work!"
        )
    elif 25.0 <= bmi < 30.0:
        return (
            "Overweight",
            "You are slightly above the typical healthy weight range. Consider maintaining a balanced diet and regular exercise."
        )
    elif 30.0 <= bmi < 35.0:
        return (
            "Obese (Class I)",
            "Your BMI falls into Obesity Class I. Speaking with a doctor or nutritionist is recommended."
        )
    elif 35.0 <= bmi < 40.0:
        return (
            "Obese (Class II)",
            "Your BMI falls into Obesity Class II. Medical consultation is strongly advised."
        )
    else:
        return (
            "Severe / Morbid Obesity (Class III)",
            "Your BMI falls into Obesity Class III. Please consult a medical professional for support."
        )


def get_healthy_weight_range_imperial(height_inches: float) -> Tuple[float, float]:
    """Calculate the healthy weight range (BMI 18.5 to 24.9) in pounds for a given height."""
    min_weight = (18.5 * (height_inches ** 2)) / 703
    max_weight = (24.9 * (height_inches ** 2)) / 703
    return min_weight, max_weight


def get_healthy_weight_range_metric(height_cm: float) -> Tuple[float, float]:
    """Calculate the healthy weight range (BMI 18.5 to 24.9) in kg for a given height."""
    height_m = height_cm / 100.0
    min_weight = 18.5 * (height_m ** 2)
    max_weight = 24.9 * (height_m ** 2)
    return min_weight, max_weight


def prompt_positive_float(prompt_message: str) -> float:
    """Prompt the user until a positive float is entered."""
    while True:
        user_input = input(prompt_message).strip()
        try:
            val = float(user_input)
            if val <= 0:
                print("  [!] Please enter a positive number greater than 0.")
                continue
            return val
        except ValueError:
            print("  [!] Invalid input. Please enter a valid numerical value.")


def display_results(bmi: float, category: str, advice: str, healthy_min: float, healthy_max: float, unit_label: str):
    """Print the calculated BMI report."""
    border = "=" * 50
    print("\n" + border)
    print("                 BMI REPORT")
    print(border)
    print(f"  Your BMI           : {bmi:.2f}")
    print(f"  Category           : {category}")
    print(f"  Healthy Weight Range: {healthy_min:.1f} - {healthy_max:.1f} {unit_label}")
    print("-" * 50)
    print(f"  Note: {advice}")
    print(border + "\n")


def run_imperial_flow():
    """Run interactive flow for English / Imperial units."""
    print("\n--- English / Imperial Units ---")
    print("Height input format:")
    print("  1) Feet and Inches (e.g., 5 ft 10 in)")
    print("  2) Total Inches (e.g., 70 in)")
    choice = input("Select format [1 or 2, default: 1]: ").strip()

    if choice == "2":
        height_inches = prompt_positive_float("Enter total height in inches: ")
    else:
        feet = prompt_positive_float("Enter height - feet: ")
        while True:
            inches_input = input("Enter height - inches [0-11]: ").strip()
            try:
                inches = float(inches_input)
                if 0 <= inches < 12:
                    break
                print("  [!] Inches should be between 0 and 11.99.")
            except ValueError:
                print("  [!] Invalid input. Please enter a number.")
        height_inches = (feet * 12) + inches

    weight_lbs = prompt_positive_float("Enter weight in pounds (lbs): ")

    bmi = calculate_bmi_imperial(weight_lbs, height_inches)
    category, advice = get_bmi_category(bmi)
    min_w, max_w = get_healthy_weight_range_imperial(height_inches)
    display_results(bmi, category, advice, min_w, max_w, "lbs")


def run_metric_flow():
    """Run interactive flow for Metric units."""
    print("\n--- Metric Units ---")
    height_cm = prompt_positive_float("Enter height in centimeters (cm): ")
    weight_kg = prompt_positive_float("Enter weight in kilograms (kg): ")

    bmi = calculate_bmi_metric(weight_kg, height_cm)
    category, advice = get_bmi_category(bmi)
    min_w, max_w = get_healthy_weight_range_metric(height_cm)
    display_results(bmi, category, advice, min_w, max_w, "kg")


def main():
    print("=" * 50)
    print("         WELCOME TO BMI CALCULATOR")
    print("=" * 50)

    while True:
        print("Please choose your preferred unit system:")
        print("  1) English / Imperial (Pounds, Feet & Inches)")
        print("  2) Metric (Kilograms, Centimeters)")
        print("  3) Exit")

        selection = input("\nEnter your choice (1, 2, or 3): ").strip()

        if selection == "1":
            run_imperial_flow()
        elif selection == "2":
            run_metric_flow()
        elif selection == "3":
            print("\nThank you for using BMI Calculator. Goodbye!")
            break
        else:
            print("\n[!] Invalid selection. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
