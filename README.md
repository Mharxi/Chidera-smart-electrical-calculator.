# Temperature Monitor and Alarm Checker

## Project Description
The Temperature Monitor and Alarm Checker is a Python program developed for the CTE123 Python Mini Project. It accepts five machine-temperature readings, calculates the highest, lowest and average temperatures, and warns when any reading exceeds a user-entered safe limit.

## Features
- Accepts exactly five temperature readings.
- Calculates the highest temperature.
- Calculates the lowest temperature.
- Calculates the average temperature.
- Displays an alarm warning if any reading is above the safe limit.
- Allows the user to enter the safe temperature limit for the machine being monitored.

## How to Run
1. Install Python 3.
2. Download this repository.
3. Open a terminal in the project folder.
4. Run: `python temperature_monitor.py`

## Sample Output
```text
===== MACHINE TEMPERATURE MONITOR =====
Enter the maximum safe temperature (C): 80
Enter temperature reading 1 (C): 65
Enter temperature reading 2 (C): 72
Enter temperature reading 3 (C): 85
Enter temperature reading 4 (C): 70
Enter temperature reading 5 (C): 78

===== TEMPERATURE REPORT =====
Readings: [65.0, 72.0, 85.0, 70.0, 78.0]
Highest temperature: 85.00 C
Lowest temperature: 65.00 C
Average temperature: 74.00 C
ALARM: Unsafe temperature reading(s) detected!
Readings above the safe limit: [85.0]
AVERAGE STATUS: The average temperature is within the safe limit.
```

## Original Extra Feature
**Average Temperature Status:** In addition to checking individual readings, the program checks whether the average temperature is above or within the user-defined safe limit.

## Important Note
The safe temperature limit depends on the specific machine and should be set according to the manufacturer's instructions or the guidance of a qualified technician. The example limit of 80°C is for demonstration only.

## What I Learned
- Using Python functions
- Collecting data with a loop
- Using lists to store readings
- Applying `max()`, `min()` and `sum()`
- Using conditional statements
- Validating numeric input and displaying warnings

## Author
Add your full name, department and institution here.
