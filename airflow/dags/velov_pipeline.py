from datetime import datetime

import requests

from airflow.sdk import dag, task


STATION_STATUS_URL = (
    "https://api.cyclocity.fr/contracts/lyon/gbfs/v2/station_status.json"
)


@dag(
    dag_id="velov_pipeline",
    schedule=None,
    start_date=datetime(2026, 8, 15),
    catchup=False,
    tags=["velov"],
)
def velov_pipeline():

    @task
    def extract_station_status():
        response = requests.get(STATION_STATUS_URL, timeout=30)
        response.raise_for_status()

        data = response.json()

        stations = data["data"]["stations"]

        print(f"Nombre de stations récupérées : {len(stations)}")
        print(f"Exemple : {stations[0]}")

        return len(stations)

    extract_station_status()


velov_pipeline()