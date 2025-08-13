# Import the QueryBase class
#### YOUR CODE HERE

# Import dependencies needed for sql execution
# from the `sql_execution` module
#### YOUR CODE HERE

# Define a subclass of QueryBase
# called Employee
#### YOUR CODE HERE

    # Set the class attribute `name`
    # to the string "employee"
    #### YOUR CODE HERE


    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution
    #### YOUR CODE HERE
        
        # Query 3
        # Write an SQL query
        # that selects two columns 
        # 1. The employee's full name
        # 2. The employee's id
        # This query should return the data
        # for all employees in the database
        #### YOUR CODE HERE
    

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    #### YOUR CODE HERE
        
        # Query 4
        # Write an SQL query
        # that selects an employees full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
        #### YOUR CODE HERE


    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    #### YOUR CODE HERE

    from .query_base import QueryBase

class Employee(QueryBase):
    """
    Class for employee-specific queries.
    This class knows everything about individual employees!
    """
    
    def __init__(self):
        super().__init__()
    
    def get_employee_info(self, employee_id):
        """
        Get basic info about one employee.
        Like looking up someone in a phone book!
        """
        query = """
        SELECT e.employee_id, e.first_name, e.last_name, e.team_id,
               t.team_name, t.shift, t.manager_name
        FROM employee e
        JOIN team t ON e.team_id = t.team_id
        WHERE e.employee_id = ?
        """
        return self.execute_query(query, [employee_id])
    
    def get_employee_events(self, employee_id, limit=None):
        """
        Get all performance events for an employee.
        Like getting someone's behavior chart from school!
        """
        query = """
        SELECT event_date, positive_events, negative_events,
               (positive_events - negative_events) as net_events
        FROM employee_events
        WHERE employee_id = ?
        ORDER BY event_date DESC
        """
        
        if limit:
            query += f" LIMIT {limit}"
            
        return self.execute_query(query, [employee_id])
    
    def get_employee_performance_stats(self, employee_id):
        """
        Get performance statistics for an employee.
        Like getting a summary report card!
        """
        query = """
        SELECT 
            employee_id,
            COUNT(*) as total_days_recorded,
            SUM(positive_events) as total_positive,
            SUM(negative_events) as total_negative,
            AVG(positive_events) as avg_positive_per_day,
            AVG(negative_events) as avg_negative_per_day,
            (SUM(positive_events) - SUM(negative_events)) as net_performance
        FROM employee_events
        WHERE employee_id = ?
        GROUP BY employee_id
        """
        return self.execute_query(query, [employee_id])
    
    def get_employee_notes(self, employee_id):
        """
        Get all notes for an employee.
        Like reading teacher comments!
        """
        query = """
        SELECT note_date, note
        FROM notes
        WHERE employee_id = ?
        ORDER BY note_date DESC
        """
        return self.execute_query(query, [employee_id])

    def model_data(self, id):

        return f"""
                    SELECT SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                """