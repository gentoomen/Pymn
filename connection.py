import socket
import threading
import time

class Connection (threading.Thread):

  host = None #server hostname
  port = None #server port
  sock = None #socket object to connect to server

  username = None
  hostname = None
  servername = None
  realname = None

  buffer = None #buffer used to store incomplete lines

  def __init__(self, host, port, username, hostname, servername, realname):
    self.host = host
    self.port = port

    self.username = username
    self.hostname = hostname
    self.servername = servername
    self.realname = realname

    self.buffer = ''
  
    #initialize connection
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.connect((host, port))

    #start new thread for connection
    threading.Thread.__init__(self)

  #helper function to send raw data over socket
  def send(self, msg):
    self.sock.send(msg + "\r\n")

  #infinite loop:
  #1. grab 4kb of data
  #2. split data into lines
  #3. if there is data in the buffer, prepend it to the first line
  #4. if there is an incomplete line, store it in the buffer
  #5. print all lines (later will parse all lines)
  #6. sleep for a reasonable amount of time
  def run(self):
    while True:
      data = self.sock.recv(4096) 
      if (data != ''):
        lines = data.splitlines()
        if (self.buffer != ''):
          lines[0] = self.buffer + lines[0]
          self.buffer = ''
        if (data[-1] != '\n'):
          self.buffer = lines.pop(-1)
        for line in lines:
          print "<- " + line
      time.sleep (0.1)
