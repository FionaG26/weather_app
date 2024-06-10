from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/weather')
def fetch_weather():
    api_key = 'YOUR_API_KEY_HERE'  # Replace with your actual API key
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    weather_data = get_weather(api_key, city)
    if weather_data:
        return jsonify(weather_data)
    else:
        return jsonify({'error': 'Failed to fetch weather data'}), 500

if __name__ == "__main__":
    app.run(debug=True)
