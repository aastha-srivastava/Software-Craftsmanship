# Function to calculate Simple Interest
def calculate_simple_interest(principal, rate, time):
    # Simple Interest formula: SI = (P * R * T) / 100
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Main function to get input and display the result
def main():
    # Get user input for principal, rate, and time
    principal = float(input("Enter the principal amount: ₹"))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period (in years): "))
    
    # Calculate Simple Interest
    si = calculate_simple_interest(principal, rate, time)
    
    # Display the result
    print(f"The Simple Interest is: ₹{si:.2f}")

# Run the program
if __name__ == "__main__":
    main()
