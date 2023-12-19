import requests
import os
import json
from datetime import datetime, timedelta

class WeatherForecast:
    def __init__(self, latitude, longitude):
        self.API_ENDPOINT = "https://api.open-meteo.com/v1/forecast"
        self.LATITUDE = latitude
        self.LONGITUDE = longitude
        self.data = {}
        self.load_data()

    def load_data(self):
        if os.path.exists("weather_data.json"):
            with open("weather_data.json", "r") as file:
                self.data = json.load(file)

    def save_data(self):
        with open("weather_data.json", "w") as file:
            json.dump(self.data, file)

    def query_weather_api(self, searched_date):
        formatted_date = searched_date.strftime("%Y-%m-%d")
        if formatted_date in self.data:
            return self.data[formatted_date]

        url = f"{self.API_ENDPOINT}?latitude={self.LATITUDE}&longitude={self.LONGITUDE}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={formatted_date}&end_date={formatted_date}"
        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.json()
            rain_sum = weather_data['daily'][0]['rain_sum']  # Access the first element of the list
            if rain_sum > 0.0:
                result = "It will rain"
            elif rain_sum == 0.0:
                result = "It will not rain"
            else:
                result = "Don't know"
            self.data[formatted_date] = result
            self.save_data()
            return result
        else:
            return "Don't know"

    def __setitem__(self, date, value):
        self.data[date] = value
        self.save_data()

    def __getitem__(self, date):
        return self.data.get(date, "Don't know")

    def __iter__(self):
        return iter(self.data)

    def items(self):
        return self.data.items()

def main():
    latitude = 51.5074  # Replace with your latitude
    longitude = -0.1278  # Replace with your longitude
    weather_forecast = WeatherForecast(latitude, longitude)

    while True:
        input_date = input("Enter the date in YYYY-mm-dd format (or press Enter for the next day): ")
        if not input_date:
            today = datetime.now()
            searched_date = today + timedelta(days=1)
        else:
            searched_date = datetime.strptime(input_date, "%Y-%m-%d")

        weather_result = weather_forecast.query_weather_api(searched_date)
        print(f"Weather for {searched_date.strftime('%Y-%m-%d')}: {weather_result}")

if __name__ == "__main__":
    main()