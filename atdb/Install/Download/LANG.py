year = '2015'
version = '5.1'
# lastest's type
#list parameters
deb_server = '*server*amd*deb'
deb_agent = '*agent*all.deb'
exe_agent = '*agent*exe'
rpm64_agent = '*agent*x86_64.rpm'
rpm32_agent = '*agent*i686.rpm'
aix_agent = '*agent*dev.aix5.1.ppc.rpm'
dbackup3_mid = '/develop/debug/'
deb_dbackup3 = 'deb'
exe_dbackup3 = 'mingw'
rpm_dbackup3 = 'rpm'
rpm64_dbackup3 = 'x86_64'
rpm32_dbackup3 = 'i686'
ppc64_dbackup3 = 'ppc64'
##-----------------------------------------------------------------------
release_path = '/product_release/scutech/dbackup/' + version + '/'
release_server = release_path + 'dbackup_server/'
release_agent = release_path + 'dbackup_agent/'
release_dbackup3 = release_path + 'dbackup3/'
release_standby_rpm = release_path + 'dbackup_standby/'
##-----------------------------------------------------------------------
lastest_path = '/ftp_product_installer/wddps/' + year + '/' + version + '/dev/'
lastest3_path = '/ftp_product_installer/dbackup3/'
##----------------------------------------------------------------------


