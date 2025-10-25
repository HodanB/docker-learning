#app.py

from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "redis-1")
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_db = int(os.getenv("REDIS_DB", 0))

r = redis.Redis(host=redis_host, port=redis_port)
@app.route('/')
def hello():
    return f'Hello! Welcome to the Flask app connected to Redis at {redis_host}.'
@app.route("/count")
def count():
    hits = r.incr("visit_count")
    return f"This page has been viewed {hits} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
