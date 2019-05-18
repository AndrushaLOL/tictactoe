from flask import Flask
from tictactoe.client import connect
app = Flask(__name__)

@app.context_processor
def client_processor():
    return dict(connect=connect)

@app.context_processor
def client_processor():
    return dict(connect=connect)


from app import routes