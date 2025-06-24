from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/ping")
def ping():
    return jsonify(status="ok", service="2")


@app.route("/hello")
def hello():
    return jsonify(message="Hello from Service 2")


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.logger.info("Congrats! Server successfully started on port 8002 ")
    app.run(host="0.0.0.0", port=8002)
