from tictactoe.server import ServerThread
from threading import Thread
from app import app

serv = ServerThread()
serv.start()
serv.join()
app.run()
