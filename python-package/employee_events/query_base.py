# Import any dependencies needed to execute sql queries
# YOUR CODE HERE

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
# YOUR CODE HERE

    # Create a class attribute called `name`
    # set the attribute to an empty string
    # YOUR CODE HERE

    # Define a `names` method that receives
    # no passed arguments
    # YOUR CODE HERE
        
        # Return an empty list
        # YOUR CODE HERE


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    # YOUR CODE HERE

        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        # YOUR CODE HERE
            
    

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    # YOUR CODE HERE

        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        # YOUR CODE HERE

from .sql_execution import DatabaseMixin

class QueryBase(DatabaseMixin):
    """
    Base class for all database queries.
    This is like the parent class that teaches other classes how to talk to the database!
    """
    
    def __init__(self):
        super().__init__()
    
    def get_all_teams(self):
        """Get all teams - like getting a list of all the different groups in the company"""
        query = """
        SELECT team_id, team_name, shift, manager_name 
        FROM team 
        ORDER BY team_name
        """
        return self.execute_query(query)
    
    def get_all_employees(self):
        """Get all employees - like getting a class roster!"""
        query = """
        SELECT e.employee_id, e.first_name, e.last_name, e.team_id, t.team_name
        FROM employee e
        JOIN team t ON e.team_id = t.team_id
        ORDER BY e.last_name, e.first_name
        """
        return self.execute_query(query)
    
    def get_performance_summary(self, start_date=None, end_date=None):
        """
        Get overall performance summary.
        Like getting a report card for everyone!
        """
        query = """
        SELECT 
            COUNT(DISTINCT employee_id) as total_employees,
            SUM(positive_events) as total_positive_events,
            SUM(negative_events) as total_negative_events,
            AVG(positive_events) as avg_positive_per_day,
            AVG(negative_events) as avg_negative_per_day
        FROM employee_events
        """
        
        params = []
        if start_date and end_date:
            query += " WHERE event_date BETWEEN ? AND ?"
            params = [start_date, end_date]
        
        return self.execute_query(query, params if params else None)
