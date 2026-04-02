from __future__ import annotations

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'service': 'impact-predictor-api'})
