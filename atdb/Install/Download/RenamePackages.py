import subprocess
proc=subprocess.Popen('ls',shell=True,stdout=subprocess.PIPE)
out,err=proc.communicate()
print out
#packages means all packagestall packages
#packages = out.split('\n')
#while i < len(packages)-1:
#    tmp = packages[i].split(' ')
#pname means package's name
#    pname = tmp[2]
#    uorder = 'dpkg -P ' + pname
#    uninstall = subprocess.call(uorder,shell=True)
#    print uorder
#    i +=1
#rmorder = 'rm -rf /etc/opt/scutech /opt/scutech/ /var/opt/scutech/ /var/log/dbackup3/ /var/lib/dbackup3/ /var/preserve/scutech/'
#print rmorder
#rm = subprocess.call(rmorder,shell=True)
