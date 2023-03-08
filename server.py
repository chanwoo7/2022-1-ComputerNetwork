from socket import *
import os
from datetime import datetime

serverName = "Python Local Server"
# serverIP = '192.168.45.45'
serverIP = '127.0.0.1'
serverVersion = "HTTP/1.1"
serverPort = 80

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))
serverSocket.listen()

print('The server is running!')

while True:
    connectionSocket, addr = serverSocket.accept()
    request_message = connectionSocket.recv(65535).decode()
    request_method = request_message.split()[0]
    request_url = request_message.split()[1]
    request_version = request_message.split()[2]
    request_body = request_message[request_message.rfind("\r\n\r\n")+4:]

    method_list = ["GET", "HEAD", "POST", "PUT"]
    connection_type = "Keep-Alive"
    content_type = "text/html"

    # GET Method
    if request_method == method_list[0] and request_version == serverVersion:
        try:
            filename = request_url.lstrip('/')

            f = open(filename, "r")
            file_data = f.read()
            content_length = len(file_data.encode('utf-8'))
            f.close()

            response_code = "200 OK"
            response_message = f"{request_version} {response_code}\r\n" \
                               f"Server: {serverName}\r\n" \
                               f"Date: {datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST')}\r\n" \
                               f"Connection: {connection_type}\r\n" \
                               f"Content-Type: {content_type}\r\n" \
                               f"Content-Length: {content_length}\r\n\r\n" \
                               f"{file_data}\r\n"
        except FileNotFoundError:
            response_code = "404 Not found"
            response_message = f"{request_version} {response_code}\r\n\r\n"

    # HEAD Method
    elif request_method == method_list[1] and request_version == serverVersion:
        try:
            filename = request_url.lstrip('/')

            f = open(filename, "r")
            file_data = f.read()
            content_length = len(file_data.encode('utf-8'))
            f.close()

            response_code = "200 OK"
            response_message = f"{request_version} {response_code}\r\n" \
                               f"Server: {serverName}\r\n" \
                               f"Date: {datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST')}\r\n" \
                               f"Connection: {connection_type}\r\n" \
                               f"Content-Type: {content_type}\r\n" \
                               f"Content-Length: {content_length}\r\n\r\n"
        except FileNotFoundError:
            response_code = "404 Not found"
            response_message = f"{request_version} {response_code}\r\n\r\n"

    # POST Method
    elif request_method == method_list[2] and request_version == serverVersion:
        try:
            filename = request_url.lstrip('/')
            isfile = os.path.isfile(filename)

            f = open(filename, "a")
            f.write(request_body)
            f.close()
            f = open(filename, "r")
            file_data = f.read()
            content_length = len(file_data.encode('utf-8'))
            f.close()

            response_code = "200 OK" if isfile else "201 Created"
            response_message = f"{request_version} {response_code}\r\n" \
                               f"Server: {serverName}\r\n" \
                               f"Date: {datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST')}\r\n" \
                               f"Connection: {connection_type}\r\n" \
                               f"Content-Type: {content_type}\r\n" \
                               f"Content-Length: {content_length}\r\n\r\n" \
                               f"{file_data}\r\n"
        except FileNotFoundError:
            response_code = "404 Not found"
            response_message = f"{request_version} {response_code}\r\n\r\n"

    # PUT Method
    elif request_method == method_list[3] and request_version == serverVersion:
        try:
            filename = request_url.lstrip('/')
            isfile = os.path.isfile(filename)

            f = open(filename, "w")
            f.write(request_body)
            f.close()
            f = open(filename, "r")
            file_data = f.read()
            content_length = len(file_data.encode('utf-8'))
            f.close()

            response_code = "200 OK" if isfile else "201 Created"
            response_message = f"{request_version} {response_code}\r\n" \
                               f"Server: {serverName}\r\n" \
                               f"Date: {datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST')}\r\n" \
                               f"Connection: {connection_type}\r\n" \
                               f"Content-Type: {content_type}\r\n" \
                               f"Content-Length: {content_length}\r\n\r\n" \
                               f"{file_data}\r\n"
        except FileNotFoundError:
            response_code = "404 Not Found"
            response_message = f"{request_version} {response_code}\r\n\r\n"

    elif request_version != serverVersion:
        response_code = "505 HTTP Version Not Supported"
        response_message = f"{request_version} {response_code}\r\n\r\n"

    elif request_method not in method_list:
        response_code = "405 Method Not Allowed"
        response_message = f"{request_version} {response_code}\r\n\r\n"

    else:
        response_code = "400 Bad Request"
        response_message = f"{request_version} {response_code}\r\n\r\n"

    connectionSocket.send(response_message.encode())
