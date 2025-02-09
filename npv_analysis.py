DISCOUNT_RATE = 0.04  # Fixed discount rate of 4%
TAX_CREDIT = 0.30  # Federal tax credit (30%)


def calculate_npv(upfront_cost, yearly_savings, discount_rate, years):
    """
    Calculate the Net Present Value (NPV) of solar panel investment over a number of years.
    The initial investment is subtracted, and yearly savings are discounted.
    """
    npv = -upfront_cost  # Initial investment (negative cash flow at year 0)
    
    for year in range(1, years + 1):
        npv += yearly_savings / (1 + discount_rate) ** year  # Discounted yearly savings
    
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
        yearly_savings = float(input("Enter your expected yearly savings on electricity: "))
        upfront_cost = float(input("Enter the total cost of solar panels and installation (e.g., $15000): "))

        # Calculate net installation cost after tax credit
        net_cost = calculate_net_cost(upfront_cost, TAX_CREDIT)

        # Calculate NPV for 25 years
        npv_25_years = calculate_npv(net_cost, yearly_savings, DISCOUNT_RATE, 25)

        # Display the results
        print(f"\nYearly Savings from Solar Panels: ${yearly_savings:.2f}")
        print(f"Net Cost of Solar Installation After Tax Credit: ${net_cost:.2f}")
        print(f"Net Present Value (NPV) of 25-Year Savings (4% Discount Rate): ${npv_25_years:.2f}")

        # Determine if solar panels are a good investment
        if npv_25_years > 0:
            print("The NPV of electricity savings exceeds the cost of installation. Solar panels are a good investment!")
        else:
            print("The NPV of electricity savings does not exceed the cost of installation. Solar panels may not be a good investment.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()