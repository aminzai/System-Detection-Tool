#@Author:Kang-Min Wang (Aminzai)
#@Date:Wed 01 Jun 2011 05:23:31 PM CST
#@desc:
#    For Debian

import platform

from LinuxSysInfoBase import LinuxSysInfoBase
from Constant import *

class DebianSysInfo(LinuxSysInfoBase):
    def __init__(self):
        pass

    def getArch(self):
        """
        @param
            None
        @return
            OS's Arch type(string) ex: x86_64
        """
        return platform.architecture()[0]

    def getVersion(self):
        """
        @param
            None
        @return
            OS's version (string) ex: 10.1
        """
        return platform.dist()[1]

    def getCodename(self):
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
