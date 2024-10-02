import pandas as pd
from sqlalchemy import create_engine

# Load the Excel file
df = pd.read_excel("Tourism_Statistics_Poland.xlsx")

# Connect to MySQL
username = 'my_name'
password = 'my_password'
host = 'localhost'
database = 'tourism_db'

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")

# Write data to a table in MySQL
df.to_sql('tourism_stats', con=engine, if_exists='replace', index=False)

print("Data successfully loaded into MySQL!")
