import utils
import numpy as np
import pandas as pd

# import logger
# from logger import setup_logger
# from utils import generate_uuid

# Generate a unique execution ID for logging
# execution_id = generate_uuid()
# logger = setup_logger(execution_id)

def create_rel_db(connection):
    rel_db = utils.read_sql_file('infrastructure_initiation/relational_db_creation.sql')

    cursor = connection.cursor()
    cursor.execute(rel_db)
    connection.commit()

def create_rel_tables(connection):
    rel_tables = utils.read_sql_file('infrastructure_initiation/relational_db_table_creation.sql')

    cursor = connection.cursor()
    cursor.execute(rel_tables)
    connection.commit()

def create_rel_dependencies(connection):
    rel_deps = utils.read_sql_file('infrastructure_initiation/relational_db_add_PK_FK_constraints.sql')

    cursor = connection.cursor()
    cursor.execute(rel_deps)
    connection.commit()

def populate_rel_tables(connection):
    df_categories = pd.read_excel('raw_data_source.xlsx', sheet_name='Categories')
    df_customers = pd.read_excel('raw_data_source.xlsx', sheet_name='Customers')
    df_employees = pd.read_excel('raw_data_source.xlsx', sheet_name='Employees')
    df_orderdetails = pd.read_excel('raw_data_source.xlsx', sheet_name='OrderDetails')
    df_orders = pd.read_excel('raw_data_source.xlsx', sheet_name='Orders')
    df_products = pd.read_excel('raw_data_source.xlsx', sheet_name='Products')
    df_region = pd.read_excel('raw_data_source.xlsx', sheet_name='Region')
    df_shippers = pd.read_excel('raw_data_source.xlsx', sheet_name='Shippers')
    df_suppliers = pd.read_excel('raw_data_source.xlsx', sheet_name='Suppliers')
    
    df_customers.sort_values(by='Phone', ascending=True, na_position='first', inplace=True)
    df_customers['Phone'] = df_customers['Phone'].astype(str)
    df_customers.replace({np.nan: None, np.inf: None, -np.inf: None}, inplace=True)

    df_employees.sort_values(by='ReportsTo', ascending=True, na_position='first', inplace=True)
    df_employees['ReportsTo'] = df_employees['ReportsTo'].astype(str)
    df_employees.replace({np.nan: None, np.inf: None, -np.inf: None}, inplace=True)

    df_orders.sort_values(by='TerritoryID', ascending=True, na_position='first', inplace=True)
    df_orders['TerritoryID'] = df_orders['TerritoryID'].astype(str)
    df_orders.replace({np.nan: None, np.inf: None, -np.inf: None}, inplace=True)

    df_suppliers.sort_values(by='Phone', ascending=True, na_position='first', inplace=True)
    df_suppliers['Phone'] = df_suppliers['Phone'].astype(str)
    df_suppliers.replace({np.nan: None, np.inf: None, -np.inf: None}, inplace=True)
    df_territories = pd.read_excel('raw_data_source.xlsx', sheet_name='Territories')

    utils.execute_sql_inserts(df_categories, 'Categories', connection)
    utils.execute_sql_inserts(df_customers, 'Customers', connection)
    utils.execute_sql_inserts(df_employees, 'Employees', connection)
    utils.execute_sql_inserts(df_orderdetails, 'OrderDetails', connection)
    utils.execute_sql_inserts(df_orders, 'Orders', connection)
    utils.execute_sql_inserts(df_products, 'Products', connection)
    utils.execute_sql_inserts(df_region, 'Region', connection)
    utils.execute_sql_inserts(df_shippers, 'Shippers', connection)
    utils.execute_sql_inserts(df_suppliers, 'Suppliers', connection)
    utils.execute_sql_inserts(df_territories, 'Territories', connection)
