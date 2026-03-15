import streamlit as st
import pandas as pd
import json
import os
from streamlit_autorefresh import st_autorefresh
from sklearn.ensemble import IsolationForest

LOG_FILE = "logs/api_logs.json"

# Auto refresh every 10 seconds
st_autorefresh(interval=10000, key="datarefresh")

st.set_page_config(page_title="API Monitoring Dashboard", layout="wide")

st.title("AI-Powered API Monitoring and Intelligent Log Analysis System")

# Check if log file exists
if not os.path.exists(LOG_FILE):

    st.error("Log file not found. Run the API monitor first.")

else:

    with open(LOG_FILE) as f:
        data = json.load(f)

    if len(data) == 0:

        st.warning("No monitoring data available.")

    else:

        df = pd.DataFrame(data)

        # ---------------------------
        # API FILTERING DASHBOARD
        # ---------------------------

        st.sidebar.header("API Filter")

        api_list = df["api"].unique()

        selected_api = st.sidebar.selectbox(
            "Select API",
            api_list
        )

        filtered_df = df[df["api"] == selected_api]

        st.subheader("Selected API")

        st.write(selected_api)

        # ---------------------------
        # MONITORING STATISTICS
        # ---------------------------

        st.subheader("Monitoring Statistics")

        col1, col2, col3 = st.columns(3)

        total_requests = len(filtered_df)
        errors = len(filtered_df[filtered_df["status"] != 200])
        slow_apis = len(filtered_df[filtered_df["response_time"] > 1])

        col1.metric("Total Requests", total_requests)
        col2.metric("Errors", errors)
        col3.metric("Slow APIs", slow_apis)

        st.divider()

        # ---------------------------
        # API UPTIME MONITORING
        # ---------------------------

        st.subheader("API Uptime Monitoring")

        successful_requests = len(filtered_df[filtered_df["status"] == 200])

        if total_requests > 0:
            uptime = (successful_requests / total_requests) * 100
        else:
            uptime = 0

        failure_rate = 100 - uptime

        col1, col2 = st.columns(2)

        col1.metric("API Uptime Percentage", f"{round(uptime,2)} %")
        col2.metric("Failure Rate", f"{round(failure_rate,2)} %")

        if uptime >= 99:

            st.success("System Reliability: Excellent")

        elif uptime >= 95:

            st.warning("System Reliability: Moderate")

        else:

            st.error("System Reliability: Poor")

        st.divider()

        # ---------------------------
        # RESPONSE TIME TREND
        # ---------------------------

        st.subheader("Response Time Trend")

        st.line_chart(filtered_df["response_time"])

        st.divider()

        # ---------------------------
        # API STATUS DISTRIBUTION
        # ---------------------------

        st.subheader("API Status Distribution")

        st.bar_chart(filtered_df["status"].value_counts())

        st.divider()

        # ---------------------------
        # AI ANOMALY DETECTION
        # ---------------------------

        st.subheader("AI Anomaly Detection")

        df_clean = filtered_df[filtered_df["response_time"].notnull()].copy()

        if len(df_clean) > 5:

            model = IsolationForest(contamination=0.1, random_state=42)

            df_clean["anomaly"] = model.fit_predict(df_clean[["response_time"]])

            anomalies = df_clean[df_clean["anomaly"] == -1]

            if len(anomalies) > 0:

                st.error(f"{len(anomalies)} anomaly events detected")

                st.dataframe(anomalies[["api", "response_time", "timestamp"]])

            else:

                st.success("No anomalies detected")

            st.line_chart(df_clean["response_time"])

        else:

            st.info("Not enough data for anomaly detection")

        st.divider()

        # ---------------------------
        # TOP SLOW APIS
        # ---------------------------

        st.subheader("Top Slow API Calls")

        slow = filtered_df.sort_values(by="response_time", ascending=False).head(5)

        st.dataframe(slow)

        st.divider()

        # ---------------------------
        # API ERRORS
        # ---------------------------

        st.subheader("API Errors")

        errors_table = filtered_df[filtered_df["status"] != 200]

        st.dataframe(errors_table)

        st.divider()

        # ---------------------------
        # FULL LOG DATA
        # ---------------------------

        st.subheader("Full Monitoring Logs")

        st.dataframe(df)