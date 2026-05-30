from Flask import Flask
from database import init_db

app = Flask(__name__)

@app.route("/")
def func():
    return {
        "status": "running",
        "service": "document repository platform"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
