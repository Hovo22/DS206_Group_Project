import pyodbc
import pandas as pd

def read_sql_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def execute_sql_inserts(df, table_name, connection):
    sql = read_sql_file(f'pipeline_relational_data/queries/insert_into_{table_name}.sql')
    cursor = connection.cursor()
    try:
        for index, row in df.iterrows():
            cursor.execute(sql, tuple(row))
        connection.commit() 
    except Exception as e:
        print(f"Failed to execute for {table_name}: {e}")
        connection.rollback()
    finally:
        cursor.close()


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-NUBFUB9\MSSQLSERVER01;'
                      'Database=ORDERS_RELATIONAL_DB;'
                      'Trusted_Connection=yes;')

df_categories = pd.read_excel('raw_data_source.xlsx', sheet_name='Categories')

def map_dtype_to_sql(dtype):
    if dtype == 'int64':
        return 'INTEGER'
    elif dtype == 'float64':
        return 'FLOAT'
    elif dtype == 'object':
        return 'NVARCHAR(255)'
    elif dtype == 'datetime64':
        return 'DATETIME'
    else:
        return 'NVARCHAR(255)'

df_customers = pd.read_excel('raw_data_source.xlsx', sheet_name='Customers')

sql_data_types = {col: map_dtype_to_sql(df_customers[col].dtype.name) for col in df_customers.columns}

df_employees = pd.read_excel('raw_data_source.xlsx', sheet_name='Employees')
df_orderdetails = pd.read_excel('raw_data_source.xlsx', sheet_name='OrderDetails')
def map_dtype_to_sql(dtype):
    if dtype == 'int64':
        return 'INTEGER'
    elif dtype == 'float64':
        return 'FLOAT'
    elif dtype == 'object':
        return 'NVARCHAR(255)'
    elif dtype == 'datetime64':
        return 'DATETIME'
    else:
        return 'NVARCHAR(255)'
df_orders = pd.read_excel('raw_data_source.xlsx', sheet_name='Orders')
sql_data_types = {col: map_dtype_to_sql(df_orders[col].dtype.name) for col in df_orders.columns}
df_products = pd.read_excel('raw_data_source.xlsx', sheet_name='Products')
df_region = pd.read_excel('raw_data_source.xlsx', sheet_name='Region')
df_shippers = pd.read_excel('raw_data_source.xlsx', sheet_name='Shippers')
df_suppliers= pd.read_excel('raw_data_source.xlsx', sheet_name='Suppliers')
df_territories = pd.read_excel('raw_data_source.xlsx', sheet_name='Territories')


def create_table_sql(df, table_name):
    sql_types = {col: map_dtype_to_sql(df[col].dtype.name) for col in df.columns}
    columns_with_types = ", ".join([f"{col} {sql_types[col]}" for col in df.columns])
    sql_create = f"CREATE TABLE {table_name} ({columns_with_types});"
    return sql_create

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


