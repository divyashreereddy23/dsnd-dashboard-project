# Import the QueryBase class
# YOUR CODE HERE

# Import dependencies for sql execution
#### YOUR CODE HERE

# Create a subclass of QueryBase
# called  `Team`
#### YOUR CODE HERE

    # Set the class attribute `name`
    # to the string "team"
    #### YOUR CODE HERE


    # Define a `names` method
    # that receives no arguments
    # This method should return
    # a list of tuples from an sql execution
    #### YOUR CODE HERE
        
        # Query 5
        # Write an SQL query that selects
        # the team_name and team_id columns
        # from the team table for all teams
        # in the database
        #### YOUR CODE HERE
    

    # Define a `username` method
    # that receives an ID argument
    # This method should return
    # a list of tuples from an sql execution
    #### YOUR CODE HERE

        # Query 6
        # Write an SQL query
        # that selects the team_name column
        # Use f-string formatting and a WHERE filter
        # to only return the team name related to
        # the ID argument
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

class Team(QueryBase):
    """
    Class for team-specific queries.
    This class knows everything about teams and groups!
    """
    
    def __init__(self):
        super().__init__()
    
    def get_team_info(self, team_id):
        """
        Get basic information about a team.
        Like getting details about a sports team!
        """
        query = """
        SELECT team_id, team_name, shift, manager_name
        FROM team
        WHERE team_id = ?
        """
        return self.execute_query(query, [team_id])
    
    def get_team_members(self, team_id):
        """
        Get all employees in a team.
        Like getting a list of everyone in your class!
        """
        query = """
        SELECT employee_id, first_name, last_name
        FROM employee
        WHERE team_id = ?
        ORDER BY last_name, first_name
        """
        return self.execute_query(query, [team_id])
    
    def get_team_performance_stats(self, team_id):
        """
        Get performance statistics for a whole team.
        Like getting the whole class's grade average!
        """
        query = """
        SELECT 
            ee.team_id,
            COUNT(DISTINCT ee.employee_id) as team_size,
            COUNT(ee.event_date) as total_days_recorded,
            SUM(ee.positive_events) as total_positive,
            SUM(ee.negative_events) as total_negative,
            AVG(ee.positive_events) as avg_positive_per_day,
            AVG(ee.negative_events) as avg_negative_per_day,
            (SUM(ee.positive_events) - SUM(ee.negative_events)) as net_performance
        FROM employee_events ee
        WHERE ee.team_id = ?
        GROUP BY ee.team_id
        """
        return self.execute_query(query, [team_id])
    
    def get_team_events_by_date(self, team_id, limit=None):
        """
        Get team performance events organized by date.
        Like seeing how the whole class did each day!
        """
        query = """
        SELECT 
            event_date,
            SUM(positive_events) as daily_positive,
            SUM(negative_events) as daily_negative,
            COUNT(employee_id) as employees_recorded,
            (SUM(positive_events) - SUM(negative_events)) as daily_net
        FROM employee_events
        WHERE team_id = ?
        GROUP BY event_date
        ORDER BY event_date DESC
        """
        
        if limit:
            query += f" LIMIT {limit}"
            
        return self.execute_query(query, [team_id])
    
    def get_team_member_performance(self, team_id):
        """
        Get individual performance stats for all team members.
        Like getting everyone's individual report cards in the class!
        """
        query = """
        SELECT 
            e.employee_id,
            e.first_name,
            e.last_name,
            COUNT(ee.event_date) as days_recorded,
            SUM(ee.positive_events) as total_positive,
            SUM(ee.negative_events) as total_negative,
            AVG(ee.positive_events) as avg_positive,
            AVG(ee.negative_events) as avg_negative,
            (SUM(ee.positive_events) - SUM(ee.negative_events)) as net_performance
        FROM employee e
        LEFT JOIN employee_events ee ON e.employee_id = ee.employee_id
        WHERE e.team_id = ?
        GROUP BY e.employee_id, e.first_name, e.last_name
        ORDER BY net_performance DESC
        """
        return self.execute_query(query, [team_id])

    def model_data(self, id):

        return f"""
            SELECT positive_events, negative_events FROM (
                    SELECT employee_id
                         , SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                    GROUP BY employee_id
                   )
                """