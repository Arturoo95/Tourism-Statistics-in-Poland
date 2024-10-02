import pandas as pd
import random
import datetime

# Define data for columns
years = list(range(2018, 2024))
months = [f'{month:02}' for month in range(1, 13)]
regions = ["Warsaw", "Kraków", "Gdańsk", "Zakopane", "Wrocław", "Poznań", "Łódź", "Szczecin"]
tourist_origins = ["Germany", "France", "Italy", "UK", "USA", "China", "Russia", "Ukraine", "Spain"]
purposes = ["Leisure", "Business", "Visiting Family", "Education"]

# Create an empty list to store records
data = []

# Generate random tourism statistics
for year in years:
    for month in months:
        for region in regions:
            for origin in tourist_origins:
                entry = {
                    "Year": year,
                    "Month": month,
                    "Region": region,
                    "Origin": origin,
                    "Tourist_Arrivals": random.randint(1000, 50000),  # Random tourist arrivals
                    "Average_Spend": round(random.uniform(50, 300), 2),  # Average spend in EUR
                    "Nights_Spent": random.randint(1, 14),  # Random number of nights
                    "Purpose_of_Visit": random.choice(purposes)  # Random purpose of visit
                }
                data.append(entry)

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
file_name = "Tourism_Statistics_Poland.xlsx"
df.to_excel(file_name, index=False)

print(f"Dataset saved to {file_name}")
