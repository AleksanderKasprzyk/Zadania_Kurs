import requests
import json
from datetime import datetime, timedelta

# API URL
api_url = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"

# Function to check the weather for a given date
def check_weather(latitude, longitude, searched_date=None):
    if not searched_date:
        # If no date is given, use the next day
        searched_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')

    # Create a unique filename based on the date
    filename = f"weather_{searched_date}.json"

    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        # If the file doesn't exist or is invalid, make a request to the API
        api_url_filled = api_url.format(latitude=latitude, longitude=longitude, searched_date=searched_date)
        response = requests.get(api_url_filled)

        if response.status_code == 200:
            data = response.json()
            # Save the API response to the file
            with open(filename, 'w') as file:
                json.dump(data, file)
        else:
            print("Failed to retrieve data from the API.")
            return "Don't know"

    # Check if there's rainfall information
    if 'daily' in data and 'rain_sum' in data['daily'] and searched_date in data['daily']['rain_sum']:
        rain_sum = data['daily']['rain_sum'][searched_date]
        if rain_sum > 0.0:
            return "It will rain"
        else:
            return "It will not rain"
    else:
        return "Don't know"

# Main program
if __name__ == "__main__":
    latitude = input("Enter latitude: ")  # Replace with the actual latitude
    longitude = input("Enter longitude: ")  # Replace with the actual longitude
    searched_date = input("Enter date (YYYY-mm-dd): ")

    result = check_weather(latitude, longitude, searched_date)
    print(f"Weather for {searched_date}: {result}")