# Project: Smart Electrical Calculator
# Author: Onyibor Chidera Maximillian
# Description: Calculates voltage, current, resistance, and power.
# Unique Feature: Electrical Safety Checker.

def calculate_voltage(current, resistance):
    # Calculate voltage using Ohm's Law.
    return current * resistance


def calculate_current(voltage, resistance):
    # Calculate current using Ohm's Law.
    return voltage / resistance


def calculate_resistance(voltage, current):
    # Calculate resistance using Ohm's Law.
    return voltage / current


def calculate_power(voltage, current):
    # Calculate electrical power.
    return voltage * current


def safety_checker(power, safe_limit):
    # Check whether the calculated power exceeds the chosen limit.
    if power > safe_limit:
        print("WARNING: Power exceeds your chosen safety limit!")
    else:
        print("Power is within your chosen limit.")


def main():
    # Display the program's welcome message.
    print("=" * 40)
    print(" SMART ELECTRICAL CALCULATOR")
    print("=" * 40)

    while True:
        # Display the available calculation options.
        print("\nChoose what you want to calculate:")
        print("1. Voltage")
        print("2. Current")
        print("3. Resistance")
        print("4. Power")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        try:
            # Perform the calculation selected by the user.
            if choice == "1":
                current = float(input("Enter current (A): "))
                resistance = float(input("Enter resistance (ohms): "))

                voltage = calculate_voltage(current, resistance)
                print(f"Voltage = {voltage:.2f} V")

            elif choice == "2":
                voltage = float(input("Enter voltage (V): "))
                resistance = float(input("Enter resistance (ohms): "))

                if resistance == 0:
                    print("Error: Resistance cannot be zero.")
                    continue

                current = calculate_current(voltage, resistance)
                print(f"Current = {current:.2f} A")

            elif choice == "3":
                voltage = float(input("Enter voltage (V): "))
                current = float(input("Enter current (A): "))

                if current == 0:
                    print("Error: Current cannot be zero.")
                    continue

                resistance = calculate_resistance(voltage, current)
                print(f"Resistance = {resistance:.2f} ohms")

            elif choice == "4":
                voltage = float(input("Enter voltage (V): "))
                current = float(input("Enter current (A): "))

                power = calculate_power(voltage, current)
                print(f"Power = {power:.2f} W")

                # Ask the user to set a power limit for the safety checker.
                safe_limit = float(
                    input("Enter your chosen power limit (W): ")
                )

                if safe_limit < 0:
                    print("Error: Power limit cannot be negative.")
                    continue

                safety_checker(power, safe_limit)

            elif choice == "5":
                print("Thank you for using Smart Electrical Calculator!")
                break

            else:
                print("Invalid choice. Please select a number from 1 to 5.")

        except ValueError:
            # Handle inputs that are not valid numbers.
            print("Invalid input. Please enter a valid number.")


# Start the program.
if __name__ == "__main__":
    main()
