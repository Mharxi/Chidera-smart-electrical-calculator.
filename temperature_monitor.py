# CTE123 Python Mini Project: Temperature Monitor and Alarm Checker
# This program analyses five machine-temperature readings.
# Extra feature: it reports whether the average temperature is within the chosen limit.

def get_temperature(prompt):
    """Get a valid numeric temperature from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric temperature.")


def analyse_temperatures(readings, safe_limit):
    """Return the highest, lowest and average readings and alarm status."""
    highest = max(readings)
    lowest = min(readings)
    average = sum(readings) / len(readings)
    unsafe_readings = [value for value in readings if value > safe_limit]
    return highest, lowest, average, unsafe_readings


def main():
    readings = []

    print("===== MACHINE TEMPERATURE MONITOR =====")
    safe_limit = get_temperature("Enter the maximum safe temperature (C): ")

    # Collect exactly five machine-temperature readings.
    for count in range(1, 6):
        temperature = get_temperature(f"Enter temperature reading {count} (C): ")
        readings.append(temperature)

    highest, lowest, average, unsafe = analyse_temperatures(readings, safe_limit)

    print("\n===== TEMPERATURE REPORT =====")
    print(f"Readings: {readings}")
    print(f"Highest temperature: {highest:.2f} C")
    print(f"Lowest temperature: {lowest:.2f} C")
    print(f"Average temperature: {average:.2f} C")

    # Warn if any reading is above the user-defined safe limit.
    if unsafe:
        print("ALARM: Unsafe temperature reading(s) detected!")
        print("Readings above the safe limit:", unsafe)
    else:
        print("STATUS: All readings are within the safe limit.")

    # Original extra feature: assess the average against the same safe limit.
    if average > safe_limit:
        print("AVERAGE STATUS: The average temperature is above the safe limit.")
    else:
        print("AVERAGE STATUS: The average temperature is within the safe limit.")


if __name__ == "__main__":
    main()
