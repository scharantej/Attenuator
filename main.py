
# Import the necessary modules.
from flask import Flask, request, redirect, render_template

# Create a Flask app.
app = Flask(__name__)

# Define the route for the main page.
@app.route('/', methods=['GET'])
def index():
    """Render the main page."""
    # Render the attenuator_control.html template.
    return render_template('attenuator_control.html')

# Define the route for setting the attenuation.
@app.route('/set_attenuation', methods=['POST'])
def set_attenuation():
    """Set the attenuation values for the four channels."""
    # Get the attenuation values from the form submission.
    attenuation_values = request.form.getlist('attenuation')

    # Check if all four attenuation values are valid.
    for attenuation_value in attenuation_values:
        if not (0 <= int(attenuation_value) <= 95):
            return redirect('/')

    # Send the updated attenuation values to the attenuator hardware.

    # Redirect the user back to the main page.
    return redirect('/')

# Run the app.
if __name__ == '__main__':
    app.run(debug=True)
