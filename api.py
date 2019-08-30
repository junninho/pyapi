import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


colors = [
    {
        'color': 'red',
		'value': '#f00'
	},
	{
		'color': 'green',
		'value': '#0f0'
	},
	{
		'color': 'blue',
		'value': '#00f'
	},
	{
		'color': 'cyan',
		'value': '#0ff'
	},
	{
		'color': 'magenta',
		'value': '#f0f'
	},
	{
		'color': 'yellow',
		'value': '#ff0'
	},
	{
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

app.run()
