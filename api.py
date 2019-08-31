import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


colors = [
    {
        'id': 0,
        'color': 'red',
		'value': '#f00'
	},
	{
        'id': 1,
		'color': 'green',
		'value': '#0f0'
	},
	{
        'id': 2,
		'color': 'blue',
		'value': '#00f'
	},
	{
        'id': 3,
		'color': 'cyan',
		'value': '#0ff'
	},
	{
        'id': 4,
		'color': 'magenta',
		'value': '#f0f'
	},
	{
        'id': 5,
		'color': 'yellow',
		'value': '#ff0'
	},
	{
        'id': 6,
		'color': 'black',
		'value': '#000'
	}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Color to HEX</h1>
<p>A prototype API for finding the corresponding HEX color code for a given color</p>'''

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/colors/all', methods=['GET'])
def api_all():
    return jsonify(colors)


@app.route('/api/v1/resources/colors', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for color in colors:
        if color['id'] == id:
            results.append(color)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()
