import socket
import select
import time

UDP_IP = "127.0.0.1"
IN_PORT = 50000
timeout = 3


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    if data:
        print("File name:"), data
        file_name = data.strip()

    f = open(file_name, 'wb')
    t0 = time.time()
    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            data, addr = sock.recvfrom(1024)
            f.write(data)
        else:
            print("%s Finish!" % file_name)
            f.close()
            total = time.time() - t0
            with open("UDPReceiverResults.txt", "a") as myfile:
                myfile.write(str(file_name) +":"+str(total)+"\n")
            break