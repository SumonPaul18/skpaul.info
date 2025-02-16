from flask import Flask, render_template, request, redirect, url_for
import yaml
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText

load_dotenv()

app = Flask(__name__)

def load_config():
    with open('config.yml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

config = load_config()
app.config['CONFIG'] = config

@app.route('/')
def index():
    return render_template('index.html', config=config)

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        name = request.form['name']
        email_address = request.form['email']
        message = request.form['message']

        # ইমেইল কনফিগারেশন .env ফাইল থেকে লোড করুন
        smtp_server = os.environ.get('SMTP_SERVER')
        smtp_port = os.environ.get('SMTP_PORT')
        smtp_username = os.environ.get('SMTP_USERNAME')
        smtp_password = os.environ.get('SMTP_PASSWORD')
        receiver_email = os.environ.get('RECEIVER_EMAIL') # আপনার ইমেল ঠিকানা .env ফাইলে যোগ করুন

        msg = MIMEText(f"নাম: {name}\nইমেইল: {email_address}\n\nমেসেজ:\n{message}")
        msg['Subject'] = f'Portfolio Contact Form - {name}'
        msg['From'] = smtp_username
        msg['To'] = receiver_email

        try:
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(smtp_username, smtp_password)
                server.sendmail(smtp_username, receiver_email, msg.as_string())
            return render_template('index.html', config=config, message_sent=True) # সাকসেস মেসেজের জন্য ভেরিয়েবল পাঠান
        except Exception as e:
            print(f"ইমেইল পাঠানোর সময় ত্রুটি: {e}")
            return render_template('index.html', config=config, message_error=True) # এরর মেসেজের জন্য ভেরিয়েবল পাঠান
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)