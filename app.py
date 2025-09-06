from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# URL Tika server (phải chạy sẵn bằng java -jar tika-server-standard-3.2.2.jar)
TIKA_URL = "http://localhost:9998"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    endpoint = request.form.get("endpoint", "/tika")
    url = TIKA_URL.rstrip("/") + endpoint

    headers = {"Accept": "application/json"} if endpoint in ["/meta", "/rmeta"] else {"Accept": "text/plain"}

    resp = requests.put(url, data=file.stream, headers=headers)

    return resp.text, resp.status_code, {"Content-Type": resp.headers.get("Content-Type", "text/plain")}

if __name__ == "__main__":
    app.run(debug=True)
