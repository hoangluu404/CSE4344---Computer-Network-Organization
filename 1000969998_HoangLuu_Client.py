# Hoang Luu
# 1000969998

import sys
import socket
import time

MESSAGE_LENGTH = 1024
FORMAT = 'utf-8'


# send requested filename to Server
def send_request_file(filename, client):

    filename = '/' + filename
    request = 'GET ' + filename + ' HTTP/1.1'
    print(f'sending request: {request}')
    timing = time.time()
    client.send(request.encode(FORMAT))
    return timing


# main function of Client
def main():

    if(len(sys.argv) == 1 ):        
        # if user do not enter Server IP and Port number
        SERVER_IP = socket.gethostbyname('localhost')
        PORT = 8080
        filename = 'index.html'
        print('no input from user')
        print(f'using default values: ip = {SERVER_IP}; port = {PORT}; filename = {filename}')
        
    elif(len(sys.argv) == 2):
        # if user enter only Server IP, but not Port number
        SERVER_IP = sys.argv[1]
        PORT = 8080
        filename = 'index.html'
        print(f'user entered: ip = {SERVER_IP}')
        print(f'using default values: port = {PORT}; filename = {filename}')

    elif(len(sys.argv) == 3):
        # if user entered both Server IP and Port number
        SERVER_IP = sys.argv[1]
        PORT = int(sys.argv[2])
        filename = 'index.html'
        print(f'user entered: p = {SERVER_IP}; port = {PORT} filename = {filename}')

    else:
        # if user entered all needed info
        SERVER_IP = sys.argv[1]
        PORT = int(sys.argv[2])
        filename = sys.argv[3]
        print(f'user entered: p = {SERVER_IP}; port = {PORT}; filename = {filename}')

    ADDRESS = (SERVER_IP, PORT)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to Server
    client.connect(ADDRESS)
    print('')
    print('server info')
    print(client) 

    # start timer for RTT
    start_time = send_request_file(filename,client)
    
    while(True):
        response = client.recv(MESSAGE_LENGTH).decode(FORMAT)
        if (len(response) == 0):
            break
        print (response)

    # stop timer for RTT
    end_time = time.time()
    RTT = end_time - start_time
    print(f'RTT is {RTT} seconds')

    # close connection with Server
    client.close()


# run main function
if __name__ == "__main__":
    main()