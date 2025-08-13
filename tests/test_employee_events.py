import pytest
from pathlib import Path

# Using pathlib create a project_root
# variable set to the absolute path
# for the root of this project
#### YOUR CODE HERE

# apply the pytest fixture decorator
# to a `db_path` function
#### YOUR CODE HERE
    
    # Using the `project_root` variable
    # return a pathlib object for the `employee_events.db` file
    #### YOUR CODE HERE

# Define a function called
# `test_db_exists`
# This function should receive an argument
# with the same name as the function
# the creates the "fixture" for
# the database's filepath
#### YOUR CODE HERE
    
    # using the pathlib `.is_file` method
    # assert that the sqlite database file exists
    # at the location passed to the test_db_exists function
    #### YOUR CODE HERE

@pytest.fixture
def db_conn(db_path):
    from sqlite3 import connect
    return connect(db_path)

@pytest.fixture
def table_names(db_conn):
    name_tuples = db_conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    return [x[0] for x in name_tuples]

# Define a test function called
# `test_employee_table_exists`
# This function should receive the `table_names`
# fixture as an argument
#### YOUR CODE HERE

    # Assert that the string 'employee'
    # is in the table_names list
    #### YOUR CODE HERE

# Define a test function called
# `test_team_table_exists`
# This function should receive the `table_names`
# fixture as an argument
#### YOUR CODE HERE

    # Assert that the string 'team'
    # is in the table_names list
    #### YOUR CODE HERE

# Define a test function called
# `test_employee_events_table_exists`
# This function should receive the `table_names`
# fixture as an argument
#### YOUR CODE HERE

    # Assert that the string 'employee_events'
    # is in the table_names list
    #### YOUR CODE HERE

import pytest
import sqlite3
from pathlib import Path

# Set up database path (like setting the address to the database!)
DB_PATH = Path(__file__).parent.parent / "python-package" / "employee_events" / "employee_events.db"

@pytest.fixture
def db_path():
    """
    This function gives us the path to the database.
    Think of it like giving directions to the treasure chest!
    """
    return DB_PATH

def test_db_exists(db_path):
    """
    Test that the database file exists.
    Like checking if the treasure chest is really there!
    """
    assert db_path.exists(), f"Database file not found at {db_path}"

def test_employee_table_exists(db_path):
    """
    Test that the employee table exists in the database.
    Like checking if there's a page about students in the school directory!
    """
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Check if the table exists
    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name='employee'
    """)
    
    result = cursor.fetchone()
    connection.close()
    
    assert result is not None, "Employee table does not exist"

def test_team_table_exists(db_path):
    """
    Test that the team table exists in the database.
    Like checking if there's a page about classes in the school directory!
    """
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Check if the table exists
    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name='team'
    """)
    
    result = cursor.fetchone()
    connection.close()
    
    assert result is not None, "Team table does not exist"

def test_employee_events_table_exists(db_path):
    """
    Test that the employee_events table exists in the database.
    Like checking if there's a page about behavior records in the school directory!
    """
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Check if the table exists
    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name='employee_events'
    """)
    
    result = cursor.fetchone()
    connection.close()
    
    assert result is not None, "Employee_events table does not exist"
