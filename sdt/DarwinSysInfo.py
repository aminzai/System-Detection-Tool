#@Author:Kang-Min Wang (Aminzai)
#@Date:Wed Jun  1 10:59:54 2011
#@desc:
#    For MacOSX

import platform

from SystemInfoBase import SystemInfoBase
from Constant import *

class DarwinSysInfo(SystemInfoBase):
    def getDistName(self):
        """
        @param:
            None
        @return:
            Distribution Name(string)
        """
        return DIST_MACOSX

    def getArch(self):
        """
        @param
            None
        @return
            OS's Arch type(string) ex: x86_64
        """
        return platform.mac_ver()[2]

    def getVersion(self):
        """
        @param
            None
        @return
            OS's version (string) ex: 10.1
        """
        return platform.mac_ver()[0]

    def getVersionName(self):
        """
        @param
            None
        @return
            Os's version name(string) ex: lenny
        """
        raise NotImplementedError

    def getAllUser(self):
        """
        @param
            None
        @return
            get all user in this machine (Dict(string username, string home directory) )
        """
        raise NotImplementedError

pass
