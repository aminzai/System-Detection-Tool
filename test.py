from sdt.SystemInfo import SystemInfo

if __name__ == "__main__":
    d = SystemInfo()

    print 'getOsType():',d.getOsType()
    print 'd.getDistName()',d.getDistName()
    print 'd.getArch()',d.getArch()
    print 'd.getVersion()',d.getVersion()
    print 'd.getLocale()',d.getLocale()
