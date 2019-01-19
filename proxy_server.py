#!/usr/bin.env python3
# "foobar" | nc localhost 8001
import socket
import time
HOST =""
PORT = 8001
BUFFER_SIZE=1024
def main():
    google_addr = None
    addr_info = socket.getaddrinfo("www.google.com",80)
    for addr in addr_info:
    (family,socktype,proto,canonname, sockaddr)= addr
    if family == socket.AF_INET and socktype ==
    socket.SOCK_STREAM:
         google_addr = addr
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) AS s:
        s.setsockopt(SOCKET.SOL_SOCKET,
        socket.SO_REUSEADDR, 1)
        s.bind((HOST,PORT))
        s.listen(1)
        while True:
            conn, addr = s.accept()   
            print (addr)
       
            print (conn ,addr) 
            (family,socktype,proto,canonname, sockaddr)= 
            google_addr
            with socket.socket (family,socktype) as proxy_end:
            proxy_end.connect(sockaddr)
            send_full_data = b""
            while True: 
                data = conn.recv(BUFFER_SIZE)
                if not data: break
                send_full_data+= data
            time.sleep(0.5)
            proxy_end.sendall(send_full_data)
            proxy_end.shutdown(socket.SHUT__WR)
            
            while True: 
                data = cpnn.recv(BUFFER_SIZE)
                if not data: break
                conn.send(data)
      conn.clos (OR WHATEVER )
                

if__name__="__main__";
    main()
#q2. 1 time us no need to bind with the client. as a 
server you need to bind to the socket and listen.
#Q3: S.SETCOCKOPT REUSE THE ADDRESS
#q4 client id and the clients port
Q5:none

