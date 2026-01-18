import python_weather, asyncio

async def main() -> None:
    async with python_weather.Client(unit=python_weather.METRIC) as client: 
        weather = await client.get('London')
        print(str(weather.temperature) + "°C")
  
if __name__ == '__main__':
  asyncio.run(main())

# Code from https://pypi.org/project/python-weather/