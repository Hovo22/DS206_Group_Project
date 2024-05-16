from ..utils import generate_uuid, get_connection
from .tasks import create_rel_db, create_rel_tables, create_rel_dependencies, populate_rel_tables

class RelationalDataFlow:
    def __init__(self):
        self.execution_id = generate_uuid()
    
    def exec(self):
        """
        Execute tasks in the right order.
        """
        server = 'DESKTOP-NUBFUB9\\MSSQLSERVER01'
        database = 'ORDERS_RELATIONAL_DB'
        connection = get_connection(server, database)

        try:
            create_rel_db(connection)
            create_rel_tables(connection)
            create_rel_dependencies(connection)
            populate_rel_tables(connection)
        except Exception as e:
            print(f"Execution {self.execution_id} failed: {e}")
        finally:
            connection.close()

        print(f"Data flow execution completed with ID: {self.execution_id}")

if __name__ == "__main__":
    data_flow = RelationalDataFlow()
    print(f"Execution ID: {data_flow.execution_id}")
    data_flow.exec()