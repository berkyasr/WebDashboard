from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("",9002  ))
try:
    while True:
        x = raw_input()
        s.send(x+"\n")
        data = s.recv(1024)
        print data
except KeyboardInterrupt:
    s.send("Connection closed by client")
    print "\nConnection with server interrupted"
    s.close()