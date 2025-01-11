import python_weather
import asyncio

async def get_weather_data(location, unit):
    # Set the unit system based on user input
    if unit.lower() == 'metric':
        unit_system = python_weather.METRIC
    else:
        unit_system = python_weather.IMPERIAL

    async with python_weather.Client(unit=unit_system) as client:
        weather = await client.get(location)
        return weather

def print_weather_data(weather, unit):
    print(f"Current weather in {weather.location.city}, {weather.location.region}:")
    print(f"  Condition: {weather.current.description}")
    print(f"  Temperature: {weather.current.temperature} {'C' if unit == 'metric' else 'F'}")
    print(f"  Humidity: {weather.current.humidity}%")
    print(f"  Wind speed: {weather.current.wind_speed} {'km/h' if unit == 'metric' else 'mph'}")

    print("\n5-day Forecast:")
    for forecast in weather.forecasts:
        print(f"  Date: {forecast.date}")
        print(f"    Condition: {forecast.sky_text}")
        print(f"    High: {forecast.high} {'C' if unit == 'metric' else 'F'}")
        print(f"    Low: {forecast.low} {'C' if unit == 'metric' else 'F'}")

async def main():
    location = input("Enter location: ")
    unit = input("Enter unit (metric or imperial): ")
    weather = await get_weather_data(location, unit)
    print_weather_data(weather, unit)

if __name__ == "__main__":
    asyncio.run(main())
