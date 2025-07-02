from fastapi import FastAPI
from supabase import  create_client, Client
import httpx
import os

app = FastAPI()

#Claves aqui
SUPABASE_URL = "https://nxxqxxiaiittdonaemkw.supabase.co"
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im54eHF4eGlhaWl0dGRvbmFlbWt3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE0MjcwNjYsImV4cCI6MjA2NzAwMzA2Nn0.40sJhwgjTVg5ics00cIq1VJy1pKHP1v6XfgrXTS6wV8'
OPENWEATHER_API_KEY = "8b872d6fff52762655ef14bbc60d337d"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/fetch_weather/")
async def fetch_weather(city: str = "Mexico City"):
    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
        )

        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            data = response.json()
        
        if response.status_code != 200:
            return{"error" : f"No se pudo obtener el clima : {data}"}
    
        
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description']

        #Guardado en SUPABASE
        supabase.table("weather").insert({
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "condition": condition,
        }).execute()

        return{
            "status" : "ok",
            "city" : city,
            "temperature" : temperature,
            "humidity" : humidity,
            "condition" : condition
        }
    except Exception as e:
        return {"error" : str(e)}
 




@app.get("/")
def home():
    return {"message": "Hola desde FastAPI"}
