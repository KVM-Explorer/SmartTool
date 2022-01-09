#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <netdb.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <stdbool.h>
#include <linux/tcp.h>
#include <unistd.h>
#include <arpa/inet.h>
#define SMTPSERVPORT 25
#define MAXDATASIZE 4096
#define TRUE 1

int main(int argc, char *argv[])
{
    printf("Start Program:");
    int sockfd;
    struct hostent *host;
    struct sockaddr_in serv_addr;
    struct in_addr ip_address_binary;
    char *SMTPMessage[] = { 
    "helo kvm\r\n",
//==============================
// Update Sender And Receiver Email
//==============================
    "mail from : <kvm@mylinux.com>\r\n",
    "rcpt to : <test2@mylinux.com>\r\n", 
    "data\r\n", 
    "Class: CS1903 Number:1907010308 By Program\r\n.\r\n", 
    "QUIT\r\n",
            NULL };
    int iLength = 0;
    int iMsg = 0;
    char buf[MAXDATASIZE];
    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) == -1)
    {
        perror("socket error ");
        exit(1);
    }
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(SMTPSERVPORT);
//==============================
// Update IP Address
//==============================

    serv_addr.sin_addr.s_addr = inet_addr("172.24.89.254");
    bzero(&(serv_addr.sin_zero), 8);
    /*置指针变量(&(serv_addr.sin_zero)中前8 个变量的值为零*/
    if (connect(sockfd, (struct sockaddr *)&serv_addr, sizeof(struct sockaddr)) == -1)
    {
        perror("connect error ");
        exit(1);

    }
    iLength = recv(sockfd, buf, sizeof(buf), 0);
    buf[iLength] ='\0';
    printf("received: %s\n", buf);
    //依次发送SMPT 命令，发送邮件
    do
    {
        bool bNodelay = TRUE; /*bool 型变量只有两个值：false 和true，是0 和1 的区别*/
        setsockopt(sockfd, IPPROTO_TCP, TCP_NODELAY,
                   (const char *)&bNodelay, sizeof(bool));
        send(sockfd, SMTPMessage[iMsg], strlen(SMTPMessage[iMsg]), 0);
        printf("have sent: %s", SMTPMessage[iMsg]);
        iLength = recv(sockfd, buf, sizeof(buf), 0);
        buf[iLength] ='\0';
        iMsg++;
        printf("received: %s, %d\n", buf, iMsg);
    } while (SMTPMessage[iMsg]);
    close(sockfd);
}
