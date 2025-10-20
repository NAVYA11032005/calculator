# Calculator CLI Application

A simple and efficient command-line calculator built with Python that performs basic arithmetic operations with a clean, user-friendly interface.

## Features

- **Basic Arithmetic Operations**: Addition, Subtraction, Multiplication, Division
- **Dual Calculation Modes**: 
  - Standard step-by-step mode
  - Direct expression input mode
- **Comprehensive Error Handling**: Validates inputs and prevents division by zero
- **Continuous Operation**: Runs until user explicitly chooses to exit
- **Clean Interface**: Well-formatted output with clear prompts

## Requirements

- Python 3.x

## Installation

1. Download `calculator.py` to your local machine
2. Open terminal/command prompt
3. Navigate to the directory containing the file

## Usage

Run the application:
```bash
python calculator.py
```

Follow the on-screen menu to select your preferred calculation mode.

### Standard Mode Example:
```
Enter the first number: 15
Enter an operator (+, -, *, /): *
Enter the second number: 4

Result: 15 * 4 = 60
```

### Expression Mode Example:
```
Enter expression: 25 / 5
Result: 25.0 / 5.0 = 5.0
```

## Project Structure

The application consists of a single file:
- `calculator.py` - Main application with all functions and logic

## Technical Implementation

### Core Functions:
- `addition(a, b)` - Returns sum of two numbers
- `subtraction(a, b)` - Returns difference between two numbers
- `multiplication(a, b)` - Returns product of two numbers
- `division(a, b)` - Returns quotient with zero-division protection
- `get_number(prompt)` - Handles and validates numeric input
- `perform_calculation()` - Manages the main calculation loop

### Key Features:
- Input validation for numbers and operators
- Error handling for invalid operations
- Modular function design for easy maintenance
- User-friendly prompts and formatted results

## Skills Demonstrated

- Python functions and modular programming
- User input handling and validation
- Loop structures and conditional logic
- Error and exception handling
- Command-line interface design
- Code documentation and organization

## Exit the Application

Type 'quit' or select the exit option from the menu to close the application.

---

**Note**: This project was developed as part of a Python programming exercise focusing on fundamental programming concepts and CLI application development.
