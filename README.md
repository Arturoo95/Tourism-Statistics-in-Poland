# Poland Tourism Statistics Analysis

## Project Overview

This project is a data analysis of tourism statistics in Poland from 2018 to 2023. The dataset contains information on tourist arrivals, average spend, nights spent, and the purpose of visits across multiple regions in Poland. The data is synthesized for the purpose of showcasing analytical skills using Python, MySQL, Tableau, and Excel. The objective is to visualize the patterns and trends in tourism over time, focusing on popular destinations, origins of tourists, and seasonal fluctuations.

## Key Features

- **Data Generation**: Synthetic dataset creation in Python using `pandas` to simulate tourism data.
- **Data Storage**: Importing the generated dataset into a MySQL database for analysis.
- **Visualization**: Analysis of tourism statistics using Tableau to create visualizations that highlight trends, popular regions, and seasonal fluctuations.

## Technologies Used

- **Python**: Used for data generation, processing, and loading the data into MySQL.
- **MySQL**: Used to store and query the tourism dataset.
- **Tableau**: Used for data visualization to showcase trends in tourism.
- **Excel**: Exported raw dataset for easy access and processing.

## Dataset

The dataset contains the following columns:
- **Year**: The year when the tourism data was recorded (2018 - 2023).
- **Month**: The month of the year (01 - 12).
- **Region**: The region in Poland where tourists visited (e.g., Warsaw, Kraków, Gdańsk).
- **Origin**: The country from where the tourists originated (e.g., Germany, France, USA).
- **Tourist_Arrivals**: The number of tourist arrivals per region.
- **Average_Spend**: The average amount spent by tourists in EUR.
- **Nights_Spent**: The number of nights spent by tourists in the region.
- **Purpose_of_Visit**: The purpose of the visit (e.g., Leisure, Business, Visiting Family, Education).

### Data Generation Script: `dataset_creation.py`
This Python script generates the synthetic tourism data using the `pandas` library. It creates random records for various regions, years, months, and origins, simulating real-world tourism data.

### Data Import to MySQL: `import_to_SQL.py`
This script imports the generated Excel data into a MySQL database. It uses `SQLAlchemy` and `pandas` to connect to MySQL and write the data into a table named `tourism_stats`.

## Visualizations

Here are the key visualizations generated in Tableau from the dataset:

1. **Line Chart**: Tourist Arrivals over time (Year vs Tourist Arrivals).
2. **Bar Chart**: Average Spend by Purpose of Visit.
3. **Pie Chart**: Distribution of Tourist Arrivals by Origin.
4. **Heat Map**: Seasonal Tourist Arrivals (Month vs Region).
5. **Scatter Plot**: Average Spend vs Nights Spent.

These charts help us understand the trends in tourist arrivals, the most popular tourist origins, and how spending and visit duration vary across regions.

## How to Run the Project

1. **Data Generation**:
   - Run the `dataset_creation.py` script in Python to generate the tourism dataset.
   - The data will be saved in an Excel file named `Tourism_Statistics_Poland.xlsx`.

2. **Import Data to MySQL**:
   - Ensure you have a MySQL database named `tourism_db` set up.
   - Run the `import_to_SQL.py` script to import the dataset into the `tourism_stats` table in MySQL.

3. **Analysis**:
   - Use MySQL to query the data or connect Tableau to the MySQL database for visualizations.
   - Alternatively, you can directly use Tableau to load the Excel file and generate visualizations.

## Conclusion

This project demonstrates how to work with tourism data in Poland by leveraging multiple technologies. From generating data using Python, importing it into MySQL, and creating insightful visualizations using Tableau.

## License

This project is for educational purposes and is open-source.
