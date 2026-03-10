from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Home page route
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

fraud_keywords = [
    "lottery",
    "win money",
    "otp",
    "redeem code",
    "bank details",
    "free gift",
    "click link"
]

@app.route('/check', methods=['POST'])
def check_message():
    data = request.json
    message = data['message'].lower()

    for word in fraud_keywords:
        if word in message:
            return jsonify({
                "status": "fraud",
                "result": "⚠️ Fraud Message Detected!"
            })

    return jsonify({
        "status": "safe",
        "result": "✅ Message Looks Safe"
    })

if __name__ == "__main__":
    app.run(debug=True)