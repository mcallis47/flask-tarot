from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TAROT_SERVICE_URL = "http://172.24.0.1:8081"


@app.route('/tarot-reading', methods=['POST'])
def tarot_reading():
    posted_data = request.get_json()
    spread = posted_data.get("spread")
    arrangement = 4
    if "arrangement" in posted_data :
        arrangement = posted_data.get("arrangement")
    spread_res = {}
    arrangement_res = {}
    try:
        spread_res = requests.get(TAROT_SERVICE_URL + "/spreads/" + str(spread)).json()
        arrangement_res = requests.get(TAROT_SERVICE_URL + "/arrangements/" + str(arrangement)).json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error":str(e)}), 500
    
    
    return spread_res

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)