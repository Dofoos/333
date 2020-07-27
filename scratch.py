#
# local host port scanner
import socket

def pscan(port):
    try:
        s.connect((ip,port))
        return True

    except:
        return False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())

for x in range(1,100):
    if pscan(x):
        print('Port',x,'is open')