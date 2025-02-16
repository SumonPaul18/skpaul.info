from flask import Flask, render_template
import yaml
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    with open("content.yml", 'r') as f:
        content = yaml.safe_load(f)
    return render_template('index.html', data=content)

if __name__ == '__main__':
    app.run(debug=True)
