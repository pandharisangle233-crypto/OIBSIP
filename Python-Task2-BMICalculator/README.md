# BMI Calculator

A simple command line BMI (Body Mass Index) calculator made in Python.
This project is part of my Oasis Infobyte internship (Python Programming Track, Task 2 - Beginner level).

## What it does

- Asks the user for weight (kg) and height (m)
- Calculates BMI using the formula: `BMI = weight / (height x height)`
- Shows the BMI rounded to 2 decimal places
- Shows the category:

| BMI | Category |
|---|---|
| below 18.5 | Underweight |
| 18.5 - 24.9 | Normal |
| 25 - 29.9 | Overweight |
| 30 and above | Obese |

- Input validation: text, empty input, zero and negative values are rejected with an error message
- You can calculate again without restarting the program

## How to run

1. Install Python 3 (no extra libraries are needed)
2. Open a terminal in this folder
3. Run:

```
python bmi_calculator.py
```

## Example

```
Enter your weight in kg: 70
Enter your height in metres (e.g. 1.65): 1.75

Your BMI is: 22.86
Category   : Normal
```

More examples are in `sample_output.txt`.

## Files

- `bmi_calculator.py` - source code
- `sample_output.txt` - output of a test run
- `README.md` - this file

## Author

Name: ______________
Track: Python Programming
Task: Task 2 - BMI Calculator
#oasisinfobyte
