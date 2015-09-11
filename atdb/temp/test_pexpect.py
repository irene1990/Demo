#!/usr/bin/python
import pexpect
child=pexpect.spawn('/usr/bin/scp',['/home/irene/odbc.txt','root@192.168.82.40:/root/odbc.txt'])
child.expect('(?i)password:')
child.sendline('dingjia')
child.wait()
child.interact()
child.close()
