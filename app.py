from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return "AI Sleep Monitoring Website is LIVE"

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=10000)