from connection import Connection

host = "irc.rizon.net"
port = 6667

conn = Connection(host, port, "test8888", "test", "test", "test")

conn.send("NICK test123456\r\n")
conn.send("USER test test test :test\r\n")

conn.start()

print "Execution terminated."
