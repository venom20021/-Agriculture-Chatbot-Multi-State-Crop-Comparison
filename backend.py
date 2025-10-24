from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "enter you api key"
RESOURCE_ID = "35be999b-0208-4354-b557-f6ca9a5355de"

@app.get("/top_crops/{state}")
def get_top_crops(state: str):
    state_input = state.strip().title()
    url = f"https://api.data.gov.in/resource/{RESOURCE_ID}?api-key={API_KEY}&format=json&filters[state_name]={state_input}&limit=100"
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return {"error": f"API returned status code: {response.status_code}"}
        
        data = response.json()
        records = data.get("records", [])

        if not records:
            return {"error": f"No records found for state: {state_input}"}

        # Aggregate top 3 crops by production
        crops = {}
        for rec in records:
            crop_name = rec["crop"]
            production = float(rec.get("production_", 0))
            crops[crop_name] = crops.get(crop_name, 0) + production
        
        top_crops = sorted(crops.items(), key=lambda x: x[1], reverse=True)[:3]
        result = [{"state_name": state_input, "crop": c[0], "production_": c[1]} for c in top_crops]

        return {"top_crops": result, "source": f"https://data.gov.in/resource/{RESOURCE_ID}"}

    except Exception as e:
        return {"error": str(e)}

