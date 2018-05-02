from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World, from version 2.0!'

if __name__ == '__main__':
  app.run(port=80)
