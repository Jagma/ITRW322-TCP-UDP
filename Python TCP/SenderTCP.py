import socket
import sys
import time

TCP_IP = "127.0.0.1"
FILE_PORT = 5005
DATA_PORT = 5006
buf = 1024
#file_name = sys.argv[1]

class TCP:
    def __init__(self, IP, FILE_PORT, DATA_PORT):
        self.ip = IP
        self.file_port = FILE_PORT
        self.data_port = DATA_PORT

    def sendTCP(self, file_name):
         try:
            t0 = time.time()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((TCP_IP, self.file_port))
            sock.send(file_name.encode())
            sock.close()

            print("Sending %s ..." % file_name)

            f = open(file_name, "rb")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((TCP_IP, self.data_port))
            data = f.read()
            sock.send(data)

         finally:
            sock.close()
            f.close()
            total = time.time() - t0
            with open("SenderResults.txt", "a") as myfile:
              myfile.write(file_name +":"+str(total)+"\n")

sender = TCP(TCP_IP, FILE_PORT, DATA_PORT) 
sender.sendTCP("1MB.txt")
sender.sendTCP("2MB.txt")
sender.sendTCP("4MB.txt")
sender.sendTCP("8MB.txt")
sender.sendTCP("16MB.txt")
sender.sendTCP("32MB.txt")
sender.sendTCP("64MB.txt")
sender.sendTCP("128MB.txt")
sender.sendTCP("256MB.txt")
sender.sendTCP("512MB.txt")
sender.sendTCP("1GB.txt")