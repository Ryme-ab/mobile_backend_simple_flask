from flask import Flask, jsonify
import json
import datetime

app = Flask(__name__)

# -------------------------------
# Health check for Leapcell
# -------------------------------
@app.route('/kaithhealthcheck')
def healthcheck():
    return jsonify({"status": "ok"}), 200

# -------------------------------
# Endpoint: Get all news articles
# -------------------------------
@app.route('/news.all.get')
def get_news_all_articles():
    with open('news_data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

# -------------------------------
# Endpoint: Get news categories
# -------------------------------
@app.route('/news.categories.get')
def get_news_categories():
    time_now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {
        'title': 'List of Categories',
        'time': time_now_str,
        'categories': [
            {'id': 1, 'name': 'Sports'},
            {'id': 2, 'name': 'Politics'},
            {'id': 3, 'name': 'Education'}
        ]
    }
    return jsonify(data)

# -------------------------------
# Root route
# -------------------------------
@app.route('/')
def index():
    return '✅ Welcome ENSIA Students from Flask on Leapcell!'

# -------------------------------
# Run the Flask app
# -------------------------------
if __name__ == "__main__":
    # Use port 8080 so Leapcell can connect
    app.run(host="0.0.0.0", port=8080)
