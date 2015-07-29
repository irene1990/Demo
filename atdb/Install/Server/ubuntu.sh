#!/usr/bin/expect
set timeout 30
spawn dpkg -i dbackup-server_5.1.16130-1.dev_amd64.deb
expect "Please enter the user name of MySQL:"
send "root\n"
expect "Please enter the password of MySQL:"
send "dingjia\n"
interact
