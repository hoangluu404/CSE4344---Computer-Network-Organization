Hoang Luu
1000969998

COMPILE AND RUN

    to compile and run with default value
    for Server: default port = 8080
        make server
    for Client: default port = 8080; IP = localhost
        make client
    for Browser:
        localhost:8080/

    to complie and run with other values
    for Server:
        python3 1000969998_HoangLuu_Server.py <port number>
    for Client:
        python3 1000969998_HoangLuu_Client.py <host IP> <port number> <filename>
    for Browsers:
        <host IP>:<port number>/<filename>

included files:

    Makefile
    readme.txt
    1000969998_HoangLuu_Server.py (Server)
    1000969998_HoangLuu_Client.py (Client)
    index.html
    about.html
    bad_request.html
    text.txt
    bear.gif
    leona.jpg

Using Python 3.7.7 and VS Code inside MAC OS

These libraries were used to complete the project
    import sys: to get the command line argument input from user
    import socket: to create and maintain TCP connection via socket
    import threading: to allow multi-threading Server
    import time: to calculate RTT