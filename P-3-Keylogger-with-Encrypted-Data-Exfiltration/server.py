from flask import Flask, request

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    data = request.data
    with open("logs/received_logs.txt","ab") as f:
        f.write(data)
    return "Logs received"

app.run(host="127.0.0.1", port=5000)
