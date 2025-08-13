from fasthtml.common import *
import matplotlib.pyplot as plt
import pandas as pd
import asyncio

# Import QueryBase, Employee, Team from employee_events
from employee_events import QueryBase, Employee, Team

# import the load_model function from the utils.py file
from utils import load_model

"""
Below, we import the parent classes
to use for subclassing
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
class ReportDropdown(Dropdown):
    
    # Overwrite the build_component method
    # ensuring it has the same parameters
    # as the Report parent class's method
    def build_component(self, entity_id, model):
        #  Set the `label` attribute so it is set
        #  to the `name` attribute for the model
        self.label = model.name
        
        # Return the output from the
        # parent class's build_component method
        return super().build_component(entity_id, model)
    
    # Overwrite the `component_data` method
    # Ensure the method uses the same parameters
    # as the parent class method
    def component_data(self, entity_id, model):
        # Using the model argument
        # call the employee_events method
        # that returns the user-type's
        return model.names()


# Create a subclass of base_components/BaseComponent
# called `Header`
class Header(BaseComponent):

    # Overwrite the `build_component` method
    # Ensure the method has the same parameters
    # as the parent class
    def build_component(self, entity_id, model):
        
        # Using the model argument for this method
        # return a fasthtml H1 objects
        # containing the model's name attribute
        return H1(model.name)
          

# Create a subclass of base_components/MatplotlibViz
# called `LineChart`
class LineChart(MatplotlibViz):
    
    # Overwrite the parent class's `visualization`
    # method. Use the same parameters as the parent
    def visualization(self, asset_id, model):
    

        # Pass the `asset_id` argument to
        # the model's `event_counts` method to
        # receive the x (Day) and y (event count)
        data = model.event_counts(asset_id)
        
        # Use the pandas .fillna method to fill nulls with 0
        data = data.fillna(0)
        
        # User the pandas .set_index method to set
        # the date column as the index
        data = data.set_index('event_date')
        
        # Sort the index
        data = data.sort_index()
        
        # Use the .cumsum method to change the data
        # in the dataframe to cumulative counts
        data = data.cumsum()
        
        
        # Set the dataframe columns to the list
        # ['Positive', 'Negative']
        data.columns = ['Positive', 'Negative']
        
        # Initialize a pandas subplot
        # and assign the figure and axis
        # to variables
        fig, ax = plt.subplots()
        
        # call the .plot method for the
        # cumulative counts dataframe
        data.plot(ax=ax)
        
        # pass the axis variable
        # to the `.set_axis_styling`
        # method
        # Use keyword arguments to set 
        # the border color and font color to black. 
        # Reference the base_components/matplotlib_viz file 
        # to inspect the supported keyword arguments
        self.set_axis_styling(ax)
        
        # Set title and labels for x and y axis
        ax.set_title('Cumulative Event Counts Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Cumulative Count')


# Create a subclass of base_components/MatplotlibViz
# called `BarChart`
class BarChart(MatplotlibViz):

    # Create a `predictor` class attribute
    # assign the attribute to the output
    # of the `load_model` utils function
    predictor = load_model()

    # Overwrite the parent class `visualization` method
    # Use the same parameters as the parent
    def visualization(self, asset_id, model):
        try:
            # Get the ML data
            data = model.ml_data()
        
            if len(data) > 0:
                # Create features with the exact names the model expects
                model_features = pd.DataFrame({
                    'positive_events': data['total_positive_events'].fillna(0),
                    'negative_events': data['total_negative_events'].fillna(0)
                })
            
                # Make prediction using the correctly named features
                predictions = self.predictor.predict_proba(model_features)
            
                # Index the second column of predict_proba output
                predictions = predictions[:, 1]
            
                # Set pred based on model type
                if model.name == "team":
                    pred = predictions.mean()
                else:
                    pred = predictions[0]
            else:
                pred = 0.5  # Default if no data
            
        except Exception as e:
            print(f"ML prediction error: {e}")
            pred = 0.5  # Fallback value
    
        # Initialize matplotlib subplot
        fig, ax = plt.subplots()
    
        # Create bar chart
        ax.barh([''], [pred])
        ax.set_xlim(0, 1)
        ax.set_title('Predicted Recruitment Risk', fontsize=20)
    
        # Apply styling
        self.set_axis_styling(ax)

 
# Create a subclass of combined_components/CombinedComponent
# called Visualizations       
class Visualizations(CombinedComponent):

    # Set the `children`
    # class attribute to a list
    # containing an initialized
    # instance of `LineChart` and `BarChart`
    children = [LineChart(), BarChart()]

    # Leave this line unchanged
    outer_div_type = Div(cls='grid')
            
# Create a subclass of base_components/DataTable
# called `NotesTable`
class NotesTable(DataTable):

    # Overwrite the `component_data` method
    # using the same parameters as the parent class
    def component_data(self, entity_id, model):
        
        # Using the model and entity_id arguments
        # pass the entity_id to the model's .notes 
        # method. Return the output
        return model.notes(entity_id)
    

class DashboardFilters(BaseComponent):
    """Simple form component that ensures proper POST submission"""
    
    def build_component(self, entity_id, model):
        # Get employee and team data for dropdowns
        employee_model = Employee()
        team_model = Team()
        
        employees = employee_model.names()
        teams = team_model.names()
        
        return Form(
            Div(
                # Radio buttons for Employee/Team selection
                Label("Select Type:"),
                Br(),
                Input(type="radio", name="profile_type", value="Employee", id="emp_radio", checked=True),
                Label("Employee", fr="emp_radio"),
                Input(type="radio", name="profile_type", value="Team", id="team_radio"),
                Label("Team", fr="team_radio"),
                style="margin: 10px 0;"
            ),
            
            Div(
                # Dropdown for employee selection  
                Label("Select Employee:"),
                Select(
                    Option("Select an employee", value=""),
                    *[Option(f"{emp[0]} (ID: {emp[1]})", value=str(emp[1])) 
                      for emp in employees],
                    name="user-selection",
                    id="employee_select"
                ),
                style="margin: 10px 0;"
            ),
            
            Div(
                # Submit button
                Button("Submit", type="submit", 
                       style="padding: 8px 16px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer;"),
                style="margin: 10px 0;"
            ),
            
            # These attributes make the POST request work
            action="/update_data",
            method="POST",
            style="border: 1px solid #ddd; padding: 15px; margin: 20px 0; border-radius: 5px;"
        )
    
# Create a subclass of CombinedComponents
# called `Report`
class Report(CombinedComponent):

    # Set the `children`
    # class attribute to a list
    # containing initialized instances 
    # of the header, dashboard filters,
    # data visualizations, and notes table
    children = [Header(), DashboardFilters(), Visualizations(), NotesTable()]

# Initialize a fasthtml app 
app = FastHTML()

# Add this right after creating your FastHTML app
@app.route("/{path:path}", methods=["POST", "PUT", "DELETE", "PATCH"])
async def catch_all_posts(request):
    print(f"🚨 CAUGHT POST REQUEST:")
    print(f"   Method: {request.method}")
    print(f"   URL: {request.url}")
    print(f"   Path: {request.url.path}")
    try:
        form_data = await request.form()
        print(f"   Form data: {dict(form_data)}")
    except Exception as e:
        print(f"   Form data error: {e}")
    
    return {"error": f"Unsupported {request.method} request to {request.url.path}"}

# Initialize the `Report` class
report = Report()


# Create a route for a get request
# Set the route's path to the root
@app.get("/")
def home():

    # Call the initialized report
    # pass the integer 1 and an instance
    # of the Employee class as arguments
    # Return the result
    return report(1, Employee())

# Create a route for a get request
# Set the route's path to receive a request
# for an employee ID so `/employee/2`
# will return the page for the employee with
# an ID of `2`. 
# parameterize the employee ID 
# to a string datatype
@app.get("/employee/{id:str}")
def employee_page(id: str):

    # Call the initialized report
    # pass the ID and an instance
    # of the Employee SQL class as arguments
    # Return the result
    return report(id, Employee())

# Create a route for a get request
# Set the route's path to receive a request
# for a team ID so `/team/2`
# will return the page for the team with
# an ID of `2`. 
# parameterize the team ID 
# to a string datatype
@app.get("/team/{id:str}")
def team_page(id: str):

    # Call the initialized report
    # pass the id and an instance
    # of the Team SQL class as arguments
    # Return the result
    return report(id, Team())


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
    print("🎯 POST ROUTE HIT!")
    try:
        form_data = await request.form()
        print(f"📝 Form data: {dict(form_data)}")
        
        profile_type = form_data.get('profile_type')
        user_selection = form_data.get('user-selection')
        
        if profile_type == 'Employee' and user_selection:
            return RedirectResponse(f"/employee/{user_selection}", status_code=303)
        elif profile_type == 'Team' and user_selection:
            return RedirectResponse(f"/team/{user_selection}", status_code=303)
        else:
            return RedirectResponse("/", status_code=303)
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return RedirectResponse("/", status_code=303)

serve()