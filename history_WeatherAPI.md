```python
import requests
import json

# API key for the OpenWeatherMap API
api_key = "YOUR_API_KEY"

# Base URL for the API
base_url = "https://api.openweathermap.org/data/2.5/weather"

# City for which the weather is to be fetched
city = "London"

# Complete URL for the API call
url = f"{base_url}?q={city}&appid={api_key}"

# Make the API call
response = requests.get(url)

# Parse the JSON response
data = json.loads(response.text)

# Extract the current temperature
temperature = data["main"]["temp"] - 273.15

# Print the current temperature
print(f"The current temperature in {city} is {temperature} degrees Celsius.")
```