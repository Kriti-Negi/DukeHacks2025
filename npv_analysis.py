DISCOUNT_RATE = 0.04  # Fixed discount rate of 4%
TAX_CREDIT = 0.30  # Federal tax credit (30%)
DEGRADATION_RATE = 0.005  # 0.5% efficiency loss per year

def calculate_npv(upfront_cost, yearly_savings, discount_rate, years):
    """
    Calculate the Net Present Value (NPV) of solar panel investment over a number of years.
    The initial investment is subtracted, and yearly savings are discounted.
    """
    npv = -upfront_cost  # Initial investment (negative cash flow at year 0)

    # Apply tax credit in Year 1 (not subtracted from upfront cost directly)
    npv += (TAX_CREDIT * upfront_cost) / (1 + discount_rate)

    for year in range(1, years + 1):
        adjusted_savings = yearly_savings * (1 - DEGRADATION_RATE) ** year  # Adjust for panel degradation
        npv += adjusted_savings / (1 + discount_rate) ** year  # Discounted yearly savings

    return npv

def calculate_net_cost(upfront_cost):
    """
    Calculate the net cost of solar panel installation before tax credit is applied.
    """
    return upfront_cost  # Tax credit is accounted for in NPV calculation separately.

def calculate_payback_period(upfront_cost, yearly_savings, discount_rate, years):
    """
    Calculate the payback period (number of years to recover investment).
    """
    total_savings = 0
    payback_years = 0

    for year in range(1, years + 1):
        adjusted_savings = yearly_savings * (1 - DEGRADATION_RATE) ** year
        total_savings += adjusted_savings / (1 + discount_rate) ** year
        
        if total_savings >= upfront_cost and payback_years == 0:
            payback_years = year

    return payback_years

def main():
    """
    Main function for NPV analysis.
    """
    try:
        # User inputs
        yearly_savings = float(input("Enter your expected yearly savings on electricity: "))
        upfront_cost = float(input("Enter the total cost of solar panels and installation (e.g., $15000): "))

        # Calculate NPV for 25 years
        npv_25_years = calculate_npv(upfront_cost, yearly_savings, DISCOUNT_RATE, 25)

        # Calculate payback period
        payback_period = calculate_payback_period(upfront_cost, yearly_savings, DISCOUNT_RATE, 25)

        # Display the results
        print(f"\nYearly Savings from Solar Panels: ${yearly_savings:.2f}")
        print(f"Net Cost of Solar Installation: ${upfront_cost:.2f}")
        print(f"Net Present Value (NPV) of 25-Year Savings (4% Discount Rate): ${npv_25_years:.2f}")
        print(f"Estimated Payback Period: {payback_period} years")

        # Determine if solar panels are a good investment
        if npv_25_years > 0:
            print("The NPV of electricity savings exceeds the cost of installation. Solar panels are a good investment!")
        else:
            print("The NPV of electricity savings does not exceed the cost of installation. Solar panels may not be a good investment.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
