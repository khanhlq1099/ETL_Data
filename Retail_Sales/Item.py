import pandas as pd
import pyodbc as po

#Import the CSV File into a DataFrame
data = pd.read_csv('/Users/lamquockhanh10/Downloads/datáet/olist_order_items_dataset.csv')
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
		CREATE TABLE stg.ITEM (
			order_id NVARCHAR(40) ,
			item_id int,
			product_id nvarchar(40) ,
			seller_id nvarchar(40),
			shipping_limit_date datetime,
			price float,
			freight_value float
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO dw_retail_sales.stg.ITEM (order_id, item_id, product_id,
       seller_id, shipping_limit_date, price, freight_value)
                VALUES (?,?,?,?,?,?,?)
                ''',
                row.order_id,
                row.order_item_id,
                row.product_id,
                row.seller_id,
                row.shipping_limit_date,
                row.price,
                row.freight_value
                )
conn.commit()
cursor.close()