import socket as sk
import msvcrt as mv
ADDRESS = ("192.168.1.110", 3000)
s= sk.socket(sk.AF_INET, sk.SOCK_STREAM)

s.connect(ADDRESS)

while True:
    msg = mv.getch()
    s.send(msg)
    print(msg.decode())
    if msg == b"e":
        break
s.close()

