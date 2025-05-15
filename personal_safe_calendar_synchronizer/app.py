from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route('/', methods=['POST'])
def create_calendar_event():
    data = request.get_json()
    # Process the data as needed
    return jsonify({"message": "POST request received", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True)