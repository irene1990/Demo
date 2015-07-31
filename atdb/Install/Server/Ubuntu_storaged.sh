#!/usr/bin/expect
set timeout 30
spawn dpkg -i /tmp/dbackup3-storaged.deb
expect "Please input DBackup3 Backup Server host"
send "192.168.82.40\r"
expect "Please input DBackup3 Backup Server port"
send "443\r"
expect "Does DBackup3 Backup Server enable SSL protocol?"
send "yes\r"
interact

