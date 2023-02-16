import json
import requests as rqt
import pandas as pd
from upload import upload_file_to_server


def run_meteo_etl():
    # Set parameters
    parameters = {
        "latitude": 37.57,
        "longitude": 126.98,
        "daily": "temperature_2m_max",
        "timezone": "Asia/Seoul"
    }
    # Define the base URL
    base_url = "https://api.open-meteo.com/v1/forecast?"

    # Make the request
    response = rqt.get(base_url, params=parameters)
    print(json.dumps(response.json(), indent=1))

    daily_temps = response.json()["daily"]

    # Gather all the dates
    days_date = []
    for day in daily_temps["time"]:
        days_date.append(day)

    # Gather all the temps
    days_temp = []
    for temp in daily_temps["temperature_2m_max"]:
        days_temp.append(temp)

    # Combine the 2 lists
    days_and_tamps_list = list(zip(days_date, days_temp))

    print(days_and_tamps_list)
    # Create a Data frame and a CSV file
    days_temps_frame = pd.DataFrame(days_and_tamps_list)
    days_temps_frame.columns = ["Date", 'Temperature']
    days_temps_frame.to_csv("days_temp.csv")
    upload_file_to_server('days_temp.csv')


run_meteo_etl()
