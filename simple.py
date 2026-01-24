import python_weather, asyncio

async def main() -> None:
    async with python_weather.Client(unit=python_weather.METRIC) as client: 
        weather = await client.get('London')
        print("It is " + str(weather.temperature) + "°C in "  + str(weather.location))  
if __name__ == '__main__':
  asyncio.run(main())