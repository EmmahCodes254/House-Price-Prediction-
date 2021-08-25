from flask import Flask, request, jsonify
from flask.wrappers import Response
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names
    })
    response.headers.add('Access-Control-Allow-origin', '*')
    return response


if __name__ == "__main__":
    app.run(debug=True)