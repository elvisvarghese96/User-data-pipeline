**Users Data pipeline using airflow**

This Airflow DAG extracts, processes, and stores random user data from a public API  called randomuser.me into a PostgreSQL database.

**🔧 Features**
Checks API availability before extraction

Fetches user data from https://randomuser.me/api/

Processes data using Pandas

Stores user info into a PostgreSQL table

**🔁 DAG Workflow**
Create Table – Creates a users table in Postgres if it doesn't exist

Check API – Verifies the API is live or not

Extract Data – Calls the API to retrieve random user data

Process Data – Transforms data using Pandas and saves to CSV

Store Data – Loads data from CSV into the database

**⚙️ Requirements**
Python 3.8+

Apache Airflow

Postgres

Pandas

**📦 Installation (for a virtual environment)**
bash
Copy
Edit
python -m venv venv
source venv/bin/activate

pip install "apache-airflow[postgres,http]" pandas
🗃️ Connections Setup in Airflow UI
HTTP Connection: user_api

Host: https://randomuser.me/

Postgres Connection: postgres

Set to your Postgres DB credentials

**📄 Output**
Processed user data is saved to /tmp/processed_user.csv before being inserted into the users table.
