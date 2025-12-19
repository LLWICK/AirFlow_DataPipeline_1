## Spotify ETL Pipeline with Apache Airflow
📌 Project Overview

This project implements an ETL (Extract, Transform, Load) data pipeline using Apache Airflow to collect music data from the Spotify Web API, process it using Python & Pandas, and store the results in Amazon S3.

The pipeline extracts albums and tracks for a given artist, computes popularity metrics, and uploads the Top 100 most popular tracks as a CSV file to an S3 bucket.

This project demonstrates real-world Data Engineering concepts such as orchestration, cloud storage integration, IAM-based security, and scheduled data workflows.

🏗️ Architecture
Spotify API
     |
     v
Apache Airflow (PythonOperator)
     |
     v
Pandas Data Processing
     |
     v
Amazon S3 (CSV Output)

🧰 Tech Stack

Apache Airflow – Workflow orchestration

Python 3.12

Pandas – Data transformation

Spotipy – Spotify Web API client

Amazon S3 – Data storage

IAM Role-based Authentication

EC2 (Linux) runtime environment

📂 Project Structure
spotify-airflow-etl/
│
├── spotify_dags.py        # Airflow DAG definition
├── spotify_etl.py         # ETL logic (Spotify API → Pandas → S3)
├── airflow.cfg            # Airflow configuration (local/EC2)
└── README.md

🔄 ETL Workflow
1️⃣ Extract

Connects to Spotify API using Client Credentials flow

Fetches all albums of a given artist

Extracts track metadata (name, popularity, album)

2️⃣ Transform

Removes duplicate tracks

Sorts tracks by popularity

Selects Top 100 most popular tracks

3️⃣ Load

Writes transformed data as CSV

Uploads to Amazon S3 using s3fs

s3://<your-bucket-name>/travis_scott_top_100.csv

🧪 Sample Output
track_name	popularity	album
SICKO MODE	92	ASTROWORLD
goosebumps	89	Birds in the Trap Sing McKnight
...	...	...
⚙️ Airflow DAG Details

DAG ID: spotify_dag

Operator: PythonOperator

Retries: 1

Retry Delay: 1 minute

Executor: SequentialExecutor (optimized for low-resource instances)

🔐 Security & Credentials
Spotify API

Credentials are not hardcoded and should be provided via environment variables:

export SPOTIFY_CLIENT_ID="your_client_id"
export SPOTIFY_CLIENT_SECRET="your_client_secret"

AWS S3 Access

Uses IAM Role attached to EC2

No AWS keys stored in code or config

Follows AWS security best practices

🚀 How to Run Locally / on EC2
1️⃣ Create virtual environment
python -m venv airflow_venv
source airflow_venv/bin/activate

2️⃣ Install dependencies
pip install apache-airflow pandas spotipy s3fs boto3

3️⃣ Start Airflow
airflow standalone


Access UI at:

http://localhost:8080


(or EC2 public IP)

📈 Learning Outcomes

Through this project, I learned:

How to build ETL pipelines using Apache Airflow

How DAG parsing and task execution work internally

Integrating third-party APIs into data workflows

Secure cloud storage access using IAM roles

Debugging Airflow DAG import and runtime errors

Running Airflow on low-resource cloud instances

🛣️ Future Improvements

Add scheduling (daily/hourly runs)

Store data in Amazon Redshift / Athena

Use Airflow S3Hook

Add data validation & logging

Dockerize the Airflow environment

Add unit tests for ETL logic

👤 Author

Linal Wickramaarachchi
Aspiring Data Engineer / Data Scientist
📍 Kandy, Sri Lanka
