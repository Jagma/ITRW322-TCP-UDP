import socket
import time
import sys

UDP_IP = "192.168.1.102"
UDP_PORT = 50000
buf = 1024
#file_name = sys.argv[1]

class UDP:
    def __init__(self, IP, PORT):
        self.ip = IP
        self.port = PORT

    def sendUDP(self, file_name):
        t0 = time.time()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(file_name.encode(), (self.ip, self.port))
        print("Sending %s ..." % file_name)

        f = open(file_name, "r")
        data = f.read(buf)
        while(data):
            if(sock.sendto(data.encode(), (self.ip, self.port))):
                data = f.read(buf)
                time.sleep(0.001) # Give receiver a bit time to save

        sock.close()
        f.close()
        total = time.time() - t0
        with open("UDPSenderResults.txt", "a") as myfile:
            myfile.write(file_name +":"+str(total)+"\n")

sender = UDP(UDP_IP, UDP_PORT)
#sender.sendUDP("1MB.txt")
#sender.sendUDP("2MB.txt")
#sender.sendUDP("4MB.txt")
#sender.sendUDP("8MB.txt")
#sender.sendUDP("16MB.txt")
#sender.sendUDP("32MB.txt")
#sender.sendUDP("64MB.txt")
#sender.sendUDP("128MB.txt")
#sender.sendUDP("256MB.txt")
#sender.sendUDP("512MB.txt")
sender.sendUDP("1GB.txt")