#!/usr/bin.env python3
# "foobar" | nc localhost 8001
import socket
HOST =""
PORT = 8001
BUFFER_SIZE=1024
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) AS s:
        s.setsockopt(SOCKET.SOL_SOCKET,
        socket.SO_REUSEADDR, 1)
        s.bind((HOST,PORT))
        s.listen(1)
        while True:
        conn, addr = s.accept()   
        
        print (conn ,addr) 
        #full_data = b""
        while True: 
            data = conn.recv(BUFFER_SIZE)
            if not data: break
            full_data+= data
        time.sleep(0.5)
        conn.sendall(full_data)
        conn.close

if__name__="__main__";
    main()
#q2. 1 time us no need to bind with the client. as a 
server you need to bind to the socket and listen.
#Q3: S.SETCOCKOPT REUSE THE ADDRESS
#q4 client id and the clients port
Q5:none

