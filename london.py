import python_weather, asyncio, os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


load_dotenv()
app = App(token=os.environ["SLACK_BOT_TOKEN"])

async def main() -> str:
    async with python_weather.Client(unit=python_weather.METRIC) as client: 
        weather = await client.get('London')
        weatheris = ("It is " + str(weather.temperature) + "°C in "  + str(weather.location))  
        return weatheris

@app.command("/weather")
def weather_command(ack, respond):
    print("Weather command invoked")
    ack()

    respond(
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": asyncio.run(main())
                }
            },
        ]
    )

if __name__ == "__main__":
    SocketModeHandler(
        app,
        os.getenv("SLACK_APP_TOKEN")
    ).start()