# from flask import Flask
# app=Flask(__name__)
# @app.route("/")
# def home():
#     return "Hello ! docker running successfully"
# if __name__="__main__":
#     app.run(host="0.0.0.0",port=5002)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Docker Jenkins App Running Successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
