import pandas as pd
import pyodbc as po

#Import the CSV File into a DataFrame
data = pd.read_csv('/Users/lamquockhanh10/Downloads/datáet/olist_orders_dataset.csv')
df = pd.DataFrame(data)
df = df.fillna(value=0)
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
		CREATE TABLE stg.[ORDER] (
			order_id NVARCHAR(40),
			customer_id NVARCHAR(40),
            order_status NVARCHAR(15),
            order_purchase_timestamp datetime,
            order_approved_at datetime,
            order_delivered_carrier_date datetime,
            order_delivered_customer_date datetime,
            order_estimated_delivery_date datetime
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO dw_retail_sales.stg.[ORDER] (order_id, customer_id, order_status, order_purchase_timestamp,
       order_approved_at, order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date)
                VALUES (?,?,?,?,?,?,?,?)
                ''',
                row.order_id,
                row.customer_id,
                row.order_status,
                row.order_purchase_timestamp,
                row.order_approved_at,
                row.order_delivered_carrier_date,
                row.order_delivered_customer_date,
                row.order_estimated_delivery_date
                )
conn.commit()
cursor.close()
