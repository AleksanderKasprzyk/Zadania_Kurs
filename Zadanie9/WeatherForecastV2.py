import requests
import json
from datetime import date, timedelta, datetime


class WeatherForecast:
    def __init__(self):
        self.weather_forecast = {}

    def __iter__(self):
        return self.weather_forecast.items()

    def __setitem__(self, key, value):
        self.weather_forecast[key] = value

    def __getitem__(self, key):
        return self.weather_forecast[key]

    def items(self):
        return self.weather_forecast.items()

    def weather_date(self, latitude, longitude, searched_date=None):
        URL = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
        API_URL = URL.format(latitude=latitude, longitude=longitude, searched_date=searched_date)
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            daily_rain_sum = data['daily']['rain_sum']
            if searched_date in daily_rain_sum:
                rainfall = daily_rain_sum[searched_date]
                return rainfall
            else:
                return "Don't know"
        else:
            return "Don't know"

def main():
    today = datetime.now()
    next_day = today + timedelta(days=1)
    date_format = "%Y-%m-%d"
    input_date = input(f"Enter a date in YYYY-MM-DD format (default is {next_day.strftime(date_format)}): ")
    if not input_date:
        searched_date = next_day.strftime(date_format)
    else:
        try:
            searched_date = datetime.strptime(input_date, date_format).strftime(date_format)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")
            return
    file_path = "weather_results.json"
    try:
        with open(file_path, "r") as file:
            weather_results = json.load(file)
    except FileNotFoundError:
        weather_results = {}

    if searched_date in weather_results:
        result = weather_results[searched_date]
    else:
        weather_forecast = WeatherForecast()
        result = weather_forecast.weather_date(latitude, longitude, searched_date)
        weather_results[searched_date] = result
        with open(file_path, "w") as file:
            json.dump(weather_results, file)

    if result == "Don't know":
        print("Weather information not available for the selected date.")
    elif result > 0.0:
        print(f"It will rain on {searched_date}.")
    else:
        print(f"It will not rain on {searched_date}.")


if __name__ == "__main__":

    latitude = input("Enter latitude: ")  # Replace with the actual latitude
    longitude = input("Enter longitude: ")  # Replace with the actual longitude
    main()
