from langchain.tools import Tool
import requests

def get_weather(city: str) -> str:
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        return response.text if response.ok else "Не вдалося отримати погоду."
    except Exception as e:
        return f"Помилка: {e}"

weather_tool = Tool.from_function(
    name="Weather Info Tool",
    description="Отримує поточну погоду в місті. Вхід — назва міста українською або англійською.",
    func=get_weather
)
