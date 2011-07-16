from connection import Connection
from testconfig import TestConfig

host = TestConfig.host
port = TestConfig.port

conn = Connection(host, port, "test8888", "test", "test", "test")

conn.send("NICK " + TestConfig.nickname)
conn.send("USER " + TestConfig.username + " " + TestConfig.hostname + " " + TestConfig.servername + " :" + TestConfig. realname)

conn.start()

print "Execution terminated."
