"""
@Author:Kang-Min Wang (Aminzai)
@Date:Tue May 31 12:26:54 2011
@desc:
    This is System Detection tool's base class
"""
class SystemInfo:
    """
    System Dectection Tool
    """
    def getOsName(self):
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

    def getUserLocale(self,user):
        """
        @param
            user: username(string)
        @return
            locale info (string) ex: en_US
        """
        raise NotImplementedError

