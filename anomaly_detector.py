import json
import pandas as pd
from sklearn.ensemble import IsolationForest


LOG_FILE = "logs/api_logs.json"


def load_logs():

    with open(LOG_FILE) as f:
        data = json.load(f)

    return data


def detect_anomalies():

    data = load_logs()

    df = pd.DataFrame(data)

    # remove rows without response time
    df = df[df["response_time"].notnull()]

    model = IsolationForest(contamination=0.1)

    df["anomaly"] = model.fit_predict(df[["response_time"]])

    anomalies = df[df["anomaly"] == -1]

    return anomalies


if __name__ == "__main__":

    anomalies = detect_anomalies()

    print("\nDetected Anomalies:\n")

    print(anomalies)