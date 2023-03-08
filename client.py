from socket import *

# serverIP = '192.168.45.45'
serverIP = '127.0.0.1'
serverPort = 80

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))

# request message example
request_message1 = "GET /index.html HTTP/1.1\r\n" \
                   "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\n" \
                   "Connection: Keep-Alive\r\n\r\n"

request_message2 = "GET /non-exist.html HTTP/1.1\r\n" \
                   "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\n" \
                   "Connection: Keep-Alive\r\n\r\n"

request_message3 = "HEAD /index.html HTTP/1.1\r\n" \
                   "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\n" \
                   "Connection: Keep-Alive\r\n\r\n"

request_message4 = "HEAD /non-exist.html HTTP/1.1\r\n" \
                   "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\n" \
                   "Connection: Keep-Alive\r\n\r\n"

request_message5 = "POST /new.html HTTP/1.1\r\n" \
                   "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\n" \
                   "Connection: Keep-Alive\r\n\r\n" \
                   "<p>Apple</p>\r\n"

request_message6 = "POST /new.html HTTP/1.1\r\n" \
                   "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\n" \
                   "Connection: Keep-Alive\r\n\r\n" \
                   "<p>Bear</p>\r\n"

request_message7 = "PUT /new-1.html HTTP/1.1\r\n" \
                   "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\n" \
                   "Connection: Keep-Alive\r\n\r\n" \
                   "<p>Python</p>\r\n" \
                   "<p>Java</p>\r\n" \
                   "<p>C++</p>\r\n"

request_message8 = "PUT /new-1.html HTTP/1.1\r\n" \
                   "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\n" \
                   "Connection: Keep-Alive\r\n\r\n" \
                   "<p>Strawberry</p>\r\n" \
                   "<p>Grape</p>\r\n"

request_message9 = "ABC /index.html HTTP/1.1\r\n" \
                   "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\n" \
                   "Connection: Keep-Alive\r\n\r\n"

request_message10 = "GET /index.html HTTP/2.0\r\n" \
                   "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\n" \
                   "Connection: Keep-Alive\r\n\r\n"

# 폴더 내에 server.py, client.py, index.html 3개의 파일만 존재하는 초기 상태에서 아래의 코드들을 순차적으로 실행 시,
# 결과는 각 줄의 주석과 같을 것이다.
clientSocket.send(request_message1.encode())  # get /index.html --> 200 OK
# clientSocket.send(request_message2.encode())  # get /non-exist.html --> 404 Not Found
# clientSocket.send(request_message3.encode())  # head /index.html --> 200 OK
# clientSocket.send(request_message4.encode())  # head /non-exist.html --> 404 Not Found
# clientSocket.send(request_message5.encode())  # post /new.html --> 201 Created
# clientSocket.send(request_message6.encode())  # post /new.html --> 200 OK
# clientSocket.send(request_message7.encode())  # put /new-1.html --> 201 Created
# clientSocket.send(request_message8.encode())  # put /new-1.html --> 200 OK
# clientSocket.send(request_message9.encode())  # --> 405 Method Not Allowed
# clientSocket.send(request_message10.encode())  # --> 505 HTTP Version Not Supported

receive_message = clientSocket.recv(65535).decode()
print(receive_message)
clientSocket.close()
