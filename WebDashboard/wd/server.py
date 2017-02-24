import threading
import socket
import app

class Agent(threading.Thread):
    def __init__(self,server,socket,id):
        threading.Thread.__init__(self)
        self._server = server
        self._socket = socket
        self._app = app.Application()
        self._id = id
        
    def run(self):
        l = self._socket[0].recv(1024)
        
        while l :
            com = l.strip('\n').split(' ')
            print "Connection " + str(self._id) + " asked for: " + str(com)
            response = 'Done'
            if com[0] == "available" :
                response = str(self._app.available())
                self._socket[0].send(response)
            elif com[0] == "loaded" :
                response = str(self._app.loaded())
                self._socket[0].send(response)
            elif com[0] == "load" :
                try:
                    if(len(com)>1):
                        self._app.load(com[1])
                        self._socket[0].send(response)
                    else:
                        self._socket[0].send('Mismatch.')
                except Exception as errStr:
                    self._socket[0].send(str(errStr))
                    print "Client " + str(self._id) + " tried to load a non-existent component"
            elif com[0] == "loadDesign" :
                if(len(com)>1):
                    self._app.loadDesign(com[1])
                    self._socket[0].send(response)
                else:
                    self._socket[0].send('Mismatch.')
            elif com[0] == "saveDesign" :
                if(len(com)>1):
                    self._app.saveDesign(com[1])
                    self._socket[0].send(response)
                else:
                    self._socket[0].send('Mismatch.')
            elif com[0] == "addInstance":
                try:
                    if(len(com)>3):
                        self._app.addInstance(com[1], int(com[2]), int(com[3]))
                        self._socket[0].send(response)
                    else:
                        self._socket[0].send('Mismatch.')
                except Exception as err:
                    self._socket[0].send(str(err))
                    print "Client " + str(self._id) + " got error: " + str(err)
            elif com[0] == "instances" :
                response = str(self._app.instances())
                self._socket[0].send(response)
            elif com[0] == "removeInstance" :
                try:
                    if(len(com)>1):
                        self._app.removeInstance(com[1])
                        self._socket[0].send(response)
                    else:
                        self._socket[0].send('Mismatch.')
                except Exception as err:
                    self._socket[0].send(str(err))
                    print "Client " + str(self._id) + " got error: " + str(err)
                    
            elif com[0] == "callMethod" :
                try:
                    if(len(com)>2):
                        response = self._app.callMethod(com[1], com[2], com[3:])
                        if response :
                            self._socket[0].send(response)
                        else :
                            self._socket[0].send("Done")
                    else:
                        self._socket[0].send('Mismatch.')
                except Exception as err:
                    self._socket[0].send(str(err))
                    print "Client " + str(self._id) + " got error: " + str(err)
            elif com[0] == "execute" :
                response = self._app.execute()
                self._socket[0].send(str(response))
            #if com[0] in dir(self._app):


            else:
                self._socket[0].send("You didn't enter a valid command.")
            l = self._socket[0].recv(1024)
            
        print "Connection " + str(self._id) + " closed"
        
        
class Server(object):
    def __init__(self,port = 9002):
        self._socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self._socket.bind(('',port))
        self._socket.listen(5)
        self._count = 1
        
    def start(self):
        try:
            c = self._socket.accept()
            while c :
                a = Agent(self,c,self._count)
                a.start()
                
                self._count += 1
            
                c = self._socket.accept()
            return
        except KeyboardInterrupt:
            print "\nServer Interrupted"
            
            
             
if __name__ == "__main__" :
    s = Server()
    s.start()       
        
        
