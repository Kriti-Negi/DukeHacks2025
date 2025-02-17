import requests
import geoiff

GOOGLE_KEY = key

address = input("enter address: ")

#35.91295348401867, -79.04683940461153



response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GOOGLE_KEY}")

data = response.json()

latitude = data["results"][0]["geometry"]["location"]["lat"]
longitude = data["results"][0]["geometry"]["location"]["lng"]

print(f"Latitude: {latitude}, Longitude: {longitude}")

response = requests.get(f"https://solar.googleapis.com/v1/buildingInsights:findClosest?location.latitude={latitude}&location.longitude={longitude}&requiredQuality=HIGH&key={GOOGLE_KEY}")
data = response.json()

print('\nYearly Energy DC in K102 Country Club Rd, Chapel Hill, NC, USAwh:')
print(data["solarPotential"]['solarPanelConfigs'][1]['yearlyEnergyDcKwh'])
print('\n')

area_wholeroofstats = int(data['solarPotential']['wholeRoofStats']['areaMeters2'])
groundArea_buildingStats = int(data['solarPotential']["buildingStats"]["groundAreaMeters2"])
groundArea_wholeroofstats = int(data['solarPotential']['wholeRoofStats']['groundAreaMeters2'])
maxArrayArea = int(data['solarPotential']['maxArrayAreaMeters2'])

wholeBuildingRoofArea = area_wholeroofstats * (groundArea_buildingStats/groundArea_wholeroofstats)

geoiff.display_image(f'https://solar.googleapis.com/v1/dataLayers:get?location.latitude={latitude}&location.longitude={longitude}&radiusMeters=100&view=FULL_LAYERS&requiredQuality=HIGH&exactQualityRequired=true&pixelSizeMeters=0.5&key={GOOGLE_KEY}', key=GOOGLE_KEY)

