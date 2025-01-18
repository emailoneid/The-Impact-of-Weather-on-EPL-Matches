from meteostat import Stations
from datetime import datetime
from meteostat import Hourly

# Create a Stations object
stations = Stations()

# Fetch all stations
stations_data = stations.fetch()

# Filter for the London weather station using its ID
london_station = stations_data.loc['03547'] if '03547' in stations_data.index else None

# Print the relevant information if found
if london_station is not None:
    selected_info = {
        'Name': london_station['name'],
        'WMO': london_station['wmo'],
        'Latitude': london_station['latitude'],
        'Longitude': london_station['longitude']
    }

    # Print the formatted output
    print("London Weather Station Information:")
    for key, value in selected_info.items():
        print(f"{key}: {value}")
else:
    print("London weather station not found.")

start = datetime(2019, 8, 9)
end = datetime(2024, 5, 19, 23, 59)

# Get hourly data
data = Hourly('03547', start, end)
data = data.fetch()

# Convert timestamps to string format if necessary
data.index = data.index.astype(str)  # Convert the index (timestamps) to strings

# Save to JSON
data.to_json('london_weather_data.json', orient='records', lines=True)

print("Data saved to 'london_weather_data.json'.")