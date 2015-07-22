from ftplib import FTP
ftp=FTP()
ftp.connect('192.168.88.10')
ftp.login('scutech','dingjia')
ftp.cwd('/ftp_product_installer/wddps/2015/5.1/dev')
server = ftp.nlst('*server*amd*deb')
l = len(server)
print server[l-1:l]
