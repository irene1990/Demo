#!/usr/bin/expect
set timeout 30
spawn sh -c "scp *.py root@192.168.82.40:/tmp"
expect "root@192.168.82.40's password:"
send "dingjia\n"
interact
