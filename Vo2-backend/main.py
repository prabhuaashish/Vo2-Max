from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import math

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Replace with your SvelteKit frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def VO2ToVel(x):
    return 29.54 + 5.000663 * x - 0.007546 * x * x

def timeConvert(speed):
    ans = (1 / speed) * 1000
    minutes = math.floor(ans)
    seconds = math.floor((ans - minutes) * 60)
    if (seconds > 9) :
        return f"{minutes}:{seconds}"
    else:
        # return '' + minutes + ':0' + seconds
        return f"{minutes}:0{seconds}"
    


class UserInput(BaseModel):
    race_distance_km: float
    finish_time_minutes: float

@app.post("/calculate_run_types/")
def calculate_run_types(user_data: UserInput):
    D = user_data.race_distance_km * 1000  # Convert to meters
    T = user_data.finish_time_minutes  # Keep time in minutes
    S = D / T  # Calculate speed in meters per minute

    vo2_max = (-4.60 + 0.182258 * S + 0.000104 * S**2) / (0.8 + 0.1894393 * math.exp(-0.012778 * T) + 0.2989558 * math.exp(-0.1932605 * T))

    easy_run_pace = VO2ToVel(vo2_max * 0.7)
    tempo_run_pace = VO2ToVel(vo2_max * 0.88)
    vo2_max_pace = VO2ToVel(vo2_max)
    speed_form_pace = VO2ToVel(vo2_max * 1.1)
    long_run_pace = VO2ToVel(vo2_max * 0.6)

    return {
        "VO2_max": vo2_max,
        "easy_run_pace":    timeConvert(easy_run_pace),
        "tempo_run_pace":   timeConvert(tempo_run_pace),
        "vo2_max_pace":     timeConvert(vo2_max_pace),
        "speed_form_pace":  timeConvert(speed_form_pace),
        "long_run_pace":    timeConvert(long_run_pace),
    }

