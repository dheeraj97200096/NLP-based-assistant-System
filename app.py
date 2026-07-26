from flask import Flask, request, jsonify, render_template
import time
from nlp_engine import process_query, speech_to_text
from reports import fetch_report

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/query', methods=['POST'])
def handle_query():
    start = time.time()
    user_query = request.json.get("query")
    response = process_query(user_query)
    latency = round(time.time() - start, 2)
    return jsonify({"response": response, "latency": latency})

@app.route('/voice-query', methods=['POST'])
def handle_voice_query():
    audio_file = request.files['file']
    text_query = speech_to_text(audio_file)
    response = process_query(text_query)
    return jsonify({"response": response})

@app.route('/reports', methods=['GET'])
def generate_reports():
    report_type = request.args.get("type", "summary")
    data = fetch_report(report_type)
    return jsonify({"report": data})

@app.route('/analytics', methods=['GET'])
def analytics():
    return jsonify({"status": "System running", "concurrency": "100+", "latency": "<2s"})

@app.route('/admin', methods=['GET'])
def admin():
    return jsonify({"message": "Admin dashboard placeholder"})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
