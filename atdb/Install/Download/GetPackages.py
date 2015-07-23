import LANG
from ftplib import FTP
class GetPackages():
	def __init__(self):
		self.ftp=FTP()
		self.ftp.connect('192.168.88.10')
		self.ftp.login('scutech','dingjia')

	def getDown(self, listname):
		l = len(listname)
		filename  =''.join(listname[l-1:l])
		f = open(filename,"wb").write
		self.ftp.retrbinary("RETR %s"%filename, f, 8192)

	def getLastDEBServer(self):
		filepath = LANG.lastest1 + LANG.year + '/' + LANG.version + LANG.lastest2
		self.ftp.cwd(filepath)
		listname = self.ftp.nlst(LANG.server_deb)
		self.getDown(listname)

	def getLastDEBAgent(self):
		filepath = LANG.lastest1 + LANG.year + '/' + LANG.version + LANG.lastest2
		self.ftp.cwd(filepath)
		listname = self.ftp.nlst(LANG.agent_deb)
		self.getDown(listname)

	def getLastRPMAgent(self):
		filepath = LANG.lastest1 + LANG.year + '/' + LANG.version + LANG.lastest2
		self.ftp.cwd(filepath)
		listname = self.ftp.nlst(LANG.agent_rpm)
		self.getDown(listname)

	def getLastAIXAgent(self):
		filepath = LANG.lastest1 + LANG.year + '/' + LANG.version + LANG.lastest2
		self.ftp.cwd(filepath)
		listname = self.ftp.nlst(LANG.agent_aix)
		self.getDown(listname)

	def getReleaseDEBServer(self):
		filepath = LANG.release_server1 + LANG.version + LANG.release_server2
		self.ftp.cwd(filepath)
		listname = self.ftp.nlst(LANG.server_deb)
		self.getDown(listname)

	def getReleaseDEBAgent(self):
		filepath = LANG.release_server1 + LANG.version + LANG.release_server3
		self.ftp.cwd(filepath)
		listname = self.ftp.nlst(LANG.agent_deb)
		self.getDown(listname)

	def getReleaseRPMAgent(self):
		filepath = LANG.release_server1 + LANG.version + LANG.release_server3
		self.ftp.cwd(filepath)
		listname = self.ftp.nlst(LANG.agent_rpm)
		self.getDown(listname)

	def getReleaseAIXAgent(self):
		filepath = LANG.release_server1 + LANG.version + LANG.release_server3
		self.ftp.cwd(filepath)
		listname = self.ftp.nlst(LANG.agent_aix)
		self.getDown(listname)
