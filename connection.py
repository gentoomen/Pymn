import socket
import threading
import time

class Connection (threading.Thread):

  host = None
  port = None
  sock = None

  username = None
  hostname = None
  servername = None
  realname = None

  buffer = None

  def __init__(self, host, port, username, hostname, servername, realname):
    self.host = host
    self.port = port

    self.username = username
    self.hostname = hostname
    self.servername = servername
    self.realname = realname

    self.buffer = ''
  
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.connect((host, port))

    threading.Thread.__init__(self)

  def send(self, msg):
    self.sock.send(msg + "\r\n")

  def run(self):
    while True:
      data = self.sock.recv(4096) 
      if (data != ''):
        lines = data.splitlines()
        if (data[-1] != '\n'):
          lines[0] = self.buffer + lines[0]
          buffer = lines.pop(-1)
        for line in lines:
          print "<- " + line
      time.sleep (0.1)
