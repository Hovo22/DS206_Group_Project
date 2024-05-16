import uuid
import pyodbc
from sqlalchemy import create_engine

def generate_uuid():
    """
    Generates a unique UUID.
    
    Returns:
    str: A string representation of a UUID.
    """
    return str(uuid.uuid4())

def read_sql_file(file_path):
    """
    Reads the content of a SQL file and returns it as a string.
    """
    with open(file_path, 'r') as file:
        return file.read()

def get_engine(server, database):
    """
    Creates and returns a SQLAlchemy engine.
    
    Parameters:
    server (str): The SQL Server name.
    database (str): The database name.
    
    Returns:
    Engine: SQLAlchemy engine object.
    """
    engine_str = f'mssql+pyodbc://{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
    return create_engine(engine_str)

def get_connection(server, database):
    """
    Creates and returns a pyodbc connection.
    
    Parameters:
    server (str): The SQL Server name.
    database (str): The database name.
    
    Returns:
    Connection: pyodbc connection object.
    """
    conn_str = f'Driver={{SQL Server}};Server={server};Database={database};Trusted_Connection=yes;'
    return pyodbc.connect(conn_str)

def execute_sql_script(file_path, connection):
    """
    Executes a SQL script from a file.
    
    Parameters:
    file_path (str): The path to the SQL file.
    connection (pyodbc.Connection): The connection object to the database.
    """
    sql = read_sql_file(file_path)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    cursor.close()

def execute_sql_inserts(df, table_name, connection):
    """
    Executes SQL insert statements for a given DataFrame and table name.
    
    Parameters:
    df (DataFrame): The DataFrame containing the data to be inserted.
    table_name (str): The name of the table into which data is to be inserted.
    connection (pyodbc.Connection): The connection object to the database.
    """

    sql = read_sql_file(f'pipeline_relational_data/queries/insert_into_{table_name}.sql')
    cursor = connection.cursor()
    for index, row in df.iterrows():
        cursor.execute(sql, tuple(row))
    connection.commit()
    cursor.close()