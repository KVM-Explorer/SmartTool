import yagmail


def send_mail(user, password, host, port, receiver, title, content):
    sender = yagmail.SMTP(user=user,
                          password=password,
                          host=host,
                          port=port
                          )
    sender.encoding = 'utf-8'
    sender.send(to=receiver,
                subject=title,
                contents=content)
