import platform,time,os
from ftplib import FTP
os = platform.platform()
class Install():
	def __init__(self):
		self.ftp=FTP()
		self.ftp.connect(CONFIG.FTPIP)
		self.ftp.login(CONFIG.FUSER,CONFIG.FPASSWD)
		self.isLinux = os.find('Linux')
		self.isWindows = os.find('Windows')
		self.isUbuntu = os.find('Ubuntu')
		self.isRedHat = os.find('redhat')
		self.isCentOS = os.find('centos')
		self.is64 = os.find('x86_64')
		self.is32 = os.find('i686')
		self.dbackup = '/ftp_product_installer/wddps/2015/5.1/dev/'
		self.dbackup3=''
	def downloads(self, listname):
		filename  =''.join(listname[-1])
		f = open(filename,"wb").write
		self.ftp.retrbinary("RETR %s"%filename, f, 8192)
	def install(self):
		if self.isLinux > -1:
			if self.isUbuntu > -1:
				self.ftp.cwd(self.dbackup)
				listname = self.ftp.nlst(*server*amd*deb)
				if self.is64 > -1:
					self.dbackup3 = '/ftp_product_installer/self.dbackup3/deb/develop/debug/x86_64/'
				else:
					print ('Ubuntu32')
			elif self.isRedHat > -1 or self.isCentOS > -1:
				if self.is64 > -1:
					self.dbackup3 = '/ftp_product_installer/self.dbackup3/rpm/develop/debug/x86_64/'
				else:
					self.dbackup3 = '/ftp_product_installer/self.dbackup3/rpm/develop/debug/i686/'
		else:
			self.dbackup3 = '/ftp_product_installer/self.dbackup3/mingw/develop/debug/'
		print self.dbackup
		print self.dbackup3
#82.64  'Linux-2.6.32-0.18.ns6.mips64el-mips64el-with-glibc2.0'
#82.65  'Linux-3.10.0+-mips64-with-glibc2.0'
#82.62  'Linux-2.6.32-0.16.ns6.mips64el-mips64el-with-redhat-6.0-Santiago'
#82.67  'Linux-2.6.32.20-16.20.201403.ky3.sparcv9-sparc64-with-redhat-4.0-GreatWall'