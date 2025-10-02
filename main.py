from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Google App Engine! 🚀"

if __name__ == "__main__":
    # For local testing
    app.run(host="0.0.0.0", port=8080, debug=True)
