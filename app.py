from flask import Flask, render_template, request, redirect, url_for, jsonify
import yaml
import os
from dotenv import load_dotenv
import markdown  # <-- এখানে ছোট হাতের 'm' ব্যবহার করতে হবে

load_dotenv()

app = Flask(__name__)

@app.template_filter('markdown')
def markdown_filter(text):
    return markdown.markdown(text, extensions=['fenced_code', 'tables'])

def load_config():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.yml')
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        return {}

config = load_config()

@app.route('/')
def index():
    return render_template('index.html', config=config)

@app.route('/api/status')
def system_status():
    """Mock API for System Status Dashboard"""
    return jsonify({
        "uptime": "99.9%",
        "cpu_usage": "12%",
        "memory_usage": "4.2GB / 16GB",
        "docker_containers": 8,
        "k8s_pods": 12,
        "last_deploy": "2 hours ago"
    })

@app.route('/send_email', methods=['POST'])
def send_email():
    # ... (আপনার আগের ইমেইল কোড িক আছে, শুধু JSON রেসপন্স যোগ করুন)
    if request.is_json:
        data = request.get_json()
        # Process AJAX request
        return jsonify({"status": "success", "message": "Email sent!"})
    
    # Fallback for form submission
    name = request.form.get('name', '')
    email_address = request.form.get('email', '')
    message = request.form.get('message', '')
    
    # ... (SMTP logic here)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)