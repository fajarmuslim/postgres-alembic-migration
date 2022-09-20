# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine
import pandas as pd

# DEFINE THE DATABASE CREDENTIALS
user = 'postgres'
password = 'postgres'
host = '127.0.0.1'
port = 5432
database = 'iris'

# PYTHON FUNCTION TO CONNECT TO THE POSTGRESQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(url=f"postgresql://{user}:{password}@{host}:{port}/{database}")

if __name__ == '__main__':
    try: 
        engine = get_connection()
        print(f"Connection to the {host} for user {user} created successfully.")
        df = pd.read_sql_table('inputtables', engine.connect())
        print(df)
    except Exception as e:
        print(f'Connection could not be made due to the following error: \n, {e}')