#!/usr/bin/expect
set timeout 30
spawn scp Download/GetPackages.py Download/LANG.py Download/try.py Server/Ubuntu_dbackup3.sh  Server/Ubuntu_server.sh Server/Ubuntu_RN.sh Server/Ubuntu_storaged.sh Server/Ubuntu_CG.sh ../Uninstall/Server/UninstallDEB.py root@192.168.82.40:/root
expect "root@192.168.82.40's password:"
send "dingjia\n"
spawn sleep 10
interact
spawn ssh -l root 192.168.82.40 "python /root/try.py"
expect "root@192.168.82.40's password:"
send "dingjia\n"
spawn sleep 10
interact
spawn ssh -l root 192.168.82.40 "/root/Ubuntu_RN.sh"
expect "root@192.168.82.40's password:"
send "dingjia\n"
interact
spawn ssh -l root 192.168.82.40 "/root/Ubuntu_server.sh"
expect "root@192.168.82.40's password:"
send "dingjia\n"
interact
spawn ssh -l root 192.168.82.40 "/root/Ubuntu_dbackup3.sh"
expect "root@192.168.82.40's password:"
send "dingjia\n"
interact
spawn ssh -l root 192.168.82.40 "/root/Ubuntu_storaged.sh"
expect "root@192.168.82.40's password:"
send "dingjia\n"
interact
spawn ssh -l root 192.168.82.40 "/root/Ubuntu_CG.sh"
expect "root@192.168.82.40's password:"
send "dingjia\n"
interact