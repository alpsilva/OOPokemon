from firebase_admin import credentials
import os

from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DB_URL")

certificate_file_path = "./serviceAccountKey.json"
database_credentials = credentials.Certificate(certificate_file_path)
database_config = {
    'databaseURL': db_url
}
