# Import the QueryBase class
from .query_base import QueryBase

# Import dependencies needed for sql execution
# from the `sql_execution` module
from .sql_execution import query, QueryMixin

# Define a subclass of QueryBase
# called Employee
class Employee(QueryBase):

    # Set the class attribute `name`
    # to the string "employee"
    name = "employee"


    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution
    def names(self):
        
        # Query 3
        # Write an SQL query
        # that selects two columns 
        # 1. The employee's full name
        # 2. The employee's id
        # This query should return the data
        # for all employees in the database
        query_string = """
        SELECT 
            first_name || ' ' || last_name as full_name,
            employee_id
        FROM employee
        ORDER BY last_name, first_name
        """
        
        return self.query(query_string)
    

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    def username(self, id):
        
        # Query 4
        # Write an SQL query
        # that selects an employees full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
        query_string = f"""
        SELECT first_name || ' ' || last_name as full_name
        FROM employee
        WHERE employee_id = {id}
        """
        
        return self.query(query_string)


    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    def ml_data(self):
        query_string = """
        SELECT 
            e.employee_id,
            e.first_name,
            e.last_name,
            t.team_name,
            t.shift,
            COUNT(ee.event_date) as total_days_recorded,
            SUM(ee.positive_events) as total_positive_events,
            SUM(ee.negative_events) as total_negative_events,
            AVG(ee.positive_events) as avg_positive_per_day,
            AVG(ee.negative_events) as avg_negative_per_day,
            (SUM(ee.positive_events) - SUM(ee.negative_events)) as net_performance
        FROM employee e
        LEFT JOIN team t ON e.team_id = t.team_id
        LEFT JOIN employee_events ee ON e.employee_id = ee.employee_id
        GROUP BY e.employee_id, e.first_name, e.last_name, t.team_name, t.shift
        ORDER BY net_performance DESC
        """
        
        return self.pandas_query(query_string)
