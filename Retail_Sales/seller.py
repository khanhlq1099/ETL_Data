import pandas as pd
import pyodbc as po

#Import the CSV File into a DataFrame
data = pd.read_csv('/Users/lamquockhanh10/Downloads/datáet/olist_sellers_dataset.csv')
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
		CREATE TABLE stg.SELLER (
			seller_id NVARCHAR(40) ,
            seller_zip_code_prefix INT,    
			seller_city NVARCHAR(40),
            seller_state NVARCHAR(5)
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO dw_retail_sales.stg.SELLER (seller_id, seller_zip_code_prefix, seller_city,seller_state)
                VALUES (?,?,?,?)
                ''',
                row.seller_id,
                row.seller_zip_code_prefix,
                row.seller_city,
                row.seller_state
                )
conn.commit()
conn.close()