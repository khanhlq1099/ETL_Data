import pandas as pd
import pyodbc as po

#Import the CSV File into a DataFrame
data = pd.read_csv('/Users/lamquockhanh10/Downloads/datáet/product_category_name_translation.csv')
df = pd.DataFrame(data)

#Connect Python to SQL Server
server = '10.10.10.20,1436'
database = 'dw_retail_sales'
username = 'de'
password = '8kP@6pyB6wV$'
driver= '{ODBC Driver 18 for SQL Server}'

conn = po.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1436;DATABASE='+database+';UID='+username+';PWD='+ password+';TrustServerCertificate=Yes;')

cursor = conn.cursor()

# Create Table
cursor.execute('''
		CREATE TABLE stg.CATEGORY (
			product_category_name NVARCHAR(50),
			product_category_name_english NVARCHAR(50)
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO dw_retail_sales.stg.CATEGORY (product_category_name, product_category_name_english)
                VALUES (?,?)
                ''',
                row.product_category_name,
                row.product_category_name_english
                )
conn.commit()
conn.close()