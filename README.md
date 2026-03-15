# AI-Powered API Monitoring and Intelligent Log Analysis System

## Overview

The **AI-Powered API Monitoring and Intelligent Log Analysis System** is a Python-based observability platform designed to monitor API health, detect failures, analyze performance metrics, and visualize system behavior through an interactive dashboard.

This system continuously monitors multiple APIs, records response times and status codes, detects abnormal behavior using machine learning, and provides a real-time analytics dashboard for system reliability monitoring.

The project demonstrates key concepts used in modern observability platforms such as monitoring, logging, anomaly detection, and performance analytics.

---

## Key Features

### 1. API Monitoring Engine

The system periodically sends HTTP requests to configured API endpoints and records the following metrics:

* API endpoint
* HTTP response status
* Response time
* Timestamp

This allows continuous monitoring of API availability and performance.

---

### 2. Log Collection System

Monitoring results are stored as structured log records in a JSON file.

Each log entry contains:

* API endpoint
* response time
* HTTP status code
* monitoring timestamp

These logs serve as the data source for analytics and anomaly detection.

---

### 3. Real-Time Monitoring Dashboard

An interactive dashboard built using **Streamlit** visualizes the monitoring data.

Dashboard capabilities include:

* Response time visualization
* API status distribution
* monitoring statistics
* error tracking
* anomaly detection visualization
* performance analysis

The dashboard automatically refreshes to display the latest monitoring data.

---

### 4. AI-Based Anomaly Detection

The system applies **Isolation Forest (from scikit-learn)** to detect abnormal response time spikes.

This allows the monitoring platform to automatically identify performance anomalies that may indicate system failures or latency issues.

---

### 5. API Uptime Monitoring

The system calculates uptime metrics based on successful responses.

Uptime is calculated using the formula:

Uptime (%) = (Successful Requests / Total Requests) × 100

This helps evaluate API reliability and service availability.

---

### 6. Interactive API Filtering Dashboard

Users can select a specific API from the sidebar filter and analyze metrics individually.

This enables:

* per-API performance analysis
* targeted failure detection
* detailed monitoring insights

---

### 7. Performance Analytics

The dashboard includes multiple analytical views:

* response time trends
* slow API detection
* error monitoring
* API reliability metrics
* full monitoring logs

These analytics help identify performance bottlenecks and unstable endpoints.

---

## System Architecture

The monitoring platform follows this pipeline:

API Endpoints
↓
Monitoring Engine
↓
Log Storage
↓
AI Anomaly Detection
↓
Analytics Dashboard

This architecture resembles simplified observability pipelines used in production monitoring systems.

---

## Project Structure

AI-API-Monitoring-System
│
├── monitor
│   └── api_monitor.py
│
├── dashboard
│   └── dashboard.py
│
├── ai_engine
│   └── anomaly_detector.py
│
├── utils
│   └── alert_system.py
│
├── config
│   └── api_list.json
│
├── logs
│   └── api_logs.json
│
├── requirements.txt
└── README.md

---

## Technologies Used

* Python
* Streamlit
* Pandas
* Requests
* Scikit-learn
* NumPy
* Matplotlib

---

## Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/ai-api-monitoring-system.git

Navigate into the project directory:

cd ai-api-monitoring-system

Install dependencies:

pip install -r requirements.txt

---

## Running the System

Start the monitoring engine:

python monitor/api_monitor.py

Start the dashboard:

streamlit run dashboard/dashboard.py

Open the dashboard in your browser:

http://localhost:8501

---

## Example Dashboard Insights

The dashboard provides:

* monitoring statistics
* API uptime percentage
* response time analytics
* anomaly detection results
* slow API identification
* error monitoring
* full monitoring logs

These insights help analyze system performance and detect failures quickly.

---

## Future Improvements

Possible enhancements include:

* email or messaging alert integrations
* incident timeline visualization
* latency heatmap analytics
* machine learning based performance prediction
* containerized deployment using Docker
* cloud deployment for public monitoring access

---

## Learning Outcomes

This project demonstrates skills in:

* API monitoring
* logging systems
* anomaly detection using machine learning
* real-time data visualization
* system reliability analysis
* observability platform design

---

## License

This project is open source and available under the MIT License.
