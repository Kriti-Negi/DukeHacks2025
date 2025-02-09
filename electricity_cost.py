# Average electricity prices for the 12 months of the year
average_prices = [
    169.62, 139.95, 118.71, 110.03, 123.27,
    150.08, 173.16, 157.14, 123.93, 110.61,
    115.16, 137.56
]

def calculate_yearly_cost(user_bill, month):
    """
    Calculate the total electricity cost for a year given the user's bill for a specific month.
    Also returns the estimated cost per month.
    """
    if month < 1 or month > 12:
        raise ValueError("Invalid month. Please enter a value between 1 and 12.")

    # Calculate the ratio of user's bill to the average for the input month
    ratio = user_bill / average_prices[month - 1]

    # Calculate estimated costs for each month
    estimated_costs = [price * ratio for price in average_prices]

    # Return the total yearly cost and monthly estimates
    return sum(estimated_costs), estimated_costs


def main():
    """
    Main function to calculate yearly electricity cost and display monthly costs.
    """
    try:
        # User input
        user_bill = float(input("Enter your energy bill for a specific month: "))
        month = int(input("Enter the month as an integer (1-12): "))

        # Calculate yearly cost and monthly estimates
        total_yearly_cost, estimated_costs = calculate_yearly_cost(user_bill, month)

        # Display estimated monthly costs
        print("\nEstimated Monthly Electricity Costs:")
        for i, cost in enumerate(estimated_costs, start=1):
            print(f"Month {i}: ${cost:.2f}")

        # Display total yearly cost
        print(f"\nTotal Electricity Cost for 1 Year: ${total_yearly_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
