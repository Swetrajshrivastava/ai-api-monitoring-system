def check_alert(result):

    status = result["status"]
    response_time = result["response_time"]
    api = result["api"]

    if status == "ERROR":
        print(f"ALERT: API ERROR → {api}")

    elif status >= 500:
        print(f"ALERT: SERVER FAILURE → {api}")

    elif status >= 400:
        print(f"WARNING: CLIENT ERROR → {api}")

    elif response_time is not None and response_time > 2:
        print(f"WARNING: SLOW API → {api} ({response_time}s)")