import ftplib


class FtpClass:
    def __init__(self, host, user, password, port):
        self.ftp = ftplib.FTP(host=host, user=user, password=password)
        self.ftp.connect(host, port=port)
        self.ftp.login(user=user, password=password)
        self.ftp.nlst()
