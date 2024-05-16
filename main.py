# main.py
import utils
from pipeline_dimensional_data.flow import DimensionalDataFlow

if __name__ == "__main__":
    connection = utils.get_sql_connection()

    flow = DimensionalDataFlow()
    flow.exec(connection)
    connection.close()
