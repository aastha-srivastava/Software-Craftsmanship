# Define a SimpleInterestCalculator class
class SimpleInterestCalculator:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate(self):
        # Simple Interest formula: SI = (P * R * T) / 100
        return (self.principal * self.rate * self.time) / 100

    def display_result(self):
        # Calculate the Simple Interest
        si = self.calculate()
        # Display the result
        print(f"The Simple Interest is: ₹{si:.2f}")

# Main function to get input and display the result
def main():
    # Get user input for principal, rate, and time
    principal = float(input("Enter the principal amount: ₹"))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period (in years): "))

    # Create a SimpleInterestCalculator object
    calculator = SimpleInterestCalculator(principal, rate, time)

    # Display the result
    calculator.display_result()

# Run the program
if __name__ == "__main__":
    main()




