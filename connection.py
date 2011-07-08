# Connection.py
# Handles a single connection to a server

import Queue
import socket
import time

class Connection:

  __connection = None
  __messages = None
  __host = None
  __port = None
  __timeout = 60      # Timeout for queueing/receiving a message
  __bufferSize = 4096 # Size of receive buffer
  __sleepTime = 0.1   # Time to sleep
  __connected = None
  
  def __init__(self, host, port):
    self.__host = host
    self.__port = port
    self.connect()
    
  def connect(self):
    self.__connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.__connection.connect((self.__host, self.__port))
    self._messages = Queue()
    self.__connected = True
    
  def sendMessage(self, msg):
    self.__connection.send(msg)
      
  def getMessage(self):
    return self.__messages.get(True, self.__timeout)
  
  def hasMessage(self):
    return not self.__messages.empty()
      
  def run (self):
    while (self.__connected):
      message = self.__connection.recv(self.__bufferSize)
      while (not message == ''):
        partition = str.partition(message)
        self.__messages.put(partition[0], True, self.__timeout)
        message = partition[2]
      time.sleep(self.__sleepTime)

