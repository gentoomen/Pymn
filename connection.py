import socket
import threading

class Connection (threading.Thread):

  host = None
  port = None
  sock = None

  username = None
  hostname = None
  servername = None
  realname = None

  def __init__(self, host, port, username, hostname, servername, realname):
    self.host = host
    self.port = port

    self.username = username
    self.hostname = hostname
    self.servername = servername
    self.realname = realname
  
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.connect((host, port))

    threading.Thread.__init__(self)

  def send(self, msg):
    self.sock.send(msg)

  def run(self):
    while True:
      data = self.sock.recv(4096) 
      print data
