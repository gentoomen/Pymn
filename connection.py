# Connection.py
# Handles a single connection to a server

import Queue
import socket
import time
import threading

class Connection (threading.Thread):

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
    threading.Thread.__init__(self)
    
  def connect(self):
    print "connecting"
    self.__connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.__connection.connect((self.__host, self.__port))
    self.__messages = Queue.LifoQueue()
    self.__connected = True
    
  def sendMessage(self, msg):
    print "sending message"
    self.__connection.send(msg)
      
  def getMessage(self):
    print "getting message"
    return self.__messages.get(True, self.__timeout)
  
  def hasMessage(self):
    print "checking messages"
    return not self.__messages.empty()
      
  def run (self):
    while (self.__connected):
      message = self.__connection.recv(self.__bufferSize)
      print message
      while (not message == ''):
        partition = ''
        partition = message.partition(partition, "\n")
        self.__messages.put(partition[0], True, self.__timeout)
        message = partition[2]
      print "sleeping"
      time.sleep(self.__sleepTime)

