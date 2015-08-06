from ftplib import FTP
import CONFIG
class GetPackages():
	def __init__(self):
		self.ftp=FTP()
		self.ftp.connect(CONFIG.FTPIP)
		self.ftp.login(CONFIG.FUSER,CONFIG.FPASSWD)

	def getDown(self, listname):
		filename  =''.join(listname[-1])
		f = open(filename,"wb").write
		self.ftp.retrbinary("RETR %s"%filename, f, 8192)

	def getLastDEBServer(self):
		self.ftp.cwd(CONFIG.LASTEST_PATH)
		listname = self.ftp.nlst(CONFIG.DEB_SERVER)
		self.getDown(listname)

	def getLastDEBAgent(self):
		self.ftp.cwd(CONFIG.LASTEST_PATH)
		listname = self.ftp.nlst(CONFIG.DEB_AGENT)
		self.getDown(listname)

	def getLastRPMAgent(self):
		self.ftp.cwd(CONFIG.LASTEST_PATH)
		listname = self.ftp.nlst(CONFIG.RPM64_AGENT)
		self.getDown(listname)

	def getLastAIXAgent(self):
		self.ftp.cwd(CONFIG.LASTEST_PATH)
		listname = self.ftp.nlst(CONFIG.AIX_AGENT)
		self.getDown(listname)

	def getReleaseDEBServer(self):
		self.ftp.cwd(CONFIG.RELEASE_SERVER)
		listname = self.ftp.nlst(CONFIG.DEB_SERVER)
		self.getDown(listname)

	def getReleaseDEBAgent(self):
		self.ftp.cwd(CONFIG.RELEASE_AGENT)
		listname = self.ftp.nlst(CONFIG.DEB_AGENT)
		self.getDown(listname)

	def getReleaseRPMAgent(self):
		self.ftp.cwd(CONFIG.RELEASE_AGENT)
		listname = self.ftp.nlst(CONFIG.RPM64_AGENT)
		self.getDown(listname)

	def getReleaseAIXAgent(self):
		self.ftp.cwd(CONFIG.RELEASE_AGENT)
		listname = self.ftp.nlst(CONFIG.AIX_AGENT)
		self.getDown(listname)

	def getLastDEBServer3(self):
		filepath = CONFIG.LASTEST3_PATH + 'deb' + CONFIG.DBACKUP3_MID + 'x86_64/'
		self.ftp.cwd(filepath)
		dir1 = self.ftp.nlst('*')
		self.ftp.cwd(dir1[-1][18:-10])
		listname1 = self.ftp.nlst('*common*')
		listname2 = self.ftp.nlst('*backupd*')
		listname3 = self.ftp.nlst('*storaged*')
		self.getDown(listname1)
		self.getDown(listname2)
		self.getDown(listname3)

	def getLastRPMDBackup3(self):
		filepath = CONFIG.LASTEST3_PATH + 'rpm' + CONFIG.DBACKUP3_MID + 'x86_64/'
		self.ftp.cwd(filepath)
		dir1 = self.ftp.nlst('*')
		self.ftp.cwd(dir1[-1][18:-25])
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
		filepath = CONFIG.LASTEST3_PATH + 'rpm' + CONFIG.DBACKUP3_MID + 'mips64el/'
		self.ftp.cwd(filepath)
		dir1 = self.ftp.nlst('*')
		self.ftp.cwd(dir1[-1][18:-27])
		listname1 = self.ftp.nlst('*common*')
		listname2 = self.ftp.nlst('*libstdc*')
		listname3 = self.ftp.nlst('*agent-3.0*')
		listname4 = self.ftp.nlst('*agent*file*')
		self.getDown(listname1)
		self.getDown(listname2)
		self.getDown(listname3)
		self.getDown(listname4)

	def getLastPPCDBackup3(self):
		filepath = CONFIG.LASTEST3_PATH + 'rpm' + CONFIG.DBACKUP3_MID + 'ppc64/'
		self.ftp.cwd(filepath)
		dir1 = self.ftp.nlst('*')
		self.ftp.cwd(dir1[-1][18:-31])
		listname1 = self.ftp.nlst('*common*5.1*')
		listname2 = self.ftp.nlst('*libstdc*5.1*')
		listname3 = self.ftp.nlst('*agent-3.0*5.1*')
		listname4 = self.ftp.nlst('*agent*oracle*5.1*')
		listname5 = self.ftp.nlst('*agent*file*5.1*')
		self.getDown(listname1)
		self.getDown(listname2)
		self.getDown(listname3)
		self.getDown(listname4)
		self.getDown(listname5)

	def getReleaseDEBServer3(self):
		filepath = CONFIG.RELEASE_DBACKUP3 + 'x86_64/'
		self.ftp.cwd(filepath)
		listname1 = self.ftp.nlst('*common*')
		listname2 = self.ftp.nlst('*backupd*')
		listname3 = self.ftp.nlst('*storaged*')
		self.getDown(listname1)
		self.getDown(listname2)
		self.getDown(listname3)

	def getReleaseRPMDBackup3(self):
		filepath = CONFIG.RELEASE_DBACKUP3 + 'x86_64/'
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
		filepath = CONFIG.RELEASE_DBACKUP3 + 'mips64el/'
		self.ftp.cwd(filepath)
		listname2 = self.ftp.nlst('*libstdc*')
		listname3 = self.ftp.nlst('*agent-3.0*')
		listname4 = self.ftp.nlst('*agent*file*')
		self.getDown(listname1)
		self.getDown(listname2)
		self.getDown(listname3)
		self.getDown(listname4)


	def getReleasePPCDBackup3(self):
		filepath = CONFIG.RELEASE_DBACKUP3 + 'ppc64/'
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

if __name__ == '__main__':
    getpackages = GetPackages()
#    getpackages.getLastDEBServer()
#    getpackages.getLastDEBAgent()
#    getpackages.getLastRPMAgent()
#    getpackages.getLastAIXAgent()
#    getpackages.getReleaseDEBServer()
#    getpackages.getReleaseDEBAgent()
#    getpackages.getReleaseRPMAgent()
#    getpackages.getReleaseAIXAgent()
#    getpackages.getLastDEBServer3()
    getpackages.getLastRPMDBackup3()
#    getpackages.getLastPPCDBackup3()
#    getpackages.getReleaseDEBServer3()
#    getpackages.getReleaseRPMDBackup3()
#    getpackages.getReleasePPCDBackup3()
#    getpackages.getLastMIPS64DBackup3()
	
