# Hardware Monitor Python

A lightweight Python script that monitors system hardware metrics (CPU, RAM, and Disk) and logs them in real-time to a Supabase PostgreSQL database.

##  Features

- **CPU Tracking**: Captures real-time CPU usage percentage.
- **Memory Monitoring**: Tracks virtual memory utilization.
- **Disk Space Insights**: Logs main disk usage metrics.
- **Cloud Logging**: Securely stores data remotely via Supabase.

##  Tech Stack

- **Python 3**
- **psutil**: For retrieving information on running processes and system utilization.
- **psycopg2**: PostgreSQL database adapter for Python.
- **Supabase**: Open-source Firebase alternative (PostgreSQL database).

##  Prerequisites

Before running the script, make sure you have a table named `monitoramento_hardware` in your Supabase database with the following structure:

- `cpu` (numeric / float)
- `memoria` (numeric / float)
- `disco` (numeric / float)

## 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone
   cd sys-metrics-tracker
   ```

2. **Install dependencies:**
   ```bash
   pip install psutil psycopg2-binary python-dotenv
   ```

3. **Configure environment variables:**
   Create a `.env` file in the root directory and add your Supabase connection string:
   ```env
   URLBANCO=postgresql://postgres:[YOUR-PROJECT-ID]:[YOUR-PASSWORD]@://supabase.com
   ```

## 💻 Usage

Run the script using Python:
```bash
python main.py
```