#!/usr/bin/env python2
import unittest

from sdt.SystemInfo import SystemInfo

class TestSystemInfo(unittest.TestCase):
    def setUp(self):
        self.d = SystemInfo()

    def test_getStr(self):
        """Print __str__()"""
        pass
        #print(self.d.__str__())

    def test_getOsType(self):
        """get os type"""
        print "getOsType", self.d.getOsType()

    def test_getDistName(self):
        """ get dist name """
        print "getDistName:", self.d.getDistName()

    def test_getArch(self):
        """ getArch """
        print "getArch:", self.d.getArch()

    def test_getVersion(self):
        """ getVersion """
        print "getVersion:", self.d.getVersion()

    def test_getLocale(self):
        """ getLocale"""
        print 'getLocale',self.d.getLocale()


if __name__ == "__main__":
    unittest.main()
