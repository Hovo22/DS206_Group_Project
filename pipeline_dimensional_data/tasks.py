import sys
import os
import pyodbc
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
# from utils import generate_uuid
# from logging import setup_logger


# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import utils and logging

# Generate a unique execution ID for logging
# execution_id = generate_uuid()
# logger = setup_logger(execution_id)

def read_sql_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def get_engine(server, database):
    engine_str = f'mssql+pyodbc://{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
    return create_engine(engine_str)

def execute_sql_inserts(df, table_name, connection):
    sql = read_sql_file(f'pipeline_relational_data/queries/insert_into_{table_name}.sql')
    cursor = connection.cursor()
    for index, row in df.iterrows():
        cursor.execute(sql, tuple(row))
    connection.commit()
    cursor.close()
    # logger.info(f"Inserted data into {table_name} table.")

def execute_update_dim_script(table_name, connection):
    sql = read_sql_file(f'pipeline_dimensional_data/queries/update_dim_{table_name}.sql')
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    # logger.info(f"Updated dimension table {table_name}.")

def main():
    server = 'DESKTOP-NUBFUB9\\MSSQLSERVER01'
    relational_db = 'ORDERS_RELATIONAL_DB'
    dimensional_db = 'ORDERS_DIMENSIONAL_DB'

    # logger.info('Starting the data ingestion process.')

    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              f'Server={server};'
                              f'Database={relational_db};'
                              'Trusted_Connection=yes;')

        # logger.info('Connected to the relational database.')

        df_categories = pd.read_excel('raw_data_source.xlsx', sheet_name='Categories')
        df_customers = pd.read_excel('raw_data_source.xlsx', sheet_name='Customers')
        df_customers.sort_values(by='Phone', ascending=True, na_position='first', inplace=True)
        df_customers['Phone'] = df_customers['Phone'].astype(str)
        df_customers.replace({np.nan: None, np.inf: None, -np.inf: None}, inplace=True)

        df_employees = pd.read_excel('raw_data_source.xlsx', sheet_name='Employees')
        df_employees.sort_values(by='ReportsTo', ascending=True, na_position='first', inplace=True)
        df_employees['ReportsTo'] = df_employees['ReportsTo'].astype(str)
        df_employees.replace({np.nan: None, np.inf: None, -np.inf: None}, inplace=True)

        df_products = pd.read_excel('raw_data_source.xlsx', sheet_name='Products')
        df_region = pd.read_excel('raw_data_source.xlsx', sheet_name='Region')
        df_shippers = pd.read_excel('raw_data_source.xlsx', sheet_name='Shippers')
        df_suppliers = pd.read_excel('raw_data_source.xlsx', sheet_name='Suppliers')
        df_suppliers.sort_values(by='Phone', ascending=True, na_position='first', inplace=True)
        df_suppliers['Phone'] = df_suppliers['Phone'].astype(str)
        df_suppliers.replace({np.nan: None, np.inf: None, -np.inf: None}, inplace=True)
        df_territories = pd.read_excel('raw_data_source.xlsx', sheet_name='Territories')

        execute_sql_inserts(df_categories, 'Categories', conn)
        execute_sql_inserts(df_customers, 'Customers', conn)
        execute_sql_inserts(df_employees, 'Employees', conn)
        execute_sql_inserts(df_products, 'Products', conn)
        execute_sql_inserts(df_region, 'Region', conn)
        execute_sql_inserts(df_shippers, 'Shippers', conn)
        execute_sql_inserts(df_suppliers, 'Suppliers', conn)
        execute_sql_inserts(df_territories, 'Territories', conn)

        # logger.info('Data ingestion process completed successfully.')

        # Update dimension and fact tables
        conn = pyodbc.connect('Driver={SQL Server};'
                              f'Server={server};'
                              f'Database={dimensional_db};'
                              'Trusted_Connection=yes;')

        # logger.info('Connected to the dimensional database.')

        update_tables = ['Customers', 'Employees', 'Products', 'Region', 'Shippers', 'Suppliers', 'Territories', 'Categories']
        for table in update_tables:
            execute_update_dim_script(table, conn)
        
        # Update fact tables
        execute_update_dim_script('FactOrders', conn)

        # logger.info('Dimension and fact tables updated successfully.')

    except Exception as e:
        # logger.error(f"An error occurred: {e}")
    # finally:
        conn.close()
        # logger.info('Database connection closed.')

if __name__ == "__main__":
    main()
