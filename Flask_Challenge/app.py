#app.py

from flask import Flask
import redis
import os
import random

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "redis-1")
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_db = int(os.getenv("REDIS_DB", 0))

r = redis.Redis(host=redis_host, port=redis_port)
@app.route('/')
def home():
    return f"""
    <html>
      <head><title>Visit Tracker Pro</title></head>
      <body style="text-align:center; font-family:sans-serif;">
        <h1>🌍 Visit Tracker Pro</h1>
        <p>Your go-to app for tracking page visits using Redis!</p>
        <h2>Features:</h2>
        <ul style="list-style-type:none;">
          <li>✅ Real-time visit counting</li>
          <li>✅ Simple and intuitive interface</li>
          <li>✅ Built with Flask and Redis</li>
        </ul>
        <h2>Technologies Used:</h2>
        <p>Flask for the web framework and Redis for fast, in-memory data storage.</p>
        <h2>Get Started:</h2>
        <p>Visit the <a href="/count">/count</a> page to see the visit counter in action!</p>
      </body>
    </html>     
    """

@app.route("/count")
def count():
    hits = r.incr("visit_count")
    return f"""
    <html>
        <head><title>Visit Counter</title></head>
        <body style="text-align:center; font-family:sans-serif;">
            <h1>🚀 Welcome to the Visit Counter!</h1>
            <p>This page has been visited <strong>{hits}</strong> times.</p>
            <p>Hi there, lucky {hits} {random.choice(['👋', '😊', '🌟', '🔥', '💡'])}! </p>
            <a href="/">Back to Home</a>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
