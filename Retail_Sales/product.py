import pandas as pd
import pyodbc as po

#Import the CSV File into a DataFrame
data = pd.read_csv('/Users/lamquockhanh10/Downloads/datáet/olist_products_dataset.csv')
df = pd.DataFrame(data)
#function
# df1= df.function()
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
		CREATE TABLE stg.PRODUCT (
			product_id NVARCHAR(40) ,
			product_category_name NVARCHAR(50),
			product_name_lenght int,
			product_description_lenght int,
			product_photos_qty int,
			product_weight_g int,
			product_length_cm int,
            product_height_cm int,
            product_width_cm int
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO dw_retail_sales.stg.PRODUCT (product_id, product_category_name, product_name_lenght,
       product_description_lenght, product_photos_qty, product_weight_g,
       product_length_cm, product_height_cm, product_width_cm)
                VALUES (?,?,?,?,?,?,?,?,?)
                ''',
                row.product_id,
                row.product_category_name,
                row.product_name_lenght,
                row.product_description_lenght,
                row.product_photos_qty,
                row.product_weight_g,
                row.product_length_cm,
                row.product_height_cm,
                row.product_width_cm
                )
conn.commit()
cursor.close()