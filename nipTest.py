import json
import requests
from datetime import datetime
from random import randint
import time


if __name__ == "__main__":

    while True:

        rand_temp = randint(-83, -77)

        data_dict = {
            "nip_pk": "1",
            "data": {
                "temperature": rand_temp,
            },
            "time": str(datetime.now())
        }

        data_json = json.dumps(data_dict)

        payload = {'json_payload': data_json}

        r = requests.post('http://127.0.0.1:8000/receiver/receive/', data = payload)
        
        time.sleep(8)