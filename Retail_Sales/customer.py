import pandas as pd
import pyodbc as po

#Import the CSV File into a DataFrame
data = pd.read_csv('/Users/lamquockhanh10/Downloads/datáet/olist_customers_dataset.csv')
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
		CREATE TABLE stg.CUSTOMER (
			customer_id NVARCHAR(50) ,
			customer_unique_id NVARCHAR(50),
			customer_zip_code_prefix INT,
			customer_city NVARCHAR(50),
			customer_state NVARCHAR(10)
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO dw_retail_sales.stg.CUSTOMER (customer_id, customer_unique_id, customer_zip_code_prefix,customer_city,customer_state)
                VALUES (?,?,?,?,?)
                ''',
                row.customer_id,
                row.customer_unique_id,
                row.customer_zip_code_prefix,
                row.customer_city,
                row.customer_state
                )
conn.commit()
conn.close()