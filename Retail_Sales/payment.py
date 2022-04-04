import pandas as pd
import pyodbc as po

#Import the CSV File into a DataFrame
data = pd.read_csv('/Users/lamquockhanh10/Downloads/datáet/olist_order_payments_dataset.csv')
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
		CREATE TABLE stg.PAYMENT (
			order_id NVARCHAR(40) ,
			payment_sequential int,
			type nvarchar(20) ,
			payment_installments int,
			value DECIMAL(18,4)
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO dw_retail_sales.stg.PAYMENT (order_id, payment_sequential, type,
       payment_installments, value)
                VALUES (?,?,?,?,?)
                ''',
                row.order_id,
                row.payment_sequential,
                row.payment_type,
                row.payment_installments,
                row.payment_value,
                )
conn.commit()
cursor.close()