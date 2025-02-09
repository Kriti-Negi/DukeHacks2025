import math

# Pricing per roof type (installation cost per panel)
ROOF_PRICING = {
    "metal": 287,
    "shingles": 328,
    "concrete": 410,
    "clay": 410,
    "other": 400
}

# New panel area in square meters
PANEL_AREA_SQ_M = 1.82  # Square meters per panel

def calculate_installation_cost(square_meters, roof_type, roof_level):
    """
    Calculate the installation cost based on square meter area, roof type, and roof level.

    Args:
        square_meters (float): Total square meter area available for solar panels.
        roof_type (str): Type of roof (metal, shingles, concrete, clay, other).
        roof_level (int): Number of stories of the building.

    Returns:
        tuple: Total installation cost, number of panels
    """
    # Validate roof type
    roof_type = roof_type.lower()
    if roof_type not in ROOF_PRICING:
        raise ValueError("Invalid roof type. Choose from: metal, shingles, concrete, clay, other.")

    # Calculate the number of panels that fit in the given square meter area
    num_panels = math.floor(square_meters / PANEL_AREA_SQ_M)

    # Get the base installation price per panel for the selected roof type
    base_install_cost_per_panel = ROOF_PRICING[roof_type]

    # Calculate base installation cost (without roof level multiplier)
    base_installation_cost = num_panels * base_install_cost_per_panel

    # Apply additional cost for multi-story buildings
    if roof_level > 1:
        additional_percentage = (roof_level - 1) * 0.15  # Each extra floor adds 15%
        adjusted_installation_cost = base_installation_cost * (1 + additional_percentage)
    else:
        adjusted_installation_cost = base_installation_cost  # No extra cost for 1st floor

    return adjusted_installation_cost, num_panels

def main():
    """
    Main function to take user input and calculate installation cost.
    """
    try:
        # Get user inputs
        square_meters = float(input("Enter the total square meters available for installation: "))
        roof_type = input("Enter the roof type (metal, shingles, concrete, clay, other): ").strip().lower()
        roof_level = int(input("Enter the number of stories of the building: "))

        # Calculate costs
        total_installation_cost, num_panels = calculate_installation_cost(square_meters, roof_type, roof_level)

        # Display results
        print(f"\nTotal number of panels that fit: {num_panels}")
        print(f"Total installation cost for {roof_type.capitalize()} roof on a {roof_level}-story building: ${total_installation_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
