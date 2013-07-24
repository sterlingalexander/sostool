#!/usr/bin/python

__author__ = 'Sterling Alexander'

import re, ConfigParser
from termcolor import colored, cprint
from os.path import expanduser

SPACER = "   "
LINESPACER = " -- "
ERROR = " === Error === | "

class baseSos:

    def __init__(self):
        self.files = {}
        cfgpath = expanduser("~/.sostool_config")
        cfg = ConfigParser.ConfigParser()
        cfg.read(cfgpath)
        for section in cfg.sections():
            for option in cfg.options(section):
                line = cfg.get(section,option)
                line = line.split(',')
                for entry in line:
#                   print "option => " + option.strip() + " entry => " + entry.strip()
                    self.files[option.strip()] = entry.strip()
        self.redhatRelease = "etc/redhat-release"
        self.testfile = "proc/meminfo"
        self.fhostname = "hostname"
        self.fuptime = "uptime"
        self.dmidecode = "dmidecode"
        self.rpms = "installed-rpms"

    def hostname(self):
        try:
            fh = open(self.fhostname)
            print "Machine hostname: " + fh.readline()
            return 1
        except IOError:
            print ERROR + "File `hostname` not found in sosreport"
            return 0

    def redHatRelease(self):
        try:
            fh = open(self.redhatRelease)
            print "Red Hat release: " + fh.readline()
            return 1
        except IOError:
            print ERROR + "File `etc/redhat-release` not found in sosreport."
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
    baseReport.hostname()
    baseReport.redHatRelease()
    baseReport.dmiOut()

if __name__ == "__main__":
    main()