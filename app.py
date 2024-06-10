from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/weather')
def get_weather():
    api_key = 'YOUR_API_KEY_HERE'  # Replace with your actual API key
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to fetch weather data'}), response.status_code

def main():
    api_key = 'YOUR_API_KEY_HERE'  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    weather_data = get_weather(api_key, city)
    if weather_data:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Failed to fetch weather data.")


if __name__ == "__main__":
    app.run(debug=True)
