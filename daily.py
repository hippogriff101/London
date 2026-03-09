import python_weather, asyncio, os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from datetime import datetime


load_dotenv()
app = App(token=os.environ["SLACK_BOT_TOKEN"])

async def main() -> str:
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get('London')
        temp = str(weather.temperature)
        kind = str(weather.kind)
        today = weather.daily_forecasts[0]
        highs = str(today.highest_temperature)
        lows = str(today.lowest_temperature)
        return temp, highs, lows, kind

def get_date() -> str:
    now = datetime.now()

    if now.day in [1, 21, 31]:
        prefix = 'st'
    elif now.day in [2, 22]:
        prefix = 'nd'
    elif now.day in [3, 23]:
        prefix = 'rd'
    else:
        prefix = 'th'

    full_date = now.strftime(f"Today is *%A %d{prefix} %B, %Y*.")

    return full_date

def greetings() -> str:
    now = datetime.now()
    hour = now.hour

    if 5 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    elif 18 <= hour < 22:
        return "Good evening!"
    else:
        return "Hello!"

def daily_msg() -> None:
    tempis = asyncio.run(main())
    full_date = get_date()
    app.client.chat_postMessage(
        channel=(os.environ["SLACK_CHANNEL"]),
        text=("_" + greetings() +"_\n" + full_date + "\nThe temperature in London is *" + tempis[0] + "°C* right now! My reports are telling me that it is `" + tempis[3] + "` now.\nToday's high is *" + tempis[1] + "°C* and the low is *" + tempis[2] + "°C*.")
    )

if __name__ == "__main__":
    daily_msg()
    print("Message sent to Slack channel at " + datetime.now().strftime("%H:%M:%S") + ".")