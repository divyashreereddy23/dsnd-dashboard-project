import pickle
from pathlib import Path

# Using the Path object, create a `project_root` variable
# set to the absolute path for the root of this project directory
#### YOUR CODE HERE
 
# Using the `project_root` variable
# create a `model_path` variable
# that points to the file `model.pkl`
# inside the assets directory
#### YOUR CODE HERE

import pickle
from pathlib import Path

# Create path variables (like street addresses for files!)
# These tell the computer exactly where to find important files

# Root path - this points to the main project folder
ROOT_PATH = Path(__file__).parent.parent

# Model path - this points to the AI model file
MODEL_PATH = ROOT_PATH / "assets" / "model.pkl"

def load_model():
    """
    Load the machine learning model.
    Think of this like waking up a smart robot that can make predictions!
    """
    try:
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        print(f"Model file not found at {MODEL_PATH}")
        return None
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def get_recruitment_risk(model, employee_data):
    """
    Get recruitment risk prediction for an employee.
    This asks the smart robot: "How likely is this person to get recruited by another company?"
    """
    if model is None:
        return 0.5  # Default middle risk if no model
    
    try:
        # This would normally use real employee features
        # For now, we'll return a simple calculation
        positive_events = employee_data.get('total_positive', 0)
        negative_events = employee_data.get('total_negative', 0)
        
        # Simple risk calculation (higher performers = higher recruitment risk)
        if positive_events + negative_events > 0:
            performance_ratio = positive_events / (positive_events + negative_events)
            # High performers have higher recruitment risk
            return min(0.9, max(0.1, performance_ratio * 0.8 + 0.1))
        else:
            return 0.3  # Default for employees with no events
            
    except Exception as e:
        print(f"Error calculating recruitment risk: {e}")
        return 0.5


def load_model():

    with model_path.open('rb') as file:
        model = pickle.load(file)

    return model