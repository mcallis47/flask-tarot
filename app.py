from flask import Flask, request, jsonify

app = Flask(__name__)

EXTERNAL_SERVICE_URL = "localhost:8080"

@app.route('/tarot-reading', methods=['POST'])
def tarot_reading():
    posted_data = request.get_json()
    print(posted_data.get("deck"))
    return jsonify(posted_data.get("deck"))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)