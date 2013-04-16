#!/usr/bin/python

__author__ = 'Sterling Alexander'

SPACER = "   "
ERROR = " === Error === | "

class baseSos:

    def __init__(self):
        self.redhatRelease = "etc/redhat-release"
        self.testfile = "proc/meminfo"
        self.fhostname = "hostname"
        self.fuptime = "uptime"
        self.dmidecode = "dmidecode"
        self.ERR_LIST = []

    def sosRootCheck(self):
        # Dirty hack to check if we are in sosroot
        try:
            fh = open(self.testfile, "r")
            return 1
        except IOError:
            print "\n\tHrm, this does not appear to be the root of a sosreport..."
            print "\tI'm baffeled, so I'm quitting..."
            return 0

    def hostname(self):
        try:
            fh = open(self.fhostname)
            print "\nMachine hostname: " + fh.readline()
            return 1
        except IOError:
            print ERROR + "File `hostname` not found in sosreport"
            return 0

    def redHatRelease(self):
        try:
            fh = open(self.redhatRelease)
            print "\nRed Hat release: " + fh.readline()
            return 1
        except IOError:
            print ERROR + "\nFile `etc/redhat-release` not found in sosreport."
            print ERROR + "--==:: WARNING ::==--  This may be an unsupported OS install."
            return 0

    def dmiOut(self):
        try:
            fh = open(self.dmidecode)
            flag = False
            for line in fh:
                if "System Information" in line:
                    print "System Information"
                    flag = True
                elif flag == True and line != '\n':
                    print SPACER + line.strip()
                    line = fh
                elif line == '\n':
                    flag = False
            print ""
            return 1
        except IOError:
            print ERROR + "File `dmidecode` not found in sosreport."
            return 0


def main():
    baseReport = baseSos()
    if baseReport.sosRootCheck() == 0:
        exit()
    baseReport.hostname()
    baseReport.redHatRelease()
    baseReport.dmiOut()

if __name__ == "__main__":
    main()