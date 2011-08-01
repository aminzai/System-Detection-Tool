import platform
import os

from SystemInfoBase import SystemInfoBase
from Constant import *

class LinuxSysInfoBase(SystemInfoBase):
    def __init__(self):
        if not self.getDistName():
            if os.path.exists('/etc/arch-release'):
                from ArchlinuxSysInfo import ArchlinuxSysInfo
                self.__class__ = ArchlinuxSysInfo
                self.__init__()
            elif os.path.exists('/usr/bin/pkg') and \
                    commands.getoutput('cat /etc/release | grep "OpenSolaris"'):
                # DIST_OPENSOLARIS
                pass
            else:
                # DIST not found
                pass
        elif self.getDistName() in DIST_DEB_BASE :
            from DebianBaseSysInfo import DebianBaseSysInfo
            self.__class__ = DebianBaseSysInfo
            self.__init__()
        """
        elif self.name == DIST_SUSE:
            #SUSE
            if commands.getoutput('cat /etc/SuSE-release | grep "openSUSE"'):
                pass
                #self.name = DIST_OPENSUSE
        elif self.name == DIST_REDHAT:
            #Red Hat Base
            if commands.getoutput('cat /etc/redhat-release | grep "Red Hat"'):
                # Red Hat
                pass
                #self.name = DIST_REDHAT
            if commands.getoutput('cat /etc/redhat-release | grep "CentOS"'):
                # CentOS
                pass
                #self.name = DIST_CENTOS
        elif self.name in ('mandrake', 'mandriva linux'):
            #Mandrake
            if os.path.exists('/etc/mandriva-release') and \
               commands.getoutput('cat /etc/mandriva-release | grep "Mandriva"'):
                pass
                #self.name = DIST_MANDRIVA
                """

    def getDistName(self):
        """
        @param:
            None
        @return:
            Distribution Name(string)
        """
        return platform.linux_distribution()[0]
