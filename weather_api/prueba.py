from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = "https://nxxqxxiaiittdonaemkw.supabase.co"
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im54eHF4eGlhaWl0dGRvbmFlbWt3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE0MjcwNjYsImV4cCI6MjA2NzAwMzA2Nn0.40sJhwgjTVg5ics00cIq1VJy1pKHP1v6XfgrXTS6wV8'
OPENWEATHER_API_KEY = "8b872d6fff52762655ef14bbc60d337d"

url = SUPABASE_URL
key = SUPABASE_KEY

supabase = create_client(url, key)

data = {
    "city": "Prueba",
    "temperature": 24.5,
    "humidity": 40,
    "condition": "nublado"
}

result = supabase.table("brtech_prod.weather").insert(data).execute()
print(result)
