__author__ = 'Sterling Alexander'

import re, ConfigParser
from termcolor import colored, cprint
from os.path import expanduser

SPACER = "    "
LINESPACER = " -- "
ERROR = " === Error === | "

class dumpReport:

    def __init__(self):
        cfgpath = expanduser("~/.sostool_config")
        self.kdumpOptions = []
        self.files = {}
        cfg = ConfigParser.ConfigParser()
        cfg.read(cfgpath)
        for section in cfg.sections():
#            print section
            for option in cfg.options(section):
                line = cfg.get(section,option)
                line = line.split(',')
                for entry in line:
 #                   print "option => " + option.strip() + " entry => " + entry.strip()
                    self.files[option.strip()] = entry.strip()

    def parseFiles(self):
        try:
            self.hostname = open(self.files["hostname"]).readline()
            self.release = open(self.files["redhat-release"]).readline()
            self.cmdline = open(self.files["cmdline"]).readline()
            self.sysctl = []

            for line in open(self.files["installed-rpms"]):
                if "kexec-tools" in line:
                    self.toolsVersion = line
            for line in open(self.files['kdump']):
                if line[0] != '#' and line[0] != '\n':
                    self.kdumpOptions.append(line.rstrip('\n'))
            for line in open(self.files['sysctl']):
                if 'panic' in line or 'sysrq' in line:
                    self.sysctl.append(line.rstrip('\n'))

        except IOError, e:
            print ERROR + e.message
            return 0



def main():
    print SPACER,
    cprint("====================| kernel capture report |====================", 'yellow', 'on_grey')
    dump = dumpReport()
    dump.parseFiles()
    print "\n" +  LINESPACER + "Hostname:\t\t\t" + dump.hostname.rstrip()
    print LINESPACER + "kexec-tools version:\t" + "  ".join(dump.toolsVersion.split())
    print LINESPACER + "Cmdline:\t\t\t" + dump.cmdline
    print LINESPACER + "Current kdump.conf options"
    print ""
    if (len(dump.kdumpOptions) == 0):
        print SPACER,
        cprint(" ===!!! Kdump configuration file using default (empty) options !!!===", 'red', 'on_blue')
        print ""
    else:
        for line in dump.kdumpOptions:
            print SPACER*2 + line
        print ""
    for line in dump.sysctl:
        print LINESPACER + line
    print ""

    raw_input("Press any key to continue...")


if __name__ == "__main__":
    main()