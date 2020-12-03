from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'hello universe!'

@app.route('/bye')
def bye_world():
  return 'bye universe!!'