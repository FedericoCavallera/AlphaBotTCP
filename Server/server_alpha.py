import socket as sk
import AlphaBot

#Address di connesione al robot
ADDRES = ("192.168.1.110", 3000) 

#Classe di implementazione controlli personalizzati
class Control():
    def __init__(self, left, right, robot):
        self.left = left
        self.right = right
        self.robot = robot
        
    def setSpeed(self,msg):
        if msg in speeds:
            self.left = speeds[msg]
            self.right = speeds[msg]

    def modularFw(self):
        self.robot.setMotor(self.left,-self.right)
        
    def modularBw(self):
        self.robot.setMotor(-self.left,self.right)

#Istanziamento classe   
Ab = AlphaBot.AlphaBot()
ctrl = Control(40, 40, Ab)
    
#dizionario di controllo del robot
#in base al carattere ricevuto viene chiamata la rispettiva funzione
movemnts = {
    "w": Ab.forward,
    "s": Ab.backward,
    "a": Ab.left,
    "d": Ab.right,
    "e": Ab.ex,
    " ": Ab.stop,
    "x": ctrl.modularFw,
    "c": ctrl.modularBw
}

#dizionario di controllo per le velocità
speeds = {
    "1": 33,
    "2": 70,
    "3": 100
}


def server_connect():
    server = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    server.bind(ADDRES)
    server.listen(1)
    conn, addr = server.accept()
    data = ""
    print("Connection from: ", addr)
    while True:
        data = conn.recv(1024).decode()
        print("Received from client: ", data)
        if data == "e":
            break
        ctrl.setSpeed(data)
        if data in movemnts:
            movemnts[data]()
        
    conn.close()
    
Ab.stop()
server_connect()    
