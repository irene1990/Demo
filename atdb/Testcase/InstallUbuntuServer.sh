#!/usr/bin/expect
set timeout 30
set target_ip [lindex $argv 0]
set username [lindex $argv 1]
set password [lindex $argv 2]
#set target_ip "192.168.82.40"
#set username "root"
#set password "dingjia"
spawn sh -c " scp ../Install/Server/* $username@$target_ip:/tmp"
expect "$username@$target_ip's $password:"
send "$password\n"
#spawn sleep 10
interact
spawn ssh -l root $target_ip "python /tmp/try.py"
expect "$username@$target_ip's $password:"
send "$password\n"
#spawn sleep 10
interact
spawn ssh -l root $target_ip "/tmp/Ubuntu_RN.sh"
expect "$username@$target_ip's $password:"
send "$password\n"
interact
spawn ssh -l root $target_ip "/tmp/Ubuntu_server.sh"
expect "$username@$target_ip's $password:"
send "$password\n"
#spawn sleep 60
interact
spawn ssh -l root $target_ip "/tmp/Ubuntu_dbackup3.sh"
expect "$username@$target_ip's $password:"
send "$password\n"
interact
spawn ssh -l root $target_ip "/tmp/Ubuntu_storaged.sh"
expect "$username@$target_ip's $password:"
send "$password\n"
interact
spawn ssh -l root $target_ip "/tmp/Ubuntu_CG.sh"
expect "$username@$target_ip's $password:"
send "$password\n"
interact
