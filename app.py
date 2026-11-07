import os
import socket
from flask import Flask
import redis

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST", "db")
redis_port = int(os.environ.get("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route("/")
def index():
    count = r.incr("hits")
    hostname = socket.gethostname()
    return f"Navštíveno {count}×, odpovídá kontejner {hostname}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
