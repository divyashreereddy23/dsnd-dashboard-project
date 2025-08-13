from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

# Using pathlib, create a `db_path` variable
# that points to the absolute path for the `employee_events.db` file
db_path = Path(__file__).parent / "employee_events.db"


# OPTION 1: MIXIN
# Define a class called `QueryMixin`
class QueryMixin:
    """
    Mixin class to handle database connections and SQL execution.
    Think of this like a helper that knows how to talk to the database!
    """

    # Define a method named `pandas_query`
    # that receives an sql query as a string
    # and returns the query's result
    # as a pandas dataframe
    def pandas_query(self, sql_query):
        """
        Execute an SQL query and return results as a pandas DataFrame.
        
        Args:
            sql_query (str): SQL query string to execute
            
        Returns:
            pandas.DataFrame: Query results as a DataFrame
        """
        connection = connect(db_path)
        try:
            df = pd.read_sql_query(sql_query, connection)
            return df
        finally:
            connection.close()

    # Define a method named `query`
    # that receives an sql_query as a string
    # and returns the query's result as
    # a list of tuples. (You will need
    # to use an sqlite3 cursor)
    def query(self, sql_query):
        """
        Execute an SQL query and return results as a list of tuples.
        
        Args:
            sql_query (str): SQL query string to execute
            
        Returns:
            list: Query results as a list of tuples
        """
        connection = connect(db_path)
        cursor = connection.cursor()
        try:
            result = cursor.execute(sql_query).fetchall()
            return result
        finally:
            connection.close()
    

 
 # Leave this code unchanged
def query(func):
    """
    Decorator that runs a standard sql execution
    and returns a list of tuples
    """

    @wraps(func)
    def run_query(*args, **kwargs):
        query_string = func(*args, **kwargs)
        connection = connect(db_path)
        cursor = connection.cursor()
        result = cursor.execute(query_string).fetchall()
        connection.close()
        return result
    
    return run_query
