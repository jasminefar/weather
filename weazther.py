import random

# Step 1: Define weather data
weather_data = {
    "New York": {
        "Monday": "Sunny, 25°C",
        "Tuesday": "Cloudy, 22°C",
        "Wednesday": "Rainy, 19°C",
        "Thursday": "Sunny, 27°C",
        "Friday": "Windy, 20°C"
    },
    "Los Angeles": {
        "Monday": "Sunny, 30°C",
        "Tuesday": "Sunny, 32°C",
        "Wednesday": "Cloudy, 28°C",
        "Thursday": "Sunny, 29°C",
        "Friday": "Sunny, 31°C"
    },
    "Chicago": {
        "Monday": "Rainy, 18°C",
        "Tuesday": "Cloudy, 20°C",
        "Wednesday": "Windy, 15°C",
        "Thursday": "Sunny, 22°C",
        "Friday": "Rainy, 19°C"
    }
}

# Step 2: Function to display weather report
def display_weather_report(city, day):
    if city in weather_data:
        if day in weather_data[city]:
            print(f"Weather in {city} on {day}: {weather_data[city][day]}")
        else:
            print(f"Sorry, we don't have weather data for {day} in {city}.")
    else:
        print(f"Sorry, we don't have weather data for {city}.")

# Step 3: User interaction
def weather_report_generator():
    while True:
        city = input("Enter city name: ")
        day = input("Enter day of the week: ")
        
        display_weather_report(city, day)
        
        another_report = input("Do you want to generate another report? (yes/no): ").strip().lower()
        if another_report != "yes":
            print("Goodbye!")
            break

# Run the weather report generator
weather_report_generator()
