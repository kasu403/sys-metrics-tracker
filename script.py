import psutil
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()
url = os.getenv("URLBANCO")

connection = None
cursor = None

cpu = psutil.cpu_percent(interval=1)
memoria= psutil.virtual_memory().percent
disco = psutil.disk_usage('/').percent

try:

    connection = psycopg2.connect(url)
    cursor = connection.cursor()

    insertquery = "INSERT INTO monitoramento_hardware (cpu, memoria, disco)  VALUES (%s, %s, %s)"

    cursor.execute(insertquery, (cpu, memoria, disco))

    connection.commit()

    print("Dados enviados com sucesso!")
    print(f"CPU: {cpu}% | Memória: {memoria}% | Disco: {disco}%")

except Exception as erro:
    print("Conexão mal sucedida, erro: ", erro)

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("Conexão finalizada com sucesso")