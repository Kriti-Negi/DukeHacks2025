# Average electricity prices for the 12 months of the year
average_prices = [
    169.62, 139.95, 118.71, 110.03, 123.27, 
    150.08, 173.16, 157.14, 123.93, 110.61, 
    115.16, 137.56
]

def calculate_costs(user_bill, month):
    # Ensure the month is valid (1 to 12)
    if month < 1 or month > 12:
        return "Invalid month. Please enter a value between 1 and 12."

    # Calculate the ratio of user's bill to the average for the input month
    ratio = user_bill / average_prices[month - 1]

    # Calculate estimated costs for each month
    estimated_costs = [price * ratio for price in average_prices]

    # Calculate total costs
    total_yearly_cost = sum(estimated_costs)
    total_5_year_cost = total_yearly_cost * 5
    total_10_year_cost = total_yearly_cost * 10


    # Display the estimated costs per month
    print("\nEstimated Monthly Costs:")
    for i, cost in enumerate(estimated_costs, start=1):
        print(f"Month {i}: ${cost:.2f}")

    # Display yearly and 5-year totals
    print(f"\nTotal Electricity Cost for 1 Year: ${total_yearly_cost:.2f}")
    print(f"Total Electricity Cost for 5 Years: ${total_5_year_cost:.2f}")
    print(f"Total Electricity Cost for 10 Years: ${total_10_year_cost:.2f}")


# User input
try:
    user_bill = float(input("Enter your energy bill for a specific month: "))
    month = int(input("Enter the month as an integer (1-12): "))
    calculate_costs(user_bill, month)
except ValueError:
    print("Invalid input. Please enter numeric values for the energy bill and month.")
