import psycopg2
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

def get_password_from_db():
    try:
        connection = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME
        )
        cursor = connection.cursor()
        cursor.execute("SELECT senha FROM login LIMIT 1;")
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            return result[0]  # Retorna a senha como string
        else:
            return None
    except Exception as e:
        print("Erro ao acessar o banco de dados:", e)
        return None
