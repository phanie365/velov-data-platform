import json
from datetime import datetime
from pathlib import Path

import requests


STATION_INFORMATION_URL = (
    "https://api.cyclocity.fr/contracts/lyon/gbfs/v2/station_information.json"
)

STATION_STATUS_URL = (
    "https://api.cyclocity.fr/contracts/lyon/gbfs/v2/station_status.json"
)

OUTPUT_DIR = Path("data")
OUTPUT_DIR.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")


def fetch_data(url):
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()


station_information = fetch_data(STATION_INFORMATION_URL)
station_status = fetch_data(STATION_STATUS_URL)


information_file = OUTPUT_DIR / f"station_information_{timestamp}.json"
status_file = OUTPUT_DIR / f"station_status_{timestamp}.json"


with open(information_file, "w", encoding="utf-8") as file:
    json.dump(
        station_information,
        file,
        ensure_ascii=False,
        indent=2,
    )


with open(status_file, "w", encoding="utf-8") as file:
    json.dump(
        station_status,
        file,
        ensure_ascii=False,
        indent=2,
    )


print(f"Station information : {information_file}")
print(f"Station status      : {status_file}")