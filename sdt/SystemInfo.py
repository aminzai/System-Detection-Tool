from SystemInfoBase import SystemInfoBase
from Constant import *

class SystemInfo(SystemInfoBase):
    def __init__(self):
        if OS_TYPE_DARWIN == self.getOsType():
            from DarwinSysInfo import DarwinSysInfo
            self.__class__ = DarwinSysInfo
        if OS_TYPE_LINUX == self.getOsType():
            from DebianSysInfo import DebianSysInfo
            self.__class__ = DebianSysInfo

pass
