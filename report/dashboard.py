from fasthtml.common import *
import matplotlib.pyplot as plt

# Import QueryBase, Employee, Team from employee_events
#### YOUR CODE HERE

# import the load_model function from the utils.py file
#### YOUR CODE HERE

"""
Below, we import the parent classes
you will use for subclassing
"""
from base_components import (
    Dropdown,
    BaseComponent,
    Radio,
    MatplotlibViz,
    DataTable
    )

from combined_components import FormGroup, CombinedComponent


# Create a subclass of base_components/dropdown
# called `ReportDropdown`
#### YOUR CODE HERE
    
    # Overwrite the build_component method
    # ensuring it has the same parameters
    # as the Report parent class's method
    #### YOUR CODE HERE
        #  Set the `label` attribute so it is set
        #  to the `name` attribute for the model
        #### YOUR CODE HERE
        
        # Return the output from the
        # parent class's build_component method
        #### YOUR CODE HERE
    
    # Overwrite the `component_data` method
    # Ensure the method uses the same parameters
    # as the parent class method
    #### YOUR CODE HERE
        # Using the model argument
        # call the employee_events method
        # that returns the user-type's
        # names and ids


# Create a subclass of base_components/BaseComponent
# called `Header`
#### YOUR CODE HERE

    # Overwrite the `build_component` method
    # Ensure the method has the same parameters
    # as the parent class
    #### YOUR CODE HERE
        
        # Using the model argument for this method
        # return a fasthtml H1 objects
        # containing the model's name attribute
        #### YOUR CODE HERE
          

# Create a subclass of base_components/MatplotlibViz
# called `LineChart`
#### YOUR CODE HERE
    
    # Overwrite the parent class's `visualization`
    # method. Use the same parameters as the parent
    #### YOUR CODE HERE
    

        # Pass the `asset_id` argument to
        # the model's `event_counts` method to
        # receive the x (Day) and y (event count)
        #### YOUR CODE HERE
        
        # Use the pandas .fillna method to fill nulls with 0
        #### YOUR CODE HERE
        
        # User the pandas .set_index method to set
        # the date column as the index
        #### YOUR CODE HERE
        
        # Sort the index
        #### YOUR CODE HERE
        
        # Use the .cumsum method to change the data
        # in the dataframe to cumulative counts
        #### YOUR CODE HERE
        
        
        # Set the dataframe columns to the list
        # ['Positive', 'Negative']
        #### YOUR CODE HERE
        
        # Initialize a pandas subplot
        # and assign the figure and axis
        # to variables
        #### YOUR CODE HERE
        
        # call the .plot method for the
        # cumulative counts dataframe
        #### YOUR CODE HERE
        
        # pass the axis variable
        # to the `.set_axis_styling`
        # method
        # Use keyword arguments to set 
        # the border color and font color to black. 
        # Reference the base_components/matplotlib_viz file 
        # to inspect the supported keyword arguments
        #### YOUR CODE HERE
        
        # Set title and labels for x and y axis
        #### YOUR CODE HERE


# Create a subclass of base_components/MatplotlibViz
# called `BarChart`
#### YOUR CODE HERE

    # Create a `predictor` class attribute
    # assign the attribute to the output
    # of the `load_model` utils function
    #### YOUR CODE HERE

    # Overwrite the parent class `visualization` method
    # Use the same parameters as the parent
    #### YOUR CODE HERE

        # Using the model and asset_id arguments
        # pass the `asset_id` to the `.model_data` method
        # to receive the data that can be passed to the machine
        # learning model
        #### YOUR CODE HERE
        
        # Using the predictor class attribute
        # pass the data to the `predict_proba` method
        #### YOUR CODE HERE
        
        # Index the second column of predict_proba output
        # The shape should be (<number of records>, 1)
        #### YOUR CODE HERE
        
        
        # Below, create a `pred` variable set to
        # the number we want to visualize
        #
        # If the model's name attribute is "team"
        # We want to visualize the mean of the predict_proba output
        #### YOUR CODE HERE
            
        # Otherwise set `pred` to the first value
        # of the predict_proba output
        #### YOUR CODE HERE
        
        # Initialize a matplotlib subplot
        #### YOUR CODE HERE
        
        # Run the following code unchanged
        ax.barh([''], [pred])
        ax.set_xlim(0, 1)
        ax.set_title('Predicted Recruitment Risk', fontsize=20)
        
        # pass the axis variable
        # to the `.set_axis_styling`
        # method
        #### YOUR CODE HERE
 
# Create a subclass of combined_components/CombinedComponent
# called Visualizations       
#### YOUR CODE HERE

    # Set the `children`
    # class attribute to a list
    # containing an initialized
    # instance of `LineChart` and `BarChart`
    #### YOUR CODE HERE

    # Leave this line unchanged
    outer_div_type = Div(cls='grid')
            
# Create a subclass of base_components/DataTable
# called `NotesTable`
#### YOUR CODE HERE

    # Overwrite the `component_data` method
    # using the same parameters as the parent class
    #### YOUR CODE HERE
        
        # Using the model and entity_id arguments
        # pass the entity_id to the model's .notes 
        # method. Return the output
        #### YOUR CODE HERE
    

class DashboardFilters(FormGroup):

    id = "top-filters"
    action = "/update_data"
    method="POST"

    children = [
        Radio(
            values=["Employee", "Team"],
            name='profile_type',
            hx_get='/update_dropdown',
            hx_target='#selector'
            ),
        ReportDropdown(
            id="selector",
            name="user-selection")
        ]
    
# Create a subclass of CombinedComponents
# called `Report`
#### YOUR CODE HERE

    # Set the `children`
    # class attribute to a list
    # containing initialized instances 
    # of the header, dashboard filters,
    # data visualizations, and notes table
    #### YOUR CODE HERE

# Initialize a fasthtml app 
#### YOUR CODE HERE

# Initialize the `Report` class
#### YOUR CODE HERE


# Create a route for a get request
# Set the route's path to the root
#### YOUR CODE HERE

    # Call the initialized report
    # pass the integer 1 and an instance
    # of the Employee class as arguments
    # Return the result
    #### YOUR CODE HERE

# Create a route for a get request
# Set the route's path to receive a request
# for an employee ID so `/employee/2`
# will return the page for the employee with
# an ID of `2`. 
# parameterize the employee ID 
# to a string datatype
#### YOUR CODE HERE

    # Call the initialized report
    # pass the ID and an instance
    # of the Employee SQL class as arguments
    # Return the result
    #### YOUR CODE HERE

# Create a route for a get request
# Set the route's path to receive a request
# for a team ID so `/team/2`
# will return the page for the team with
# an ID of `2`. 
# parameterize the team ID 
# to a string datatype
#### YOUR CODE HERE

    # Call the initialized report
    # pass the id and an instance
    # of the Team SQL class as arguments
    # Return the result
    #### YOUR CODE HERE


# Keep the below code unchanged!
@app.get('/update_dropdown{r}')
def update_dropdown(r):
    dropdown = DashboardFilters.children[1]
    print('PARAM', r.query_params['profile_type'])
    if r.query_params['profile_type'] == 'Team':
        return dropdown(None, Team())
    elif r.query_params['profile_type'] == 'Employee':
        return dropdown(None, Employee())


@app.post('/update_data')
async def update_data(r):
    from fasthtml.common import RedirectResponse
    data = await r.form()
    profile_type = data._dict['profile_type']
    id = data._dict['user-selection']
    if profile_type == 'Employee':
        return RedirectResponse(f"/employee/{id}", status_code=303)
    elif profile_type == 'Team':
        return RedirectResponse(f"/team/{id}", status_code=303)
    


serve()

from fasthtml.common import *
from pathlib import Path
import sys

# Add the project root to the path so we can import our package
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

# Import our employee events package
from employee_events import Employee, Team

# Import utilities
from utils import load_model, get_recruitment_risk

# Import dashboard components
from base_components.data_table import DataTable
from base_components.dropdown import Dropdown
from base_components.matplotlib_viz import MatplotlibViz
from combined_components.form_group import FormGroup

# CSS for making our dashboard look nice!
css = """
body { 
    font-family: Arial, sans-serif; 
    margin: 0; 
    padding: 20px; 
    background-color: #f5f5f5;
}
.dashboard-header { 
    background-color: #2c3e50; 
    color: white; 
    padding: 20px; 
    border-radius: 8px; 
    margin-bottom: 20px;
}
.dashboard-content { 
    background-color: white; 
    padding: 20px; 
    border-radius: 8px; 
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.form-group { 
    margin-bottom: 20px; 
    padding: 15px; 
    background-color: #ecf0f1; 
    border-radius: 5px;
}
table { 
    width: 100%; 
    border-collapse: collapse; 
    margin-top: 10px;
}
th, td { 
    border: 1px solid #ddd; 
    padding: 8px; 
    text-align: left;
}
th { 
    background-color: #3498db; 
    color: white;
}
.risk-high { color: #e74c3c; font-weight: bold; }
.risk-medium { color: #f39c12; font-weight: bold; }
.risk-low { color: #27ae60; font-weight: bold; }
"""

# Create FastHTML app (like building the foundation of our dashboard!)
app = FastHTML(hdrs=[Style(css)])

# Load the machine learning model
model = load_model()

class EmployeePerformanceTable(DataTable):
    """
    A table that shows employee performance data.
    Like a report card table!
    """
    
    def component_data(self, entity_id, model):
        """Get the data for this employee"""
        employee_model = Employee()
        return employee_model.get_employee_performance_stats(entity_id)
    
    def build_component(self, entity_id, model):
        """Build the HTML table"""
        data = self.component_data(entity_id, model)
        
        if not data:
            return Div("No performance data available", style="color: red;")
        
        employee_data = data[0]
        
        # Calculate recruitment risk
        risk_score = get_recruitment_risk(model, employee_data)
        risk_level = "High" if risk_score > 0.7 else "Medium" if risk_score > 0.4 else "Low"
        risk_class = f"risk-{risk_level.lower()}"
        
        return Table(
            Thead(
                Tr(Th("Metric"), Th("Value"))
            ),
            Tbody(
                Tr(Td("Total Days Recorded"), Td(str(employee_data.get('total_days_recorded', 0)))),
                Tr(Td("Total Positive Events"), Td(str(employee_data.get('total_positive', 0)))),
                Tr(Td("Total Negative Events"), Td(str(employee_data.get('total_negative', 0)))),
                Tr(Td("Net Performance"), Td(str(employee_data.get('net_performance', 0)))),
                Tr(Td("Recruitment Risk"), Td(f"{risk_level} ({risk_score:.2%})", cls=risk_class)),
            )
        )

class TeamPerformanceTable(DataTable):
    """
    A table that shows team performance data.
    Like a class report card!
    """
    
    def component_data(self, entity_id, model):
        """Get team performance data"""
        team_model = Team()
        return team_model.get_team_performance_stats(entity_id)
    
    def build_component(self, entity_id, model):
        """Build the HTML table for team data"""
        data = self.component_data(entity_id, model)
        
        if not data:
            return Div("No team performance data available", style="color: red;")
        
        team_data = data[0]
        
        # Calculate average recruitment risk for team
        team_model = Team()
        members_data = team_model.get_team_member_performance(entity_id)
        
        if members_data:
            total_risk = sum(get_recruitment_risk(model, member) for member in members_data)
            avg_risk = total_risk / len(members_data)
            risk_level = "High" if avg_risk > 0.7 else "Medium" if avg_risk > 0.4 else "Low"
            risk_class = f"risk-{risk_level.lower()}"
        else:
            avg_risk = 0.5
            risk_level = "Medium"
            risk_class = "risk-medium"
        
        return Table(
            Thead(
                Tr(Th("Metric"), Th("Value"))
            ),
            Tbody(
                Tr(Td("Team Size"), Td(str(team_data.get('team_size', 0)))),
                Tr(Td("Total Days Recorded"), Td(str(team_data.get('total_days_recorded', 0)))),
                Tr(Td("Total Positive Events"), Td(str(team_data.get('total_positive', 0)))),
                Tr(Td("Total Negative Events"), Td(str(team_data.get('total_negative', 0)))),
                Tr(Td("Net Performance"), Td(str(team_data.get('net_performance', 0)))),
                Tr(Td("Average Recruitment Risk"), Td(f"{risk_level} ({avg_risk:.2%})", cls=risk_class)),
            )
        )

class EmployeeDropdown(Dropdown):
    """
    A dropdown to select employees.
    Like choosing from a list of students!
    """
    
    def component_data(self, entity_id, model):
        """Get list of all employees"""
        employee_model = Employee()
        return employee_model.get_all_employees()
    
    def build_component(self, entity_id, model):
        """Build the dropdown HTML"""
        employees = self.component_data(entity_id, model)
        
        options = [Option("Select an employee", value="")]
        for emp in employees:
            full_name = f"{emp['first_name']} {emp['last_name']} (ID: {emp['employee_id']})"
            options.append(Option(full_name, value=str(emp['employee_id'])))
        
        return Select(*options, name="employee_id", id="employee_select")

class TeamDropdown(Dropdown):
    """
    A dropdown to select teams.
    Like choosing from a list of classes!
    """
    
    def component_data(self, entity_id, model):
        """Get list of all teams"""
        team_model = Team()
        return team_model.get_all_teams()
    
    def build_component(self, entity_id, model):
        """Build the dropdown HTML"""
        teams = self.component_data(entity_id, model)
        
        options = [Option("Select a team", value="")]
        for team in teams:
            team_name = f"{team['team_name']} (ID: {team['team_id']})"
            options.append(Option(team_name, value=str(team['team_id'])))
        
        return Select(*options, name="team_id", id="team_select")

# Dashboard routes (like different pages in our website!)

@app.route("/")
def index():
    """
    Home page - like the front door of our dashboard!
    """
    return Html(
        Head(Title("Employee Performance Dashboard")),
        Body(
            Div(
                H1("Employee Performance Dashboard"),
                P("Welcome! This dashboard helps you track how employees are doing and if they might leave for other jobs."),
                cls="dashboard-header"
            ),
            Div(
                H2("Choose what you want to see:"),
                P(
                    A("View Individual Employee Performance", href="/employee", style="margin-right: 20px; padding: 10px; background-color: #3498db; color: white; text-decoration: none; border-radius: 5px;"),
                    A("View Team Performance", href="/team", style="padding: 10px; background-color: #2ecc71; color: white; text-decoration: none; border-radius: 5px;")
                ),
                cls="dashboard-content"
            )
        )
    )

@app.route("/employee")
def employee_dashboard():
    """
    Employee page - for looking at individual employees!
    """
    return Html(
        Head(Title("Employee Performance")),
        Body(
            Div(
                H1("Employee Performance"),
                A("← Back to Home", href="/", style="color: white; text-decoration: none;"),
                cls="dashboard-header"
            ),
            Div(
                Form(
                    Div(
                        Label("Select Employee:", fr="employee_select"),
                        EmployeeDropdown().build_component(None, None),
                        Button("View Performance", type="submit", style="margin-left: 10px; padding: 5px 15px; background-color: #3498db; color: white; border: none; border-radius: 3px;"),
                        cls="form-group"
                    ),
                    method="get",
                    action="/employee_view"
                ),
                cls="dashboard-content"
            )
        )
    )

@app.route("/team")
def team_dashboard():
    """
    Team page - for looking at whole teams!
    """
    return Html(
        Head(Title("Team Performance")),
        Body(
            Div(
                H1("Team Performance"),
                A("← Back to Home", href="/", style="color: white; text-decoration: none;"),
                cls="dashboard-header"
            ),
            Div(
                Form(
                    Div(
                        Label("Select Team:", fr="team_select"),
                        TeamDropdown().build_component(None, None),
                        Button("View Performance", type="submit", style="margin-left: 10px; padding: 5px 15px; background-color: #2ecc71; color: white; border: none; border-radius: 3px;"),
                        cls="form-group"
                    ),
                    method="get",
                    action="/team_view"
                ),
                cls="dashboard-content"
            )
        )
    )

@app.route("/employee_view")
def employee_view(employee_id: str = None):
    """
    Show detailed employee performance.
    """
    if not employee_id:
        return RedirectResponse("/employee")
    
    try:
        emp_id = int(employee_id)
        employee_model = Employee()
        emp_info = employee_model.get_employee_info(emp_id)
        
        if not emp_info:
            return Html(Body(H1("Employee not found"), A("← Back", href="/employee")))
        
        emp_data = emp_info[0]
        employee_name = f"{emp_data['first_name']} {emp_data['last_name']}"
        
        return Html(
            Head(Title(f"Performance: {employee_name}")),
            Body(
                Div(
                    H1(f"Employee Performance: {employee_name}"),
                    A("← Back to Employee Dashboard", href="/employee", style="color: white; text-decoration: none;"),
                    cls="dashboard-header"
                ),
                Div(
                    H2("Performance Summary"),
                    EmployeePerformanceTable().build_component(emp_id, model),
                    cls="dashboard-content"
                )
            )
        )
    except ValueError:
        return Html(Body(H1("Invalid employee ID"), A("← Back", href="/employee")))

@app.route("/team_view")
def team_view(team_id: str = None):
    """
    Show detailed team performance.
    """
    if not team_id:
        return RedirectResponse("/team")
    
    try:
        t_id = int(team_id)
        team_model = Team()
        team_info = team_model.get_team_info(t_id)
        
        if not team_info:
            return Html(Body(H1("Team not found"), A("← Back", href="/team")))
        
        team_data = team_info[0]
        team_name = team_data['team_name']
        
        return Html(
            Head(Title(f"Performance: {team_name}")),
            Body(
                Div(
                    H1(f"Team Performance: {team_name}"),
                    A("← Back to Team Dashboard", href="/team", style="color: white; text-decoration: none;"),
                    cls="dashboard-header"
                ),
                Div(
                    H2("Team Performance Summary"),
                    TeamPerformanceTable().build_component(t_id, model),
                    cls="dashboard-content"
                )
            )
        )
    except ValueError:
        return Html(Body(H1("Invalid team ID"), A("← Back", href="/team")))

# Run the application
if __name__ == "__main__":
    print("Starting Employee Performance Dashboard...")
    print("Visit http://localhost:5001 to see the dashboard!")
    serve(port=5001)
