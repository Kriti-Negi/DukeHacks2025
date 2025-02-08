from electricity_cost import calculate_yearly_cost

DISCOUNT_RATE = 0.04  # Fixed discount rate of 4%
TAX_CREDIT = 0.30  # Federal tax credit (30%)


def calculate_npv(total_yearly_cost, discount_rate, years):
    """
    Calculate the Net Present Value (NPV) for a given yearly cost over a number of years with a discount rate.
    """
    npv = 0
    for year in range(1, years + 1):
        npv += total_yearly_cost / (1 + discount_rate) ** year
    return npv


def calculate_net_cost(upfront_cost, tax_credit):
    """
    Calculate the net cost of solar panel installation after applying tax credits.
    """
    return upfront_cost * (1 - tax_credit)


def main():
    """
    Main function for NPV analysis.
    """
    try:
        # User inputs
        user_bill = float(input("Enter your energy bill for a specific month: "))
        month = int(input("Enter the month as an integer (1-12): "))
        upfront_cost = float(input("Enter the total cost of solar panels and installation (e.g., $15000): "))

        # Calculate yearly cost (from electricity_cost.py)
        total_yearly_cost = calculate_yearly_cost(user_bill, month)

        # Calculate NPV for 25 years
        npv_25_years = calculate_npv(total_yearly_cost, DISCOUNT_RATE, 25)

        # Calculate net installation cost
        net_cost = calculate_net_cost(upfront_cost, TAX_CREDIT)

        # Display the results
        print(f"\nTotal Electricity Cost for 1 Year: ${total_yearly_cost:.2f}")
        print(f"Net Present Value (NPV) of 25-Year Costs (4% Discount Rate): ${npv_25_years:.2f}")
        print(f"Net Cost of Solar Installation After Tax Credit: ${net_cost:.2f}")

        # Compare savings and installation cost
        if npv_25_years > net_cost:
            print("The NPV of electricity savings exceeds the cost of installation. Solar panels are a good investment!")
        else:
            print("The NPV of electricity savings does not exceed the cost of installation. Solar panels may not be a good investment.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()