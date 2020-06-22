# Hoang Luu
# 1000969998

import sys
import socket
import threading

MESSAGE_LENGTH = 1024
FORMAT = 'utf-8'


# open the file and return its data
def open_file(filename, file_extension):
    try:
        # if file exists
        if file_extension == '':
            file_extension == 'html'
        if(file_extension == 'jpg' or file_extension == 'jpeg' or file_extension == 'png' or file_extension == 'gif'):
            f = open(filename, 'rb')
            data = f.read()
            print(f'IMAGE ==== {data}')
            f.close()
            return data
        f = open(filename, 'r')
        data = f.read()
        f.close()       
        return data

    except IOError:
        # if file does not exist
        print('file does not exists')
        return False


# format the response and return the data
def header_format_response(filename, file_extension, protocol):

    # open the file
    data = open_file(filename, file_extension)
    print(data)
    if(data):
        # if file exists
        #connection.send(b'HTTP/1.0 200 OK\r\nContent-Length: 11\r\nContent-Type: text/html; charset=UTF-8\r\n\r\nHello World sdfasfasfs\r\n')
        return protocol + ' 200 OK'
   
    else:
        # if file does not exist
        return protocol + ' 404 Not Found'


# whenever new client connects
def new_client(connection, address):
    print('')
    print('------new connection------')
    print(f'[{address}] connected!')
            
    message = connection.recv(MESSAGE_LENGTH).decode(FORMAT)
    if message:
        # if message request is not empty

        # split the strings into segments
        temp = message.split()
        #action = temp[0]
        filename = temp[1]
        filename = filename[1:]
        protocol = temp[2]

        # if no file is entered, return index page
        if filename == '':
            filename = 'index.html'
                
        file_extension = filename.split('.')
        if(len(file_extension) > 1):
            file_extension = file_extension[1]

        # print out the request from the client
        print(f'[{address}] requested: {temp}')

        # get header
        header = header_format_response(filename,file_extension, protocol)

        # open the file
        data = open_file(filename, file_extension)
        content = data
        if(data == False):
            # bad request handler
            content = open_file('bad_request.html', 'html')

        # pieces of the response
        body = str(content) # body
        if(file_extension == 'jpg' or file_extension == 'jpeg' or file_extension == 'png' or file_extension == 'gif'):
            body = content
        header = str(header) # header
        response1 = str('\r\nContent-Length: ')
        length = str(len(body)) # length of the body response
        response2 = str('\r\nContent-Type: ')
    
        # file type handler
        if(file_extension == 'html' and data != False):
            file_type = 'text/html'
        elif((file_extension == 'jpg' or file_extension == 'jpeg') and data != False):
            file_type = 'image/jpeg'
        elif(file_extension == 'png' and data != False):
            file_type = 'image/png'
        elif(file_extension == 'gif' and data != False):
            file_type = 'image/gif'
        elif(file_extension == 'txt' and data != False):
            file_type = 'text/txt'
        elif(file_extension == 'py'):
            file_type = 'text/txt'
        else:
            file_type = 'text/html'

        file_type = str(file_type)
        response3 = str('; charset=UTF-8\r\n\r\n')
        response4 = str('\r\n')
        
        # concatenate header and body into one response message for print out
        response = header + response1 + length + response2 + file_type + response3
    
        # send response to client
        connection.send(str.encode(header))
        connection.send(str.encode(response1 + length))
        connection.send(str.encode(response2 + file_type))
        connection.send(str.encode(response3))

        # image/text handling
        if((file_extension == 'jpg' or file_extension == 'jpeg' or file_extension == 'png' or file_extension == 'gif') and data != False):
            # image handling
            response += str(body)
            connection.send((body))
        else:
            # file handling
            response += body
            connection.send(str.encode(body))

        response += response4
        connection.send(str.encode(response4))
        print('\nresponse:\n')
        print(response)

    # close connection
    connection.close()
    print(f'[{address}] connection closed!')
    
            
# initiate Server
def start(server):
    
    server.listen(5)
    print(f'server established {server}')
    
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=new_client, args=(connection,address))
        thread.start()


# main function
def main():

    # Assign a port number
    HOST = 'localhost' # default host
    # I tried using socket.gethostbyname(socket.gethostname())
    # But it does not work on Mac OS for some reason
    
    PORT = 8080 # default port number

    # replace port number if user enter
    if(len(sys.argv)>1):
        PORT = int(sys.argv[1])

    ADDRESS = (HOST,PORT)

    # Create a TCP server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

    # Bind the socket to server address and server port
    server.bind(ADDRESS)

    # Start the server
    start(server)


# run main function of the Server
if __name__ == "__main__":
    main()