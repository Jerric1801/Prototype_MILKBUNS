import pandas as pd
import datetime
import random

def prediction(query):
    earliest = query["earliest"]
    latest = query["latest"]

    predictions = pd.read_csv("./app/static/predictions.csv")
        # Filter the predictions by date.
    filtered = predictions[predictions["arrival_date"] >= earliest]
    filtered = filtered[filtered["arrival_date"] <= latest]

    for index, row in filtered.iterrows():
        if row["expected_count"] > 48:
            filtered.drop(index, inplace=True)

    date_list = filtered["arrival_date"].tolist()

    count = 0
    result =[]

    TPDets = {
        "B1": [103.60596, 1.24136],
        "B2": [103.60659, 1.24383],
        "B3": [103.61217, 1.24387],
        "B4": [103.60834, 1.24596],
        "B5": [103.60922, 1.24080],
    }

    for dt in date_list:
        berth = list(TPDets.keys())[random.randint(0, 4)]
        temp = {}
        temp["num"] = count
        temp["cost"] = f"${random.randint(5000, 20000)}/day"
        temp["date"] = dt
        temp["country"] = "Singapore"
        temp["port"] = f"Tuas Port {berth}"
        temp["image"] = f"Tuas{berth}.jpeg"
        temp["coord"] = TPDets[berth]

        result.append(temp)

        count += 1

    return result
