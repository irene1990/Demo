#!/usr/bin/expect
set timeout 30
spawn dpkg -i /root/dbackup-server_5.1.16141-1.dev_amd64.deb
expect "Please enter the user name of MySQL:"
send "root\n"
expect "Please enter the password of MySQL:"
send "dingjia\n"
spawn dpkg -i /root/dbackup3-common_3.0.3609-1.5665265.dbg~precise_amd64.deb /root/dbackup3-backupd_3.0.3609-1.5665265.dbg~precise_amd64.deb
interact
