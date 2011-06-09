#@Author:Kang-Min Wang (Aminzai)
#@Date:Tue May 31 12:26:54 2011
#@desc:
#    This is System Detection tool's base class

import os
import platform

from Constant import *

class SystemInfoBase:
    """
    System Dectection Tool
    """
    def getOsType(self):
        """
        @param:
            None
        @return:
            OS Type(string) ex: linux, macos
        """
        osType = platform.system().lower()

        if OS_TYPE_LINUX == osType:
            return OS_TYPE_LINUX
        elif OS_TYPE_DARWIN == osType:
            return OS_TYPE_DARWIN

    def getDistName(self):
        """
        @param:
            None
        @return:
            OS Name(string)
        """
        raise NotImplementedError

    def getArch(self):
        """
        @param
            None
        @return
            OS's Arch type(string) ex: x86_64
        """
        raise NotImplementedError

    def getVersion(self):
        """
        @param
            None
        @return
            OS's version (string) ex: 10.1
        """
        raise NotImplementedError

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

    def getLocale(self):
        """
        @param
            None
        @return
            locale info (string) ex: en_us
        """
        LANG = "en_us"
        try:
            LANG = os.getenv('LANG').split('.')[0].lower()
        except TypeError:
            pass

        return LANG

pass
