import requests
import json
from datetime import datetime, timedelta


class WeatherForecast:
    def __init__(self, latitude, longitude, file_name="Weather_dates.json"):
        self.latitude = latitude
        self.longitude = longitude
        self.file_name = file_name
        self.data = self.loading_file()

    def __setitem__(self, key, value):
        self.data[key] = value
        self.saving_file()

    def __getitem__(self, key):
        return self.data.get(key, "Don't know")

    def __iter__(self):
        return iter(self.data)

    def items(self):
        return self.data.items()

    def saving_file(self):
        with open(self.file_name, mode='w') as file_stream:
            json.dump(self.data, file_stream)

    def loading_file(self):
        try:
            with open(self.file_name, mode='r') as file_stream:
                return json.load(file_stream)
        except FileNotFoundError:
            return {}

    def query_weather(self, date):
        if date not in self.data:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={date}&end_date={date}"
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
                rain_sum = weather_data.get('daily', {}).get('rain_sum', [0])[0]
                if rain_sum > 0.0:
                    self[date] = "It will rain"
                elif rain_sum == 0.0:
                    self[date] = "It will not rain"
                else:
                    self[date] = "Don't know"


if __name__ == "__main__":
    latitude = input("Enter latitude: ")
    longitude = input("Enter longitude: ")
    weather_forecast = WeatherForecast(latitude, longitude)

    date = input("Enter a date (YYYY-MM-DD): ")
    if not date:
        tomorrow = datetime.now() + timedelta(days=1)
        date = tomorrow.strftime("%Y-%m-%d")

    result = weather_forecast[date]

    if result == "Don't know":
        weather_forecast.query_weather(date)
        result = weather_forecast[date]

    print(f"On {date}, {result}")

    print("\nStored weather data:")
    for date, weather in weather_forecast.items():
        print(f"{date}: {weather}")

    print("\nDates for which weather is known:")
    for date in weather_forecast:
        print(date)
