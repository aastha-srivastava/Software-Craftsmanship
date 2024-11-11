# Define a Calculator class
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Error! Division by zero."

    def display_menu(self):
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

    def perform_operation(self, choice, num1, num2):
        if choice == '1':
            return f"{num1} + {num2} = {self.add(num1, num2)}"
        elif choice == '2':
            return f"{num1} - {num2} = {self.subtract(num1, num2)}"
        elif choice == '3':
            return f"{num1} * {num2} = {self.multiply(num1, num2)}"
        elif choice == '4':
            return f"{num1} / {num2} = {self.divide(num1, num2)}"
        else:
            return "Invalid input! Please choose a valid operation."

# Main function to drive the calculator program
def main():
    calculator = Calculator()
    calculator.display_menu()
    
    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")
    
    # Check if the input is a valid choice
    if choice in ['1', '2', '3', '4']:
        # Take numbers from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Perform the operation and display the result
        result = calculator.perform_operation(choice, num1, num2)
        print(result)
    else:
        print("Invalid input! Please choose a valid operation.")

# Run the program
if __name__ == "__main__":
    main()
