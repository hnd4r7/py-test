from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/health")
def home():
    return "up"

app.run(debug=True)

