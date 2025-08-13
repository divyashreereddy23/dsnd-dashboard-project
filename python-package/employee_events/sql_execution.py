from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

# Using pathlib, create a `db_path` variable
# that points to the absolute path for the `employee_events.db` file
#### YOUR CODE HERE


# OPTION 1: MIXIN
# Define a class called `QueryMixin`
class QueryMixin:
    """
    Mixin class to handle database connections and SQL execution.
    Think of this like a helper that knows how to talk to the database!
    """

    def __init__(self):
        # Find the database file (it's like finding the treasure chest!)
        self.db_path = Path(__file__).parent / "employee_events.db"

    def execute_query(self, query, params=None):
        """
        This method opens the database, runs your question (query), 
        and gives you back the answer - just like asking a librarian!
        """
        connection = None
        try:
            # Open connection to database (like opening a door)
            connection = sqlite3.connect(self.db_path)
            connection.row_factory = sqlite3.Row  # Makes results easier to work with
            cursor = connection.cursor()
            
            # Execute the query (ask the question)
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            # Get all results (collect all the answers)
            results = cursor.fetchall()
            
            # Convert to list of dictionaries (make it easy to read)
            return [dict(row) for row in results]
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
        finally:
            # Always close the connection (like closing the door when you leave)
            if connection:
                connection.close()

    # Define a method named `pandas_query`
    # that receives an sql query as a string
    # and returns the query's result
    # as a pandas dataframe
    #### YOUR CODE HERE

    # Define a method named `query`
    # that receives an sql_query as a string
    # and returns the query's result as
    # a list of tuples. (You will need
    # to use an sqlite3 cursor)
    #### YOUR CODE HERE
    

 
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
