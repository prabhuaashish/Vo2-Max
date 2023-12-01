from fastapi import HTTPException
from sqlalchemy.orm import Session
import math
from .. import schemas, models
from fastapi.responses import JSONResponse


def save_race_time(data: schemas.RaceTimeCalculation, user_id:str, db: Session):
    # Formulas to calculate race time

    # Access the relevant variables from the data parameter
    frace = data.frace
    r1 = data.r1
    r2 = data.r2
    r1t_hours = int(data.r1t_hours) if data.r1t_hours else 0
    r1t_minutes = int(data.r1t_minutes) if data.r1t_minutes else 0
    r1t_seconds = int(data.r1t_seconds) if data.r1t_seconds else 0
    r2t_hours = int(data.r2t_hours) if data.r2t_hours else 0
    r2t_minutes = int(data.r2t_minutes) if data.r2t_minutes else 0
    r2t_seconds = int(data.r2t_seconds) if data.r2t_seconds else 0
    mpw = float(data.mpw) if data.mpw else 0.0  # Convert to float
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
        'half_marathon': 13.109375,
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
    pt_hms_formatted = str(pt_hms)

    # Create an instance of the RaceTimePrediction model
    race_time_prediction = models.RaceTimePrediction(
        goal_race=data.frace,
        recent_race=data.r1,
        r1t_hours=r1t_hours,
        r1t_minutes=r1t_minutes,
        r1t_seconds=r1t_seconds,
        another_race=data.r2,
        r2t_hours=r2t_hours,
        r2t_minutes=r2t_minutes,
        r2t_seconds=r2t_seconds,
        milage_per_week=data.mpw,
        dunits=dunits,
        predicted_time=pt_hms_formatted,
        pace_mile=pace_mile_formatted,
        pace_km=pace_km_formatted,
        user_id=user_id
    )

    # Add the instance to the database session and commit
    db.add(race_time_prediction)
    db.commit()
    db.refresh(race_time_prediction)

    # Return the calculated race time and other data
    return {
        "predictedTime": pt_hms,
        "frace": data.frace,
        "paceMile": pace_mile_formatted,
        "paceKm": pace_km_formatted,
    }

def calculate_race_time(data: schemas.RaceTimeCalculation):
    # Formulas to calculate race time

    # Access the relevant variables from the data parameter
    frace = data.frace
    r1 = data.r1
    r2 = data.r2
    r1t_hours = int(data.r1t_hours) if data.r1t_hours else 0
    r1t_minutes = int(data.r1t_minutes) if data.r1t_minutes else 0
    r1t_seconds = int(data.r1t_seconds) if data.r1t_seconds else 0
    r2t_hours = int(data.r2t_hours) if data.r2t_hours else 0
    r2t_minutes = int(data.r2t_minutes) if data.r2t_minutes else 0
    r2t_seconds = int(data.r2t_seconds) if data.r2t_seconds else 0
    mpw = float(data.mpw) if data.mpw else 0.0  # Convert to float
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
        'half_marathon': 13.109375,
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
    pt_hms_formatted = str(pt_hms)

    # Return the calculated race time and other data
    return {
        "predictedTime": pt_hms,
        "frace": data.frace,
        "paceMile": pace_mile_formatted,
        "paceKm": pace_km_formatted,
    }


def VO2ToVel(x):
    return 29.54 + 5.000663 * x - 0.007546 * x * x

def timeConvert(speed, pace_type):
    if pace_type == "min/km":
        ans = (1 / speed) * 1000
    else:
        ans = (1 / speed) * 1609
        
    minutes = math.floor(ans)
    seconds = math.floor((ans - minutes) * 60)
    if (seconds > 9) :
        return f"{minutes}:{seconds}"
    else:
        # return '' + minutes + ':0' + seconds
        return f"{minutes}:0{seconds}"

def save_run_types(user_data: schemas.RunType, db:Session, user_id: str):
    if user_data.units == "km": 
        D = user_data.race_distance* 1000  # Convert to meters
    else:
        D = user_data.race_distance* 1609  # Convert to meters

    finishTime = user_data.finish_time_hours * 60 + user_data.finish_time_minutes + user_data.finish_time_seconds / 60

    T =  finishTime # Keep time in minutes
    
    if T == 0:
        # Handle the case where finish_time_minutes is zero
        return {"error": "Finish time cannot be zero."}
    
    S = D / T  # Calculate speed in meters per minute

    vo2_max = (-4.60 + 0.182258 * S + 0.000104 * S**2) / (0.8 + 0.1894393 * math.exp(-0.012778 * T) + 0.2989558 * math.exp(-0.1932605 * T))
    
    # Create a new instance of the PacePrediction model
    run_type_pace_prediction = models.PacePrediction(
        recent_race_distance = user_data.race_distance,
        units = user_data.units,
        finish_time_hours = user_data.finish_time_hours,
        finish_time_minutes = user_data.finish_time_minutes,
        finish_time_seconds = user_data.finish_time_seconds,
        pace_type = user_data.pace_type,
        type = user_data.type,
        vdot = round(vo2_max, 2),
        user_id=user_id
    )

    db.add(run_type_pace_prediction)
    db.commit()

    if user_data.type == "Daniels_old":
        result = models.DanielsOldRaceTimePrediction(**daniels_old_run_types(vo2_max, user_data.pace_type, run_type_pace_prediction.id))
        
    elif user_data.type == "Daniels_new":
        result = models.DanielsNewRaceTimePrediction(**daniels_new_run_types(vo2_max, user_data.pace_type, run_type_pace_prediction.id))
        
    elif user_data.type == "Pfitzinger":
        result = models.PfitzingerRaceTimePrediction(**pfitzinger_run_types(vo2_max, user_data.pace_type, run_type_pace_prediction.id))
        
    elif user_data.type == "Matt_Fitzgerald":
        result = models.MattFitzgeraldRaceTimePrediction(**matt_fitzgerald_run_types(vo2_max, user_data.pace_type, run_type_pace_prediction.id))
    
    db.add(result)
    db.commit()
    db.refresh(run_type_pace_prediction)


    if user_data.type == "Daniels_new" :
        return vo2_max, daniels_new_run_types(vo2_max, user_data.pace_type, run_type_pace_prediction.id)
    elif user_data.type == "Pfitzinger" :
        return vo2_max, pfitzinger_run_types(vo2_max, user_data.pace_type, run_type_pace_prediction.id)
    elif user_data.type == "Matt_Fitzgerald" :
        return vo2_max, matt_fitzgerald_run_types(vo2_max, user_data.pace_type, run_type_pace_prediction.id)
    else:
        return vo2_max, daniels_old_run_types(vo2_max, user_data.pace_type, run_type_pace_prediction.id)

def calculate_run_types(user_data: schemas.RunType):
    if user_data.units == "km": 
        D = user_data.race_distance* 1000  # Convert to meters
    else:
        D = user_data.race_distance* 1609  # Convert to meters

    finishTime = user_data.finish_time_hours * 60 + user_data.finish_time_minutes + user_data.finish_time_seconds / 60

    T =  finishTime # Keep time in minutes
    
    if T == 0:
        # Handle the case where finish_time_minutes is zero
        return {"error": "Finish time cannot be zero."}
    
    S = D / T  # Calculate speed in meters per minute

    vo2_max = (-4.60 + 0.182258 * S + 0.000104 * S**2) / (0.8 + 0.1894393 * math.exp(-0.012778 * T) + 0.2989558 * math.exp(-0.1932605 * T))

    id = 1

    if user_data.type == "Daniels_new" :
        return vo2_max, daniels_new_run_types(vo2_max, user_data.pace_type, id)
    elif user_data.type == "Pfitzinger" :
        return vo2_max, pfitzinger_run_types(vo2_max, user_data.pace_type, id)
    elif user_data.type == "Matt_Fitzgerald" :
        return vo2_max, matt_fitzgerald_run_types(vo2_max, user_data.pace_type, id)
    else:
        return vo2_max, daniels_old_run_types(vo2_max, user_data.pace_type, id)

def daniels_old_run_types(vo2_max:float, pace_type: str, id: int):   
    easy_run_pace = VO2ToVel(vo2_max * 0.7)
    tempo_run_pace = VO2ToVel(vo2_max * 0.88)
    vo2_max_pace = VO2ToVel(vo2_max)
    speed_form_pace = VO2ToVel(vo2_max * 1.1)
    long_run_pace = VO2ToVel(vo2_max * 0.6)
    return {
        "easy_run_pace":    f"{timeConvert(easy_run_pace, pace_type)} {pace_type}",
        "tempo_run_pace":   f"{timeConvert(tempo_run_pace, pace_type)} {pace_type}",
        "vo2_max_pace":     f"{timeConvert(vo2_max_pace, pace_type)} {pace_type}",
        "speed_form_pace":  f"{timeConvert(speed_form_pace, pace_type)} {pace_type}",
        "long_run_pace":    f"{timeConvert(easy_run_pace, pace_type)} - {timeConvert(long_run_pace, pace_type)} {pace_type}",
        "pace_prediction_id": id
    }

def daniels_new_run_types(vo2_max:float, pace_type: str, id: int):
    Easy_min = VO2ToVel(vo2_max * 0.59)
    Easy_max = VO2ToVel(vo2_max * 0.74)
    Marathon_min = VO2ToVel(vo2_max * 0.75)
    Marathon_max = VO2ToVel(vo2_max * 0.84)
    Threshold_min = VO2ToVel(vo2_max * 0.83)
    Threshold_max = VO2ToVel(vo2_max * 0.88)
    Interval_min = VO2ToVel(vo2_max * 0.95)
    Interval_max = VO2ToVel(vo2_max * 1)
    Repetition_min = VO2ToVel(vo2_max * 1.05)
    Repetition_max = VO2ToVel(vo2_max * 1.1)

    return {
        "easy_run_pace": f"{timeConvert(Easy_max, pace_type)} - {timeConvert(Easy_min, pace_type)} {pace_type}",
        "marathon_pace": f"{timeConvert(Marathon_max, pace_type)} - {timeConvert(Marathon_min, pace_type)} {pace_type}",
        "threshold_pace": f"{timeConvert(Threshold_max, pace_type)} - {timeConvert(Threshold_min, pace_type)} {pace_type}",
        "interval_pace": f"{timeConvert(Interval_max, pace_type)} - {timeConvert(Interval_min, pace_type)} {pace_type}",
        "repetition_pace": f"{timeConvert(Repetition_max, pace_type)} - {timeConvert(Repetition_min, pace_type)} {pace_type}",
        "pace_prediction_id": id
    }

def pfitzinger_run_types(vo2_max:float, pace_type: str, id: int):
    Recovery = VO2ToVel(vo2_max * 0.7)
    Aerobic_min = VO2ToVel(vo2_max * 0.64)
    Aerobic_max = VO2ToVel(vo2_max * 0.75)
    Long_Medium_min = VO2ToVel(vo2_max * 0.69)
    Long_Medium_max = VO2ToVel(vo2_max * 0.78)
    Marathon_min = VO2ToVel(vo2_max * 0.73)
    Marathon_max = VO2ToVel(vo2_max * 0.83)
    Lactate_threshold_min = VO2ToVel(vo2_max * 0.90)
    Lactate_threshold_max = VO2ToVel(vo2_max * 0.92)
    VO2_min = VO2ToVel(vo2_max * 0.95)
    VO2_max = VO2ToVel(vo2_max * 1)

    return {
        "recovery_run_pace": f"{timeConvert(Recovery, pace_type)} {pace_type}",
        "aerobic_run_pace": f"{timeConvert(Aerobic_max, pace_type)} - {timeConvert(Aerobic_min, pace_type)} {pace_type}",
        "long_medium_run_pace": f"{timeConvert(Long_Medium_max, pace_type)} - {timeConvert(Long_Medium_min, pace_type)} {pace_type}",
        "marathon_pace": f"{timeConvert(Marathon_max, pace_type)} - {timeConvert(Marathon_min, pace_type)} {pace_type}",
        "lactate_threshold_pace": f"{timeConvert(Lactate_threshold_max, pace_type)} - {timeConvert(Lactate_threshold_min, pace_type)} {pace_type}",
        "vo2max_pace": f"{timeConvert(VO2_max, pace_type)} - {timeConvert(VO2_min, pace_type)} {pace_type}",
        "pace_prediction_id": id
    }

def matt_fitzgerald_run_types(vo2_max:float, pace_type: str, id: int):
    Gray_zone_1 = VO2ToVel(vo2_max * 0.55)
    Low_Aerobic_min = VO2ToVel(vo2_max * 0.55)
    Low_Aerobic_max = VO2ToVel(vo2_max * 0.65)
    Moderate_Aerobic_min = VO2ToVel(vo2_max * 0.65)
    Moderate_Aerobic_max = VO2ToVel(vo2_max * 0.75)
    High_Aerobic_min = VO2ToVel(vo2_max * 0.75)
    High_Aerobic_max = VO2ToVel(vo2_max * 0.85)
    Threshold_min = VO2ToVel(vo2_max * 0.85)
    Threshold_max = VO2ToVel(vo2_max * 0.90)
    Gray_zone_3_min = VO2ToVel(vo2_max * 0.90)
    Gray_zone_3_max = VO2ToVel(vo2_max * 0.95)
    VO2_min = VO2ToVel(vo2_max * 0.95)
    VO2_max = VO2ToVel(vo2_max * 1)

    return {
        "gray_zone_1_pace": f"{timeConvert(Gray_zone_1, pace_type)} {pace_type}",
        "low_aerobic_run_pace": f"{timeConvert(Low_Aerobic_max, pace_type)} - {timeConvert(Low_Aerobic_min, pace_type)} {pace_type}",
        "moderate_aerobic_run_pace": f"{timeConvert(Moderate_Aerobic_max, pace_type)} - {timeConvert(Moderate_Aerobic_min, pace_type)} {pace_type}",
        "high_aerobic_run_pace": f"{timeConvert(High_Aerobic_max, pace_type)} - {timeConvert(High_Aerobic_min, pace_type)} {pace_type}",
        "threshold_pace": f"{timeConvert(Threshold_max, pace_type)} - {timeConvert(Threshold_min, pace_type)} {pace_type}",
        "gray_zone_3_pace": f"{timeConvert(Gray_zone_3_max, pace_type)} - {timeConvert(Gray_zone_3_min, pace_type)} {pace_type}",
        "vo2max_pace": f"{timeConvert(VO2_max, pace_type)} - {timeConvert(VO2_min, pace_type)} {pace_type}",
        "pace_prediction_id": id
    }


