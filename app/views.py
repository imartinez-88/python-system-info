from flask import Flask, jsonify # type: ignore
import platform
import psutil

app = Flask(__name__)

@app.route('/')
def home():
    return "OK"

@app.route('/info')
def info():
    return jsonify({
        "os": platform.system(),
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent
    })