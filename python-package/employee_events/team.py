# Import the QueryBase class
from .query_base import QueryBase

# Import dependencies for sql execution
from .sql_execution import query, QueryMixin

# Create a subclass of QueryBase
# called  `Team`
class Team(QueryBase):

    # Set the class attribute `name`
    # to the string "team"
    name = "team"


    # Define a `names` method
    # that receives no arguments
    # This method should return
    # a list of tuples from an sql execution
    def names(self):
        
        # Query 5
        # Write an SQL query that selects
        # the team_name and team_id columns
        # from the team table for all teams
        # in the database
        query_string = """
        SELECT 
            team_name,
            team_id
        FROM team
        ORDER BY team_name
        """
        
        return self.query(query_string)
    

    # Define a `username` method
    # that receives an ID argument
    # This method should return
    # a list of tuples from an sql execution
    def username(self, id):

        # Query 6
        # Write an SQL query
        # that selects the team_name column
        # Use f-string formatting and a WHERE filter
        # to only return the team name related to
        # the ID argument
        query_string = f"""
        SELECT team_name
        FROM team
        WHERE team_id = {id}
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
            t.team_id,
            t.team_name,
            t.shift,
            t.manager_name,
            COUNT(DISTINCT e.employee_id) as team_size,
            COUNT(ee.event_date) as total_days_recorded,
            SUM(ee.positive_events) as total_positive_events,
            SUM(ee.negative_events) as total_negative_events,
            AVG(ee.positive_events) as avg_positive_per_day,
            AVG(ee.negative_events) as avg_negative_per_day,
            (SUM(ee.positive_events) - SUM(ee.negative_events)) as net_performance
        FROM team t
        LEFT JOIN employee e ON t.team_id = e.team_id
        LEFT JOIN employee_events ee ON e.employee_id = ee.employee_id
        GROUP BY t.team_id, t.team_name, t.shift, t.manager_name
        ORDER BY net_performance DESC
        """
        
        return self.pandas_query(query_string)