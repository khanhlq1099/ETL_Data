import pandas as pd
import pyodbc as po

#Import the CSV File into a DataFrame
data = pd.read_csv('/Users/lamquockhanh10/Downloads/datáet/olist_geolocation_dataset.csv')
df = pd.DataFrame(data)

#Connect Python to SQL Server
server = '10.10.10.20,1436'
database = 'dw_retail_sales'
username = 'de'
password = '8kP@6pyB6wV$'
driver= '{ODBC Driver 18 for SQL Server}'

conn = po.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1436;DATABASE='+database+';UID='+username+';PWD='+ password+';TrustServerCertificate=Yes;')

cursor = conn.cursor()

#Create Table
cursor.execute('''
		CREATE TABLE stg.LOCATION (
			geolocation_zip_code_prefix INT ,
			geolocation_lat DECIMAL(20,17),
			geolocation_long DECIMAL(20,17) ,
			geolocation_city NVARCHAR(50),
			geolocation_state NVARCHAR(5)
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO dw_retail_sales.stg.LOCATION (geolocation_zip_code_prefix,geolocation_lat,geolocation_long,
       geolocation_city,geolocation_state)
                VALUES (?,?,?,?,?)
                ''',
                row.geolocation_zip_code_prefix,
                row.geolocation_lat,
                row.geolocation_lng,
                row.geolocation_city,
                row.geolocation_state
                )
conn.commit()
conn.close()