from ftplib import FTP
ftp=FTP()
CONST_BUFFER_SIZE = 8192
ftp.connect('192.168.88.10')
ftp.login('scutech','dingjia')
ftp.cwd('/ftp_product_installer/wddps/2015/5.1/dev')
server = ftp.nlst('*server*amd*deb')
l = len(server)
lastest =''.join(server[l-1:l])
f = open(lastest,"wb").write
ftp.retrbinary("RETR %s"%lastest, f, CONST_BUFFER_SIZE)
