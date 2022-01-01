#coding=utf-8
from socket import *
import codecs
import datetime
#解析请求报文的请求形象路径
def findPath(str):
    try:

        pathTemp=str.decode().split(' ')[1]
        pathTemp=pathTemp[1:]
        path=pathTemp.replace('/','//')
        
        if (path=="State") :
            return 2

        return path[0]+':'+path[1:]
    except:
        return 1   
#判断文件是否存在
def findFile(path):
    try:
        file=open(path)
        file.close()        
        return True
    except:
         return False
#读文件
def readFile(path):
    try:
        file=codecs.open(path,'r','utf-8')
        str=file.read()
        file.close()
    except:
        str= False 
    finally:
        return str
 #计算时间
def timeFormed(form):
    now = datetime.datetime.now()
    return now.strftime(form)
def time():
    week_day = {
    0 : 'Mon',
    1 : 'Tues',
    2 : 'Web',
    3 : 'Thur',
    4 : 'Fri',
    5 : 'San',
    6 : 'Sun'
    }
    day = datetime.datetime.now().weekday()
    week=week_day[day]#星期
    month_dict={
    0:'Jan',
    1:'Feb',
    2:'Mar',
    3:'Apr',
    4:'May',
    5:'Jun',
    6:'Jul',
    7:'Aug',
    8:'Sep',
    9:'Oct',
    10:'Nov',
    11:'Dec'   
        }
    now = datetime.datetime.now()
    month=month_dict[int(now.strftime('%m'))]#月份
    time=week+', '+timeFormed('%d')+' '+month+' '+timeFormed('%Y %H:%M:%S')
    return time
# print now
#请求成功后的响应报文头部    
def responseMessageHead(text):
    responseMessage='''HTTP/1.1 200 OK
Connection: keep-alive
Data: Thur, 22 Mar '''+time()+''' GMT
Server:PythonWebServer 1.0
Last-Modified: Thur, 22 Mar 2017 19:26:03 GMT
Content-Lenth: '''+ str(len(text.encode('utf-8'))) +'\nContent-Type:text/html\n\n'
    return responseMessage   

#=================================Main===================================
serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(6)
print('The server is ready to receive.')
while 1:
    connectionSocket,addr=serverSocket.accept()
    sentence=connectionSocket.recv(1024)#sentence是从客户端发送的请求报文
    path=findPath(sentence)
    
    if path==2:
        text="1,2,3,4,5".encode()
        connectionSocket.send(text)
    elif path==1:
        connectionSocket.send('404 Not Found'.encode())#被请求文档不在服务器上
        # connectionSocket.send('400 Bad Request')#该请求不能被服务器理解
        print('This quest the server can\'t understand')
    elif path != 2 and not findFile(path):
        connectionSocket.send('404 Not Found'.encode())#被请求文档不在服务器上
        print( 'Not found the file which the client want')
    else:
        text=readFile(path)
        reuestMessage=responseMessageHead(text)+text
        reuestMessage=reuestMessage.encode('utf-8')
        connectionSocket.send(reuestMessage)
    connectionSocket.close()
    print('The online client is as follows:')
    print('Client\'s IP is:',addr[0],',','client\'s port is',addr[1],'\n')
    print('The client\'s request message is as follows:')
    print(sentence)

