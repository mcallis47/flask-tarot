from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

EXTERNAL_SERVICE_URL= "localhost:8080"

@app.route('/tarot-reading', methods=['POST'])
def tarot_reading():
    posted_data = request.get_json()
    