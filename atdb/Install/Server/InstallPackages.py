#!/usr/bin/python
import pexpect
class InstallPackages():
	def __init__(self,serverIP,agentIP):
		self.serverIP = serverIP
		self.agentIP = agentIP

	def expect(self,cmd):
		child = pexpect.spawn(cmd)
		child.expect("(?i)password:")
		child.send("dingjia\r")
		child.wait()
		child.interact()

	def installDEBServer(self,version):
		cmd = 'ssh -l root ' + self.serverIP +' " dpkg -i /tmp/dbackup-server_' + version + '.dev_amd64.deb"'
		child = pexpect.spawn(cmd)
		child.expect("(?i)password:")
		child.send("dingjia\r")
		child.expect("Please enter the user name of MySQL:")
		child.send("root\r")
		child.expect("Please enter the password of MySQL:")
		child.send("dingjia\r")
		child.wait()
		child.interact()

	def installDEBCommon(self,version):
		cmd = 'ssh -l root ' + self.serverIP +' " dpkg -i /tmp/dbackup3-common_' + version + '_amd64.deb"'
		self.expect(cmd)

	def installDEBBackupd(self,version):
		cmd = 'ssh -l root ' + self.serverIP +' " dpkg -i /tmp/dbackup3-backupd_' + version + '_amd64.deb"'
		self.expect(cmd)

	def installDEBStoraged(self,version):
		cmd = 'ssh -l root ' + self.serverIP +' " dpkg -i /tmp/dbackup3-storaged_' + version + '_amd64.deb"'
		child = pexpect.spawn(cmd)
		child.expect("(?i)password:")
		child.send("dingjia\r")
		child.expect("Please input DBackup3 Backup Server host")
		child.send(self.serverIP +'\r')
		child.expect("Please input DBackup3 Backup Server port")
		child.send("443\r")
		child.expect("Does DBackup3 Backup Server enable SSL protocol?")
		child.send("yes\r")
		child.wait()
		child.interact()
		sed_cmd = 'ssh -l root ' + self.serverIP +' " sed -i "s#BACKUPD_PORT\s*=.*#BACKUPD_PORT=443#g" /etc/default/dbackup3-storaged'
		self.expect(sed_cmd)

	def installRPMDBackup(self,version):
		cmd = 'ssh -l root ' + self.agentIP + ' "rpm -ivh /tmp/dbackup-agent-' + version + '.dev.x86_64.rpm'
		self.expect(cmd)

	def installRPMDBackup3(self,version,module):
		cmd = 'ssh -l root ' + self.agentIP + ' "rpm -ivh '
		cmd0 = '/tmp/dbackup3-libstdc++6-' + version + '.dbg.x86_64.rpm /tmp/dbackup3-common-' + version + '.dbg.x86_64.rpm /tmp/dbackup3-agent-' + version + '.dbg.x86_64.rpm '
		cmd1 = '/tmp/dbackup3-agent-oracle-' + version + '.dbg.x86_64.rpm '
		cmd2 = '/tmp/dbackup3-agent-postgres-' + version + '.dbg.x86_64.rpm '
		cmd3 = '/tmp/dbackup3-agent-file-' + version + '.dbg.x86_64.rpm '
		if module == '0' :
			cmd += cmd0 + '"'
		elif module == '1' :
			cmd += cmd0 + cmd1 + '"'
		elif module == '2' :
			cmd += cmd0 + cmd2 + '"'
		elif module == '3' :
			cmd += cmd0 + cmd3 + '"'
		elif module == '12':
			cmd += cmd0 + cmd1 + cmd2 + '"'
		elif module == '13':
			cmd += cmd0 + cmd1 + cmd3 + '"'
		elif module == '23':
			cmd += cmd0 + cmd2 + cmd3 + '"'
		elif module == '123':
			cmd += cmd0 + cmd1 + cmd2 + cmd3 + '"'
		print cmd
		self.expect(cmd)

	def configRPMDBackup(self):
		cmd = 'ssh -l root ' + self.agentIP + ' /etc/init.d/dbackup_agentd config'
		print cmd
		child = pexpect.spawn(cmd)
		child.expect("(?i)password:")
		child.send("dingjia\r")
		child.expect('(?i)[oracle]:')
		child.send("oracle\r")
		child.expect('(?i)db_1]:')
		child.send("\r")
		child.expect('Use HTTPS or not? (y/N):')
		child.send("\r")
		child.expect('Please input DBackup Server\'s IP address:')
		child.send(self.serverIP+'\r')
		child.expect('Please input DBackup Server\'s service port[80]:')
		child.send("\r")
		child.expect('Select service type [0]:')
		child.send("\r")
		child.expect('Restart DBackup Agent to take effect now? (Y/n):')
		child.send("\r")
		child.wait()
		child.interact()

if __name__ == '__main__':
    installpackages = InstallPackages('192.168.82.33','192.168.82.40')
    #installpackages.installDEBServer('5.1.16192-1')
    #installpackages.installDEBCommon('' + version + '.dbg~precise')
    #installpackages.installDEBBackupd('' + version + '.dbg~precise')
    #installpackages.installDEBStoraged('' + version + '.dbg~precise')
    #installpackages.installRPMDBackup('5.1.14293-1')
    installpackages.configRPMDBackup()
    #installpackages.installRPMDBackup3('3.0.3686-1.ff2d841','1')