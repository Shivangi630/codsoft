#TASK2 CALCULATOR

# Define a simple calculator function
def calculator():
# Prompt user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
# Display available operations
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
 # Prompt user for operation choice
    choice = input("Enter choice (1/2/3/4): ")

# Perform the chosen operation
    if choice == '1':
        result = num1 + num2
    elif choice == '2':
        result = num1 - num2
    elif choice == '3':
        result = num1 * num2
    elif choice == '4':
# Check for division by zero
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero."
    else:
        result = "Invalid input"

# Display the result
    print(f"Result: {result}")

# Call the calculator function
calculator()