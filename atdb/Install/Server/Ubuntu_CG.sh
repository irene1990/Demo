#!/bin/bash
sed -i "s#BACKUPD_PORT\s*=.*#BACKUPD_PORT=443#g" /etc/default/dbackup3-storaged
/etc/init.d/dbackup3-storaged restart
