import json
import requests
import datetime as dt
import os

today = dt.date.today()
bugun = today.strftime("%d/%m/%Y")

time = dt.datetime.now()
zaman = time.strftime("%H:%M:%S")
print(os.environ)
NUTRITION_ID = os.environ.get("NUTRITION_ID")
NUTRITITON_KEY = os.environ.get("NUTRITION_KEY")

url = "https://trackapi.nutritionix.com"
url_ext = "v2/natural/exercise"

header = {
    "Content-Type": "application/json",
    "x-app-id":NUTRITION_ID,
    "x-app-key":NUTRITITON_KEY
}

data = {
    "query":input("Tell me which exercises do you:")
}
body_data = json.dumps(data)
responce = requests.post(url=f"{url}/{url_ext}",data=body_data, headers=header)
duration = responce.json()["exercises"]
#nf_calories = responce.json()["exercises"]["nf_calories"]

last_body={}
i=0
for exercise in responce.json()["exercises"]:
    bodyy = {}
    bodyy["Exercise"]=exercise["name"]
    bodyy["Duration"]=exercise["duration_min"]
    bodyy["Calories"] =exercise["nf_calories"]
    last_body[i]=bodyy
    i+=1

url = 'https://api.sheety.co/c8fb731f96ce2fd4d8aeacf7d455606d/workoutTracking/workouts'

for key in range(len(last_body)):

    body = {
        "workout":
            {
                "date": bugun,
                "time": zaman,
                "exercise":last_body[key]["Exercise"].title(),
                "duration":last_body[key]["Duration"],
                "calories":last_body[key]["Calories"]
            }
            # Buraya workout verilerini ekleyin

    }

    # JSON formatındaki veriyi dönüştürme
    body_json = json.dumps(body)

    # POST isteği yapma
    response = requests.post(url, data=body_json, headers={"Content-Type": "application/json"})

    # Yanıtı JSON formatına çevirme ve işleme alma
    json_response = response.json()

    # Yanıtı kullanma
    if response.status_code == 200:
        print(json_response['workout'])
    else:
        print("Hata:", json_response)

    body.clear()