import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/proxy/palestine', methods=['GET'])
def proxy_palestine():
    api_key = request.args.get('key')
    limit = request.args.get('limit', '200')
    
    if not api_key:
        return jsonify({"error": "Missing key"}), 400

    target_url = f"http://2.56.246.128:30194/api/v1/messages?limit={limit}"
    headers = {
        "X-API-Key": api_key,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
        "Accept": "application/json"
    }
    
    try:
        res = requests.get(target_url, headers=headers, timeout=15)
        return jsonify(res.json()), res.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "service": "Palestine Proxy"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
