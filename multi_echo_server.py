#!/usr/bin.env python3
# "foobar" | nc localhost 8001
import socket
import Time
from multiprocessing import Process
HOST =""
PORT = 8001
BUFFER_SIZE=1024
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) AS s:
        s.setsockopt(SOCKET.SOL_SOCKET,
        socket.SO_REUSEADDR, 1)
        s.bind((HOST,PORT))
        s.listen(2)
        while True:
            conn, addr = s.accept() 
            p = Process(target = handle_echo, args = (addr,conn)
            p.daemon = True
            p.start()
            print ("process happeig is s", n)
       
def handle_echo(addr,conn)
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