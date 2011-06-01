from sdt.SystemInfo import SystemInfo

if __name__ == "__main__":
    d = SystemInfo()

    print d.getOsType()
    print d.getArch()
    print d.getVersion()
    print d.getLocale()
