from flask import Flask, render_template
import yaml
import os
from dotenv import load_dotenv
from flask_mail import Mail, Message

load_dotenv()

app = Flask(__name__)
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
mail = Mail(app)

def load_config():
    with open('config.yml') as f:
        return yaml.safe_load(f)

@app.route('/')
def index():
    try:
        with open('config.yml') as f:
            config = yaml.safe_load(f)
        return render_template('index.html', config=config)
    except Exception as e:
        print(f"Error loading config: {e}")
        return "Configuration Error", 500

if __name__ == '__main__':
    app.run(debug=True)