from ftplib import FTP
ftp=FTP()
ftp.connect('192.168.88.10')
ftp.login('scutech','dingjia')
ftp.cwd('/ftp_product_installer/wddps/2015/5.1/dev')
