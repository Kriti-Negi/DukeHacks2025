# import flask module
import os
from flask import Flask, request, send_file
import requests
import math
from flask_cors import CORS
import subprocess

import geoiff
# instance of flask application
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT']=1
CORS(app)

average_prices = [
    169.62, 139.95, 118.71, 110.03, 123.27,
    150.08, 173.16, 157.14, 123.93, 110.61,
    115.16, 137.56
]

ROOF_PRICING = {
    "metal": 287,
    "shingles": 328,
    "concrete": 410,
    "clay": 410,
    "other": 400
}

DISCOUNT_RATE = 0.04  # Fixed discount rate of 4%
TAX_CREDIT = 0.30  # Federal tax credit (30%)
DEGRADATION_RATE = 0.005  # 0.5% efficiency loss per year

# Constants
PANEL_AREA_SQ_M = 1.825  # Square meters per panel

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

def calculate_yearly_savings(total_area, yearly_kwh_per_4_panels, ELECTRICITY_RATE):
    """
    Calculate yearly electricity savings based on available area and electricity rate.

    Args:
        total_area (float): Total available installation area in square meters.
        yearly_kwh_per_4_panels (float): Yearly energy production of 4 solar panels (kWh).

    Returns:
        tuple: Yearly savings ($) and number of panels installed.
    """
    # Calculate the number of solar panels that fit in the given area
    num_panels = math.floor(total_area / PANEL_AREA_SQ_M)

    # Calculate the yearly kWh output for all installed panels
    yearly_kwh_per_panel = yearly_kwh_per_4_panels / 4  # Convert 4-panel production to per-panel production
    total_yearly_kwh = num_panels * yearly_kwh_per_panel  # Total kWh generated by all installed panels

    # Calculate yearly savings based on electricity rate
    yearly_savings = total_yearly_kwh * ELECTRICITY_RATE 

    return yearly_savings, num_panels

# home route that returns below text when root url is accessed
@app.route("/")
def hello_world():
    data = {'message': 'Hello, world!', 'status': 'success'}
    return data

@app.route("/getEstimate")
def test():
    address = str(request.args.get("address"))
    material = str(request.args.get("material"))
    monthlyBill = int(request.args.get("bill"))
    month = int(request.args.get("monthID"))
    ELECTRICITY_RATE = float(request.args.get("solarCost")) # Cost per kWh ($/kWh)
    panelSize = float(request.args.get("panelSize"))

    PANEL_AREA_SQ_M = panelSize
    roofLevel = int(request.args.get("roofLevel"))

    GOOGLE_KEY = 'AIzaSyA9gmgZyfPk_axoIBafWssnWG3quLVahoY'

    response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GOOGLE_KEY}")

    data = response.json()

    latitude = data["results"][0]["geometry"]["location"]["lat"]
    longitude = data["results"][0]["geometry"]["location"]["lng"]

    print(f"Latitude: {latitude}, Longitude: {longitude}")

    response = requests.get(f"https://solar.googleapis.com/v1/buildingInsights:findClosest?location.latitude=37.4450&location.longitude=-122.1390&requiredQuality=HIGH&key={GOOGLE_KEY}")
    data = response.json()

    print('\nYearly Energy DC in Kwh:')
    yearly_kwh_per_4_panels = data["solarPotential"]['solarPanelConfigs'][1]['yearlyEnergyDcKwh']

    area_wholeroofstats = int(data['solarPotential']['wholeRoofStats']['areaMeters2'])
    groundArea_buildingStats = int(data['solarPotential']["buildingStats"]["groundAreaMeters2"])
    groundArea_wholeroofstats = int(data['solarPotential']['wholeRoofStats']['groundAreaMeters2'])

    #wholeBuildingRoofArea = area_wholeroofstats * (groundArea_buildingStats/groundArea_wholeroofstats)

    wholeBuildingRoofArea = int(data['solarPotential']['maxArrayAreaMeters2'])
    wholeBuildingRoofArea = wholeBuildingRoofArea / 13.8
    total_yearly_cost, estimated_costs = calculate_yearly_cost(monthlyBill, (month + 1))

    # Calculate costs
    total_installation_cost, num_panels = calculate_installation_cost(wholeBuildingRoofArea, material, roofLevel)

    # Calculate yearly savings
    yearly_savings, num_panels = calculate_yearly_savings(wholeBuildingRoofArea, yearly_kwh_per_4_panels, ELECTRICITY_RATE)

    # User inputs
    upfront_cost = total_installation_cost

    # Calculate NPV for 25 years
    npv_25_years = calculate_npv(upfront_cost, yearly_savings, DISCOUNT_RATE, 15)

    # Calculate payback period
    payback_period = calculate_payback_period(upfront_cost, yearly_savings, DISCOUNT_RATE, 25)

    ROI = (yearly_savings * 5 - (total_installation_cost))/total_installation_cost
    
    carbonFootprint = (yearly_kwh_per_4_panels * 1/4 * num_panels) * 0.639 #in lbs per house

    # Display the results
    print(f"\nYearly Savings from Solar Panels: ${yearly_savings:.2f}")
    print(f"Net Cost of Solar Installation: ${upfront_cost:.2f}")
    print(f"Net Present Value (NPV) of 25-Year Savings (4% Discount Rate): ${npv_25_years:.2f}")
    print(f"Estimated Payback Period: {payback_period} years")

    return {
        "totalYearlyCost": total_yearly_cost,
        "estimatedCost": estimated_costs,
        "totalInstallationCost": total_installation_cost,
        "yearlySavings": yearly_savings,
        "numPanels": num_panels,
        "npv": npv_25_years,
        "paybackPeriod": payback_period,
        "ROI": (ROI * 100),
        "area": wholeBuildingRoofArea,
        "carbonFootprintOffset": carbonFootprint
    }

@app.route("/giveImage")
def get_image():

    GOOGLE_KEY = 'AIzaSyA9gmgZyfPk_axoIBafWssnWG3quLVahoY'

    address = request.args.get("address")
    month = 6

    response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GOOGLE_KEY}")

    data = response.json()

    latitude = data["results"][0]["geometry"]["location"]["lat"]
    longitude = data["results"][0]["geometry"]["location"]["lng"]

    print(f"Latitude: {latitude}, Longitude: {longitude}")

    response = requests.get(f"https://solar.googleapis.com/v1/buildingInsights:findClosest?location.latitude={latitude}&location.longitude={longitude}&requiredQuality=HIGH&key={GOOGLE_KEY}")
    data = response.json()

    geoiff.display_image(f'https://solar.googleapis.com/v1/dataLayers:get?location.latitude={latitude}&location.longitude={longitude}&radiusMeters=100&view=FULL_LAYERS&requiredQuality=HIGH&exactQualityRequired=true&pixelSizeMeters=0.5&key={GOOGLE_KEY}', key=GOOGLE_KEY)
    
    filename = "../../hello.png"
    return send_file(path_or_file = filename)

if __name__ == '__main__':  
   app.run(debug=True)  