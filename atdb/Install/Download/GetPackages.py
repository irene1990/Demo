import LANG
from ftplib import FTP
class GetPackages():
	def __init__(self):
		self.ftp=FTP()
		self.ftp.connect('192.168.88.10')
		self.ftp.login('scutech','dingjia')

	def getDown(self, listname):
		filename  =''.join(listname[-1])
		f = open(filename,"wb").write
		self.ftp.retrbinary("RETR %s"%filename, f, 8192)

	def getLastDEBServer(self):
		self.ftp.cwd(LANG.lastest_path)
		listname = self.ftp.nlst(LANG.deb_server)
		self.getDown(listname)

	def getLastDEBAgent(self):
		self.ftp.cwd(LANG.lastest_path)
		listname = self.ftp.nlst(LANG.deb_agent)
		self.getDown(listname)

	def getLastRPMAgent(self):
		self.ftp.cwd(LANG.lastest_path)
		listname = self.ftp.nlst(LANG.rpm64_agent)
		self.getDown(listname)

	def getLastAIXAgent(self):
		self.ftp.cwd(LANG.lastest_path)
		listname = self.ftp.nlst(LANG.aix_agent)
		self.getDown(listname)

	def getReleaseDEBServer(self):
		self.ftp.cwd(LANG.release_server)
		listname = self.ftp.nlst(LANG.deb_server)
		self.getDown(listname)

	def getReleaseDEBAgent(self):
		self.ftp.cwd(LANG.release_agent)
		listname = self.ftp.nlst(LANG.deb_agent)
		self.getDown(listname)

	def getReleaseRPMAgent(self):
		self.ftp.cwd(LANG.release_agent)
		listname = self.ftp.nlst(LANG.rpm64_agent)
		self.getDown(listname)

	def getReleaseAIXAgent(self):
		self.ftp.cwd(LANG.release_agent)
		listname = self.ftp.nlst(LANG.aix_agent)
		self.getDown(listname)

	def getLastDEBServer3(self):
		filepath = LANG.lastest3_path + 'deb' + LANG.dbackup3_mid + 'x86_64'
		self.ftp.cwd(filepath)
		dir1 = self.ftp.nlst('*')
		self.ftp.cwd(dir1[-1][18:-10])
		listname1 = self.ftp.nlst('*common*')
		listname2 = self.ftp.nlst('*backupd*')
#		listname3 = self.ftp.nlst('*storaged*')
		self.getDown(listname1)
		self.getDown(listname2)
#		self.getDown(listname3)

	def getLastRPMDBackup3(self):
		filepath = LANG.lastest3_path + 'rpm' + LANG.dbackup3_mid + 'x86_64'
		self.ftp.cwd(filepath)
		dir1 = self.ftp.nlst('*')
		self.ftp.cwd(dir1[-1][18:-17])
		listname1 = self.ftp.nlst('*common*')
		listname2 = self.ftp.nlst('*libstdc*')
		listname3 = self.ftp.nlst('*agent-3.0*')
		listname4 = self.ftp.nlst('*agent*oracle*')
		listname5 = self.ftp.nlst('*agent*postgres*')
		listname6 = self.ftp.nlst('*agent*file*')
		self.getDown(listname1)
		self.getDown(listname2)
		self.getDown(listname3)
		self.getDown(listname4)
		self.getDown(listname5)
		self.getDown(listname6)

        def getLastMIPS64DBackup3(self):
                filepath = LANG.lastest3_path + 'rpm' + LANG.dbackup3_mid + 'mips64el'
                self.ftp.cwd(filepath)
                dir1 = self.ftp.nlst('*')
                self.ftp.cwd(dir1[-1][18:-19])
                listname1 = self.ftp.nlst('*common*')
                listname2 = self.ftp.nlst('*libstdc*')
                listname3 = self.ftp.nlst('*agent-3.0*')
                listname4 = self.ftp.nlst('*agent*file*')
                self.getDown(listname1)
                self.getDown(listname2)
                self.getDown(listname3)
                self.getDown(listname4)

	def getLastPPCDBackup3(self):
		filepath = LANG.lastest3_path + 'rpm' + LANG.dbackup3_mid + 'ppc64'
		print filepath
		self.ftp.cwd(filepath)
		dir1 = self.ftp.nlst('*')
		self.ftp.cwd(dir1[-1][18:-23])
		listname1 = self.ftp.nlst('*common*')
		listname2 = self.ftp.nlst('*libstdc*')
		listname3 = self.ftp.nlst('*agent-3.0*')
		listname4 = self.ftp.nlst('*agent*oracle*')
		listname5 = self.ftp.nlst('*agent*file*')
		self.getDown(listname1)
		self.getDown(listname2)
		self.getDown(listname3)
		self.getDown(listname4)
		self.getDown(listname5)

	def getReleaseDEBServer3(self):
		filepath = LANG.release_dbackup3 + 'x86_64'
		self.ftp.cwd(filepath)
		listname1 = self.ftp.nlst('*common*')
		listname2 = self.ftp.nlst('*backupd*')
		listname3 = self.ftp.nlst('*storaged*')
		self.getDown(listname1)
		self.getDown(listname2)
		self.getDown(listname3)

	def getReleaseRPMDBackup3(self):
		filepath = LANG.release_dbackup3 + 'x86_64'
		self.ftp.cwd(filepath)
		listname1 = self.ftp.nlst('*common*')
		listname2 = self.ftp.nlst('*libstdc*')
		listname3 = self.ftp.nlst('*agent-3.0*')
		listname4 = self.ftp.nlst('*agent*oracle*')
		listname5 = self.ftp.nlst('*agent*postgres*')
		listname6 = self.ftp.nlst('*agent*file*')
		self.getDown(listname1)
		self.getDown(listname2)
		self.getDown(listname3)
		self.getDown(listname4)
		self.getDown(listname5)
		self.getDown(listname6)

        def getReleaseiMIPS64DBackup3(self):
                filepath = LANG.release_dbackup3 + 'mips64el'
                self.ftp.cwd(filepath)
                listname1 = self.ftp.nlst('*common*')
                listname2 = self.ftp.nlst('*libstdc*')
                listname3 = self.ftp.nlst('*agent-3.0*')
                listname4 = self.ftp.nlst('*agent*file*')
                self.getDown(listname1)
                self.getDown(listname2)
                self.getDown(listname3)
                self.getDown(listname4)


	def getReleasePPCDBackup3(self):
		filepath = LANG.release_dbackup3 + 'ppc64'
		self.ftp.cwd(filepath)
		listname1 = self.ftp.nlst('*common*')
		listname2 = self.ftp.nlst('*libstdc*')
		listname3 = self.ftp.nlst('*agent-3.0*')
		listname4 = self.ftp.nlst('*agent*oracle*')
		listname5 = self.ftp.nlst('*agent*file*')
		self.getDown(listname1)
		self.getDown(listname2)
		self.getDown(listname3)
		self.getDown(listname4)
		self.getDown(listname5)
