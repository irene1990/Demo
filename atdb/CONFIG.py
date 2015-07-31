DBIP="192.168.82.40"
FTPIP="192.168.88.10"
FUSER="scutech"
FPASSWD="dingjia"
DUSER="dingjia"
DPASSWD="dingjia123"
YEAR = '2015'
VERSION = '5.1'
# lastest's type
#list parameters
DEB_SERVER = '*server*amd*deb'
DEB_AGENT = '*agent*all.deb'
EXE_AGENT = '*agent*exe'
RPM64_AGENT = '*agent*x86_64.rpm'
RPM32_AGENT = '*agent*i686.rpm'
AIX_AGENT = '*agent*dev.aix5.1.ppc.rpm'
DBACKUP3_MID = '/develop/debug/'
DEB_DBACKUP3 = 'deb'
EXE_DBACKUP3 = 'mingw'
RPM_DBACKUP3 = 'rpm'
RPM4_DBACKUP3 = 'x86_64'
RPM32_DBACKUP3 = 'i686'
PPC64_DBACKUP3 = 'ppc64'
##-----------------------------------------------------------------------
RELEASE_PATH = '/product_release/scutech/dbackup/' + VERSION + '/'
RELEASE_SERVER = RELEASE_PATH + 'dbackup_server/'
RELEASE_AGENT = RELEASE_PATH + 'dbackup_agent/'
RELEASE_DBACKUP3 = RELEASE_PATH + 'dbackup3/'
RELEASE_STANDBY_RPM = RELEASE_PATH + 'dbackup_standby/'
##-----------------------------------------------------------------------
LASTEST_PATH = '/ftp_product_installer/wddps/' + YEAR + '/' + VERSION + '/dev/'
LASTEST3_PATH = '/ftp_product_installer/dbackup3/'
##----------------------------------------------------------------------

