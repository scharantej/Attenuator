## Attenuator Controller Website Design

### HTML Files

- 1) attenuator_control.html
   - This file serves as the interface for the user to interact with the attenuator.
   - It contains a slider for each of the four channels, along with a label to indicate the channel number and a text field to display the selected attenuation value.

### Routes

- 1) @app.route('/', methods=['GET'])
   - This route handles GET requests to the root URL '/'.
   - It renders the attenuator_control.html file, providing the user with the interface to control the attenuator.

- 2) @app.route('/set_attenuation', methods=['POST'])
   - This route handles POST requests to '/set_attenuation'.
   - It receives attenuation values for the four channels via a form submission.
   - The route processes the attenuation values and sends the updated values to the attenuator hardware.
   - It then redirects the user back to the root URL '/'.