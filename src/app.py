from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Howard Lau is now on AWS EC2'