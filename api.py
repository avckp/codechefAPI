from flask import Flask, jsonify, render_template
import requests

from settings import *
from utils import *

app = Flask(__name__)

@app.route('/')
def home():
	"""
	Static Home Page
	"""
	return render_template('home.html')


@app.route('/ranks/<id>')
def codechef_api(id):
	"""
	Returns the user stat in JSON after fetching from Codechef.
	"""
	if is_user_valid(id):
		response = requests.post(BASE_URL + id)
		if response.status_code is 200:
			user_data = parse_html(response.content)

			if not user_data:
				return jsonify({'status' : 'Retry',
				'data' : {}
					})

			return jsonify({'status' : 'OK', 
				'data' : build_response_dict(user_data)
				})
		else:
			return jsonify({'status' : 'ERROR',
				'data' : {}
				})
	else:
		return jsonify({'status' : 'INVALID username',
				'data' : {}
			})

if __name__ == '__main__':
	app.run(debug=True)