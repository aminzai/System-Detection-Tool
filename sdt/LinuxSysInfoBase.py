import platform

from SystemInfoBase import SystemInfoBase
from Constant import *

class LinuxSysInfoBase(SystemInfoBase):
    def __init__(self):
        if DIST_DEBIAN == self.getDistName():
            from DebianSysInfo import DebianSysInfo
            self.__class__ = DebianSysInfo
            self.__init__()

    def getDistName(self):
        """
        @param:
            None
        @return:
            Distribution Name(string)
        """
        return platform.linux_distribution()[0]
