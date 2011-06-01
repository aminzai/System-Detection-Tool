from SystemInfoBase import SystemInfoBase
from DarwinSysInfo import DarwinSysInfo
from Constant import *

class SystemInfo(SystemInfoBase):
    def __init__(self):
        if OS_TYPE_DARWIN == self.getOsType():
            self.__class__ = DarwinSysInfo

pass
