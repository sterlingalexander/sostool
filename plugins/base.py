#!/usr/bin/python

__author__ = 'Sterling Alexander'

class baseSos:

    def __init__(self):
        self.testfile = "proc/meminfo"
        self.fhostname = "hostname"
        self.fuptime = "uptime"
        self.dmidecode = "dmidecode"

    def sosRootCheck(self):
        # Dirty hack to check if we are in sosroot
        try:
            open(self.testfile, "r")
            return 1
        except IOError:
            print "\n\tHrm, this does not appear to be the root of a sosreport..."
            print "\tI'm baffeled, so I'm quitting..."
            return 0

    def dmiOut(self):
        for line in open(self.dmidecode):
            if "CPU" in line:
                print line

def main():
    baseReport = baseSos()
    if baseReport.sosRootCheck() == 0:
        exit()

    print "I'm running now and my name is base.py!"
    baseReport.dmiOut()

if __name__ == "__main__":
    main()