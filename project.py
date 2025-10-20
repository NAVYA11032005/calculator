"""
Simple Calculator CLI Application
A command-line calculator supporting basic arithmetic operations.
"""

def display_welcome():
    """Display welcome message and instructions"""
    print("\n" + "="*50)
    print("           WELCOME TO CALCULATOR CLI")
    print("="*50)
    print("This calculator supports the following operations:")
    print("  +  Addition")
    print("  -  Subtraction")
    print("  *  Multiplication")
    print("  /  Division")
    print("Enter 'quit' to exit the program")
    print("="*50)

def get_number(prompt):
    """
    Get a valid number input from user
    
    Args:
        prompt (str): The message to display to user
        
    Returns:
        float: Valid number entered by user
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def addition(a, b):
    """
    Perform addition operation
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Sum of a and b
    """
    return a + b

def subtraction(a, b):
    """
    Perform subtraction operation
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Difference of a and b
    """
    return a - b

def multiplication(a, b):
    """
    Perform multiplication operation
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Product of a and b
    """
    return a * b

def division(a, b):
    """
    Perform division operation with zero division check
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Quotient of a and b
        
    Raises:
        ValueError: If division by zero is attempted
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed!")
    return a / b

def perform_calculation():
    """
    Main function to run the calculator application
    Handles user input and performs calculations
    """
    display_welcome()
    
    while True:
        try:
            # Get first number
            num1 = get_number("\nEnter the first number: ")
            
            # Get operator
            operator = input("Enter an operator (+, -, *, /): ").strip()
            
            # Check if user wants to quit
            if operator.lower() == 'quit':
                print("👋 Thank you for using Calculator CLI. Goodbye!")
                break
            
            # Validate operator
            if operator not in ['+', '-', '*', '/']:
                print("❌ Invalid operator! Please use one of: +, -, *, /")
                continue
            
            # Get second number
            num2 = get_number("Enter the second number: ")
            
            # Perform calculation based on operator
            result = None
            operation_name = ""
            
            if operator == '+':
                result = addition(num1, num2)
                operation_name = "Addition"
            elif operator == '-':
                result = subtraction(num1, num2)
                operation_name = "Subtraction"
            elif operator == '*':
                result = multiplication(num1, num2)
                operation_name = "Multiplication"
            elif operator == '/':
                try:
                    result = division(num1, num2)
                    operation_name = "Division"
                except ValueError as e:
                    print(f"❌ Error: {e}")
                    continue
            
            # Display result
            if result is not None:
                print(f"\n✅ {operation_name} Result: {num1} {operator} {num2} = {result}")
                
                # Show additional info for division
                if operator == '/' and num2 != 0:
                    print(f"   (Division: {num1} ÷ {num2} = {result})")
            
            # Ask if user wants to continue
            continue_calc = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
            if continue_calc not in ['y', 'yes']:
                print("👋 Thank you for using Calculator CLI. Goodbye!")
                break
                
        except KeyboardInterrupt:
            print("\n\n⏹️  Program interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")

def run_single_expression_mode():
    """
    Alternative mode: Calculate from a single expression string
    Example: "5 + 3" or "10 * 2.5"
    """
    print("\n" + "="*50)
    print("        SINGLE EXPRESSION MODE")
    print("="*50)
    print("Enter expressions like: 5 + 3, 10 * 2.5, etc.")
    print("Enter 'quit' to return to main menu")
    print("="*50)
    
    while True:
        try:
            expression = input("\nEnter expression: ").strip()
            
            if expression.lower() == 'quit':
                break
            
            # Remove any extra spaces and split
            parts = expression.split()
            
            if len(parts) != 3:
                print("❌ Invalid format! Use: number operator number")
                print("   Example: 5 + 3 or 10.5 * 2")
                continue
            
            num1_str, operator, num2_str = parts
            
            # Convert to numbers
            try:
                num1 = float(num1_str)
                num2 = float(num2_str)
            except ValueError:
                print("❌ Invalid numbers! Please enter valid numeric values.")
                continue
            
            # Validate operator
            if operator not in ['+', '-', '*', '/']:
                print("❌ Invalid operator! Please use one of: +, -, *, /")
                continue
            
            # Perform calculation
            result = None
            if operator == '+':
                result = addition(num1, num2)
            elif operator == '-':
                result = subtraction(num1, num2)
            elif operator == '*':
                result = multiplication(num1, num2)
            elif operator == '/':
                try:
                    result = division(num1, num2)
                except ValueError as e:
                    print(f"❌ Error: {e}")
                    continue
            
            if result is not None:
                print(f"✅ Result: {num1} {operator} {num2} = {result}")
                
        except KeyboardInterrupt:
            print("\n\n⏹️  Returning to main menu...")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")

def main():
    """
    Main program entry point with menu system
    """
    print("🚀 Starting Calculator CLI Application...")
    
    while True:
        print("\n" + "="*50)
        print("            CALCULATOR MAIN MENU")
        print("="*50)
        print("1. Standard Calculator Mode")
        print("2. Single Expression Mode")
        print("3. Exit")
        print("="*50)
        
        choice = input("Select mode (1-3): ").strip()
        
        if choice == '1':
            perform_calculation()
        elif choice == '2':
            run_single_expression_mode()
        elif choice == '3':
            print("👋 Thank you for using Calculator CLI. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please select 1, 2, or 3.")

# Additional utility functions
def calculate_expression(expression):
    """
    Calculate result from expression string
    
    Args:
        expression (str): Mathematical expression like "5 + 3"
        
    Returns:
        float: Calculation result or None if error
    """
    try:
        parts = expression.split()
        if len(parts) != 3:
            return None
        
        num1, operator, num2 = float(parts[0]), parts[1], float(parts[2])
        
        operations = {
            '+': addition,
            '-': subtraction,
            '*': multiplication,
            '/': division
        }
        
        if operator in operations:
            if operator == '/':
                return division(num1, num2)
            return operations[operator](num1, num2)
        
        return None
    except:
        return None

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Program terminated by user. Goodbye!")
    except Exception as e:
        print(f"💥 A critical error occurred: {e}")