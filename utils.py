import configparser

def get_sql_config(filename, database):
     cf = configparser.ConfigParser ()
     cf.read (filename) 
     _server = cf.get(database,"Server")
     _database = cf.get(database,"Database")
     _trusted_connection = cf.get(database,"Trusted_Connection")
     return _server,_database,_trusted_connection

def extract_tables_db(cursor, *args):
    results = []
    for x in cursor.execute('exec sp_tables'):
        if x[1] not in args:
            results.append(x[2])
    return results

def extract_table_cols(cursor, table_name):
    result = []
    for row in cursor.columns(table=table_name):
        result.append(row.column_name)
    return result


def find_primary_key(cursor, table_name, schema):
    table_primary_key = cursor.primaryKeys(table_name, schema=schema)

    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    try:
        return results[0]
    except:
        pass
    return results

def unpacker(row, collist):
    result = []
    for i in collist:
        result.append(row[i])

    return tuple(result)

import uuid

def generate_uuid():
    """Generate a unique UUID string."""
    return str(uuid.uuid4())