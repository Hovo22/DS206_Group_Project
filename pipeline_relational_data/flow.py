from utils import generate_uuid
from tasks import execute_sql_inserts
import pyodbc
import pandas as pd

class RelationalDataFlow:
    def __init__(self):
        self.execution_id = generate_uuid()

    def exec(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-NUBFUB9\\MSSQLSERVER01;'
                              'Database=ORDERS_RELATIONAL_DB;'
                              'Trusted_Connection=yes;')

        try:
            df_customers = pd.read_excel('raw_data_source.xlsx', sheet_name='Customers')
            execute_sql_inserts(df_customers, 'Customers', conn)

        finally:
            conn.close()

        print(f"Data flow execution completed with ID: {self.execution_id}")

