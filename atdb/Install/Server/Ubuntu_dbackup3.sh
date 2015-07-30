#!/bin/bash
count=2
while [[ $count > 0 ]]
do
    if [[ $count -eq 2 ]]
    then 
        count=`ps -ef |grep dpkg |wc -l`
        continue
        echo 'continue'
    else 
        dpkg -i dbackup3-common* dbackup3-backupd*
        echo 'install'
        break
    fi
done
