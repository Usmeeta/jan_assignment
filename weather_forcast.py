import requests
import json

# Function to fetch weather forecast data
def fetch_weather_forecast(city, api_key, days):
    url = f"https://api.open-meteo.com/v1/forecast"
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("Weather forecast data fetched successfully.")
        return response.json()  # Return the JSON data
    else:
        print(f"Failed to fetch weather data. Error: {response.status_code}")
        return None  # Return None if the request fails

# Function to save data to a file
def save_weather_data(data, file_name):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)  
    print(f"Weather forecast data saved to {file_name}")

# Main script
if __name__ == "__main__":  
    API_KEY = "your_api_key_here"  
    city_name = "New York"  
    forecast_days = 3  # Forecast for the next 3 days
    
    forecast_data = fetch_weather_forecast(city_name, API_KEY, forecast_days)
   
    if forecast_data:
        save_weather_data(forecast_data, "forecast_data.json")