import pexpect
#child = pexpect.spawn('ssh -l root 192.168.82.40 " dpkg -i /tmp/dbackup-server_5.1.16190-1.dev_amd64.deb"')
#child.expect("root@192.168.82.40's password:")
#child.send("dingjia\n")
#child.expect("Please enter the user name of MySQL:")
#child.send("root\n")
#child.expect("Please enter the password of MySQL:")
#child.send("dingjia\n")
child = pexpect.spawn('ssh root@192.168.82.40')
child.expect("(?i)password:")
child.send("dingjia\n")