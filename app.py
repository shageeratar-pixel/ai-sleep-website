from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Sleep Monitoring Backend is LIVE"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    sleep_hours = data.get("sleep_hours", 0)
    movement = data.get("movement", 0)

    # Simple demo logic (replace with AI later)
    if sleep_hours >= 7 and movement < 5:
        result = "Good Sleep"
    else:
        result = "Poor Sleep"

    return jsonify({
        "sleep_quality": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
