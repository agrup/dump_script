# create a function t conecte to a postgrs database
# create a function tu backup the database
from datetime import datetime
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()
def get_database_url() -> str:
    """
    Gets the database URL from the environment variables.
    """
    url = os.getenv('DATABASE_URL')
    database = os.getenv('DATABASE_NAME')
    user = os.getenv('DATABASE_USER')
    password = os.getenv('DATABASE_PASSWORD')
    host = os.getenv('DATABASE_HOST')
    port = os.getenv('DATABASE_PORT')
    return f"postgresql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"

def get_backup_file_path() -> str:
    """
    return a path with the current date and time
    """
    directory = os.getenv("OUTPUT_FOLDER").replace("/","")
    return f"{directory}/backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"

def backup_database() -> bool:
    """
    Creates a backup (dump) of the PostgreSQL database.

    Returns:
        bool: True if backup was successful, False otherwise.
    """ 
    # connection_string = get_database_url()
    backup_file_path = get_backup_file_path()

    try:
        database_url = get_database_url()
        cmd = [
            "pg_dump",
            "-d", database_url,
            "-f", backup_file_path
        ]

        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Database backup failed: {e}")
        return False
    except Exception as e:
        print(f"Error during backup: {e}")
        return False
