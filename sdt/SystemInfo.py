from SystemInfoBase import SystemInfoBase
from DarwinSysInfo import DarwinSysInfo
from LinuxSysInfoBase import LinuxSysInfoBase

from Constant import *

class SystemInfo(SystemInfoBase):
    def __init__(self):
        if OS_TYPE_DARWIN == self.getOsType():
            self.__class__ = DarwinSysInfo
        elif OS_TYPE_LINUX == self.getOsType():
            self.__class__ = LinuxSysInfoBase
            self.__init__()

pass
