#!/usr/bin/expect
set timeout 30
spawn dpkg -i /tmp/dbackup-server.deb
expect "Please enter the user name of MySQL:"
send "root\n"
expect "Please enter the password of MySQL:"
send "dingjia\n"
interact
