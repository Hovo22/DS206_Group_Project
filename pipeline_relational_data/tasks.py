import pyodbc
import pandas as pd
from sqlalchemy import create_engine
import numpy as np


def read_sql_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
server = 'DESKTOP-NUBFUB9\\MSSQLSERVER01'
database = 'ORDERS_RELATIONAL_DB'

engine_str = f'mssql+pyodbc://{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(engine_str)
    
def execute_sql_inserts(df, table_name, connection):
    sql = read_sql_file(f'pipeline_relational_data/queries/insert_into_{table_name}.sql')
    cursor = connection.cursor()
    for index, row in df.iterrows():
        cursor.execute(sql, tuple(row))
        cursor.commit()
    cursor.close()

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-NUBFUB9\MSSQLSERVER01;'
                      'Database=ORDERS_RELATIONAL_DB;'
                      'Trusted_Connection=yes;')

df_categories = pd.read_excel('raw_data_source.xlsx', sheet_name='Categories')

df_customers = pd.read_excel('raw_data_source.xlsx', sheet_name='Customers')
df_customers.sort_values(by='Phone', ascending=True, na_position='first', inplace=True)
df_customers['Phone'] = df_customers['Phone'].astype(str)
df_customers.replace({np.nan: None, np.inf: None, -np.inf: None}, inplace=True)

df_employees = pd.read_excel('raw_data_source.xlsx', sheet_name='Employees')

df_employees.sort_values(by='ReportsTo', ascending=True, na_position='first', inplace=True)
df_employees['ReportsTo'] = df_employees['ReportsTo'].astype(str)
df_employees.replace({np.nan: None, np.inf: None, -np.inf: None}, inplace=True)

df_orderdetails = pd.read_excel('raw_data_source.xlsx', sheet_name='OrderDetails')
df_orders = pd.read_excel('raw_data_source.xlsx', sheet_name='Orders')

df_orders.sort_values(by='TerritoryID', ascending=True, na_position='first', inplace=True)
df_orders['TerritoryID'] = df_orders['TerritoryID'].astype(str)
df_orders.replace({np.nan: None, np.inf: None, -np.inf: None}, inplace=True)

df_products = pd.read_excel('raw_data_source.xlsx', sheet_name='Products') 
df_region = pd.read_excel('raw_data_source.xlsx', sheet_name='Region')
df_shippers = pd.read_excel('raw_data_source.xlsx', sheet_name='Shippers')
df_suppliers= pd.read_excel('raw_data_source.xlsx', sheet_name='Suppliers')

df_suppliers.sort_values(by='Phone', ascending=True, na_position='first', inplace=True)
df_suppliers['Phone'] = df_suppliers['Phone'].astype(str)
df_suppliers.replace({np.nan: None, np.inf: None, -np.inf: None}, inplace=True)

df_territories = pd.read_excel('raw_data_source.xlsx', sheet_name='Territories')

execute_sql_inserts(df_categories, 'Categories', conn)
execute_sql_inserts(df_customers, 'Customers', conn)
execute_sql_inserts(df_employees, 'Employees', conn)
execute_sql_inserts(df_orderdetails, 'OrderDetails', conn)
execute_sql_inserts(df_orders, 'Orders', conn)
execute_sql_inserts(df_products, 'Products', conn)
execute_sql_inserts(df_region, 'Region', conn)
execute_sql_inserts(df_shippers, 'Shippers', conn)
execute_sql_inserts(df_suppliers, 'Suppliers', conn)
execute_sql_inserts(df_territories, 'Territories', conn)
conn.close()