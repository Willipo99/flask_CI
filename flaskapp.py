from flask import Flask
from redis import Redis, RedisError
import os
import socket

#connect to my redis instance
redis = Redis(host="redis-server", db=0, socket_timeout=2, socket_connect_timeout=10)

#create a new application instance
app = Flask(__name__)

#define my routes
@app.route("/")
def index():
    return "<h1> Hello World ! </h1>"

@app.route("/visit")
def visit_counting():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i> I cannot connect to Redis, I don't know why... </i>"
    html = "<h1> Number of visits : {}</h1>, \n Hostname {}".format(visits, socket.gethostname())
    return html

if __name__ == "__main__":
    app.run(debut=True, port=80, host='0.0.0.0')