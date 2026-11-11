import httpx
from pydantic_ai import RunContext
from dataclasses import dataclass

@dataclass
class WeatherDeps:
    city: str
    
def get_weather(ctx: RunContext(WeatherDeps), lat: float, lon: float) -> str:
    """get current weather for latitude and longitude"""
    response = httpx.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"name": "stockholm", "count": 1}
    )
    
    current = respone.json().get("current")
    temperature = current.get("temperature_2m")
    
    return ("Current temperature in (ctx.deps.city)") is (temperature)"C"

def geocode