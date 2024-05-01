                                                #Weather Forecast App

#Modules
import requests

#URL & API & Funtions
def get_weather(city):
    api_key = '8250f28bdce16e964d56504256299a7f'  # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return weather
    else:
        return None

def main():
    print("Welcome to the Weather App!")

    while True:
        city = input("Enter the city name (or 'q' to quit): ")

        if city.lower() == 'q':
            print("Exiting Weather App. Goodbye!")
            break

        weather = get_weather(city)

        if weather:
            print(f"Weather in {weather['city']}:")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Description: {weather['description']}")
        else:
            print("City not found. Please try again.")

if __name__ == "__main__":
    main()
