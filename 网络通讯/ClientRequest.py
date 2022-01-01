#coding=utf-8
from socket import *
serverName='127.0.0.1'
serverPort=12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
content=r"/E/test.html"

def AddContentToMessage(str):
    return '''GET '''+str+''' HTTP/1.1
Host: 127.0.0.1
Connection: keep-alive
Accept: text/html
User-Agent: Mozilla/5.0
Accept-Encoding: gzip, deflate
Accept-Language: zh-cn,en-us'''

content = r"\State"
requestMessage=AddContentToMessage(content)

requestMessage=requestMessage.encode('utf-8')
clientSocket.send(requestMessage)
modifiedSentence=clientSocket.recv(1024)
print('From Server:')
print(modifiedSentence.decode())
clientSocket.close()
