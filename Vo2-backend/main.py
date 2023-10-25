from fastapi import FastAPI, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from enum import Enum
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


class UserInput(BaseModel):
    race_distance_km: float
    finish_time_minutes: float

class RaceType(str, Enum):
    marathon = "marathon"
    half = "half"
    m10 = "10m"
    m10k = "10k"
    m5 = "5m"
    m5k = "5k"
    k3 = "3k"
    mile = "mile"
    m1500 = "1500"

class RaceTimeCalculation(BaseModel):
    frace: RaceType
    r1: RaceType
    r1t_hours: int
    r1t_minutes: int
    r1t_seconds: int
    r2: RaceType
    r2t_hours: int
    r2t_minutes: int
    r2t_seconds: int
    mpw: float
    dunits: str


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

def calculate_race_time(data: RaceTimeCalculation):
# Formulas to calculate race time
    # Access the relevant variables from the data parameter
    frace = data.frace
    r1 = data.r1
    r2 = data.r2
    r1t_hours = data.r1t_hours
    r1t_minutes = data.r1t_minutes
    r1t_seconds = data.r1t_seconds
    r2t_hours = data.r2t_hours
    r2t_minutes = data.r2t_minutes
    r2t_seconds = data.r2t_seconds
    mpw = data.mpw
    dunits = data.dunits

    # Function to convert time to seconds
    def to_seconds(h, m, s):
        return h * 3600 + m * 60 + s
    
    # Function to convert time to string formatted HH::MM::SS

    def time_display(s):
        hours, remainder = divmod(s, 3600)
        minutes, seconds = divmod(remainder, 60)
        formatted_time = ""
        if hours:
            formatted_time += f"{int(hours):02d}:"
        if minutes or formatted_time:
            formatted_time += f"{int(minutes):02d}:{int(seconds):02d}"
        else:
            formatted_time += f"{int(seconds):02d}"
        return formatted_time

    r1t = to_seconds(r1t_hours, r1t_minutes, r1t_seconds)
    r2t = to_seconds(r2t_hours, r2t_minutes, r2t_seconds)
    
    # Function to convert KM to Miles
    def to_miles(dist, unit):
        return dist if unit == 'mi' else dist / 0.621371192

    # Dictionary to map race distances to miles
    race_distances = {
        'marathon': 26.21875,
        'half': 13.109375,
        '10m': 10,
        '10k': 6.21371192,
        '5m': 5,
        '5k': 3.10685596,
        '3k': 1.864113576,
        'mile': 1,
        '1500': 0.932056788,
    }

    frace_miles = race_distances.get(frace, 0)
    r1_miles = race_distances.get(r1, 0)
    r2_miles = race_distances.get(r2, 0)

    if r2_miles and r2_miles < r1_miles:
        r1, r2 = r2, r1
        r1t, r2t = r2t, r1t
        r1_miles, r2_miles = r2_miles, r1_miles


    if r1_miles:
        r1_pace = r1t / r1_miles

        if not (210 <= r1_pace <= 960):
            return ('The pace calculated time falls outside the limits of this tool.')

    if r2_miles:
        r2_pace = r2t / r2_miles
        if not (210 <= r2_pace <= 960):
            return ('The pace calculated time falls outside the limits of this tool.')

    if mpw:
        mpw = round(mpw)
        if not mpw or mpw < 5 or mpw > 150:
            return ('Invalid weekly training distance.')
        if dunits == 'km':
            mpw *= 0.621371
    
    if frace == r1 or frace == r2 or r1 == r2:
        return ('Invalid race distances.')

    if frace == 'marathon':
        if r2 and r2t and mpw:
            eq = 'm2'
        elif mpw:
            eq = 'm1'
        else:
            eq = 'r106'
    else:
        eq = 'r106'
    

    if eq == 'r106':
        b = frace_miles / r1_miles
        pt = r1t * math.pow(b, 1.06)
    elif eq == 'm1':
        r1_meters = r1_miles * 1609.34
        velocity_riegel = 42195 / (r1t * math.pow(42195 / r1_meters, 1.07))
        velocity_model1 = 0.16018617 + 0.83076202 * velocity_riegel + 0.06423826 * (mpw / 10)
        pt = 42195 / 60 / velocity_model1 * 60
    elif eq == 'm2':
        r1_meters = r1_miles * 1609.34
        r2_meters = r2_miles * 1609.34
        kr2r1 = math.log(r2t / r1t) / math.log(r2_meters / r1_meters)
        prek = 1.4510756 + -0.23797948 * kr2r1 + -0.01410023 * (mpw / 10)
        pt = r2t * math.pow(42195 / r2_meters, prek)
    else:
        return ('Oops! Something went wrong. Please try again.')

    pt_hms = time_display(pt)
    frace_km = frace_miles * 1.60934
    pace_mile_seconds = int(pt / frace_miles)
    pace_mile = time_display(pace_mile_seconds)

    pace_km_seconds = int(pt / frace_km)
    pace_km = time_display(pace_km_seconds)

    # Format pace values as "MM:SS/mile" and "MM:SS/km"
    pace_mile_formatted = f"{pace_mile}/mile"
    pace_km_formatted = f"{pace_km}/km"

    return {
        "predictedTime": pt_hms,
        "frace": data.frace,
        "paceMile": pace_mile_formatted,
        "paceKm": pace_km_formatted,
    }



@app.post("/calculate_run_types/")
def calculate_run_types(user_data: UserInput):
    D = user_data.race_distance_km * 1000  # Convert to meters
    T = user_data.finish_time_minutes  # Keep time in minutes
    S = D / T  # Calculate speed in meters per minute

    vo2_max = (-4.60 + 0.182258 * S + 0.000104 * S**2) / (0.8 + 0.1894393 * math.exp(-0.012778 * T) + 0.2989558 * math.exp(-0.1932605 * T))
    return calculate_run_types_from_Vo2(vo2_max)

@app.get("/calculate_run_types_from_Vo2/")
def calculate_run_types_from_Vo2(vo2_max:float):
    easy_run_pace = VO2ToVel(vo2_max * 0.7)
    tempo_run_pace = VO2ToVel(vo2_max * 0.88)
    vo2_max_pace = VO2ToVel(vo2_max)
    speed_form_pace = VO2ToVel(vo2_max * 1.1)
    long_run_pace = VO2ToVel(vo2_max * 0.6)

    return {
        "VO2_max": vo2_max,
        "easy_run_pace":    timeConvert(easy_run_pace) ,
        "tempo_run_pace":   timeConvert(tempo_run_pace),
        "vo2_max_pace":     timeConvert(vo2_max_pace),
        "speed_form_pace":  timeConvert(speed_form_pace),
        "long_run_pace":    timeConvert(long_run_pace),
    }

@app.post("/calculate-race-time/")
async def calculate_race_time_route(data: RaceTimeCalculation):
    result = calculate_race_time(data)
    return JSONResponse(content=result)


