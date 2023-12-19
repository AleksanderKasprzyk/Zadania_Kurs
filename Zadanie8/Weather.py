import requests
import json
from datetime import datetime, timedelta

# Adres strony do darmowego serwera API Open Meteo
URL = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"

# Funkcja weather jest funkcją Pythona, która sprawdza pogodę dla danej szerokości i długości geograficznej oraz daty.
def weather(latitude, longitude, searched_date=None):
    # Jezeli nie podamy zadnej daty to wykona sie warunek "if not".
    if not searched_date:

        # Zapis dnia w formie dnia jutrzejszego.
        # Fragment kodu timedelta(days=1)).strftime('%Y-%m-%d') służy do obliczania daty następnego dnia i formatowania jej jako ciągu znaków w formacie "RRRR-MM-DD".

        searched_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    filename = f"Weather_for_{searched_date}.json"

    # Wyjatek try i except służy do otwarcia i odczytania danych z pliku oraz obsługi potencjalnych wyjątków, które mogą wystąpić podczas tego procesu.
    try:
        # Odczyt danych z pliku.
        with open(filename, mode='r') as file:
            data = json.load(file)

    # Json.decoder.JSONDecodeError sluzy do dekodowania danych z pliku, wyjatek zglasza problem z dekodowaniem jezeli natrafi na zly format danych.
    except (FileNotFoundError, json.decoder.JSONDecodeError):

        # Formatowanie danych, aby zastąpić latitude, longitude, searched_date odpowiednimi wartościami.
        API_URL = URL.format(latitude=latitude, longitude=longitude, searched_date=searched_date)
        response = requests.get(API_URL)

        # response.status_code sprawdza, czy strona API odpowiada na zapytanie ze strony uzytkownika. Numer 200 oznacza pomyslne zadanie.
        if response.status_code == 200:
            data = response.json()

            with open(filename, mode='w') as file:
                json.dump(data, file)
        else:
            print("Failed to retrieve data from the API.")
            return "Don't know"

    # Ta czesc funkcji weather przeanalizuje dane pogodowe uzyskane z odpowiedzi API.
    if 'daily' in data and 'rain_sum' in data['daily'] and searched_date in data['daily']['rain_sum']:
        rain_sum = data['daily']['rain_sum'][searched_date]
        if rain_sum > 0.0:
            return "It will rain"
        else:
            return "It will not rain"
    else:
        return "Don't know"

# if __name__ == "__main__":: - Sprawdza, czy skrypt jest uruchamiany jako główny program (nie zaimportowany jako moduł).
# Jeśli jest to główny program, kod wewnątrz tego bloku zostanie wykonany.
if __name__ == "__main__":
    latitude = input("Enter latitude: ")  # Replace with the actual latitude
    longitude = input("Enter longitude: ")  # Replace with the actual longitude
    searched_date = input("Enter date (YYYY-MM-DD): ")

# Ta linia wywołuje funkcję weather z podanymi danymi jako argumentami i zapisuje wynik w zmiennej result.
    result = weather(latitude, longitude, searched_date)
    print(f"Weather for {searched_date}: {result}")
