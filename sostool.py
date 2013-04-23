#!/usr/bin/python
__author__ = 'Sterling Alexander'

import sys, os, imp, subprocess, ConfigParser
from fnmatch import fnmatch
from os.path import expanduser
from termcolor import colored, cprint
import argparse

class Plugins:

    def __init__(self):
        self.root = self.getScriptPath()
        self.pattern = "*.py"
        self.sosPwd = self.getPwd()
        self.pluginList = self.buildList()

    def getScriptPath(self):
        return os.path.dirname(os.path.realpath(sys.argv[0]))

    def getPwd(self):
        return os.getcwd()

    def buildList(self):
        plist = []
        pdir = self.root + "/plugins/"
        for path, subdirs, files in os.walk(pdir):
            for name in files:
                if fnmatch(name, self.pattern):
                    fullpath = os.path.join(path, name)
                    # print " --> " + os.path.join(path, name)
                    plist.append(fullpath)
        return plist

    def debugPrint(self):
        print "Current Plugin List:"
        print self.pluginList
        print "Current script root:\t" + self.root
        print "Plugin parse pattern:\t" + self.pattern
        print "Current pwd:\t\t" + self.sosPwd

class Sostool():

    def __init__(self):
        cfgpath = expanduser("~/.sostool_config")
        config = ConfigParser.ConfigParser()
        try:
            config.readfp( open(cfgpath) )
            print "Configuration found and read successfully"
        except IOError:
            self.defaultConfig(cfgpath)
            config.read(cfgpath)
            print "Configuration read, starting tools..."

    def defaultConfig(self, cfgpath):
        print "Generating the default configuration file..."
        cfg = open(cfgpath, 'w')
        baseConfig = ConfigParser.ConfigParser()
        baseConfig.add_section('Files')
        baseConfig.set('Files', 'hostname', 'hostname')
        baseConfig.set('Files', 'chkconfig', 'chkconfig')
        baseConfig.set('Files', 'redhat-release', 'etc/redhat-release')
        baseConfig.set('Files', 'meminfo', 'proc/meminfo')
        baseConfig.set('Files', 'uptime', 'uptime')
        baseConfig.set('Files', 'dmidecode', 'dmidecode')
        baseConfig.set('Files', 'sysctl', 'sos_commands/kernel/sysctl_-a')
        baseConfig.set('Files', 'kdump', 'etc/kdump.conf')
        baseConfig.set('Files', 'free', 'free')
        baseConfig.set('Files', 'df', 'df')
        baseConfig.set('Files', 'installed-rpms', 'installed-rpms')
        baseConfig.set('Files', 'cmdline', 'proc/cmdline')
        baseConfig.write(cfg)
        cfg.close()
        print "....Done!"

    def sosreportRootCheck(self):
    # TODO: Improve this dirty hack to check if we are in sosroot
        try:
            fh = open("hostname", "r")
            return 1
        except IOError:
            print "\n\tHrm, this does not appear to be the root of a sosreport..."
            print "\tFor your reference, you are here: " + os.getcwd()
            print "\tI'm baffeled, so I'm quitting..."
            return 0

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dumpreport", help="Display information on kdump/diskdump/netdump", action="store_true")
    parser.add_argument("-b", "--base", help="Display basic machine information", action="store_true")
    parser.add_argument("-v", "--verbosity", help="Increase the output verbosity", action="store_true")
    args = parser.parse_args()

#    usage='By default sostool will run all plugins.  This may change in the future'
#    description='Performs common analysis functions on sosreports'
#    parser = ArgumentParser(usage=usage,description=description)
#
#    parser.add_argument('-d','--dumpreport', action='store', dest='state',
#                        help='Run the dumpreport plugin' ,required=False)
#    parser.add_argument('-b','--base',action='store',dest='county',
#                        help='Optional county in state process')
    sostool = Sostool()
    if not sostool.sosreportRootCheck():
        exit()

    print type(args)
    print args.base
    print args.dumpreport
    print args.verbosity

#    pluginList = []
#    for x in args:
#        pluginList.append(x)
#    print pluginList

    print "Sawce config has been read....(feels official, doesn't it?)"
    plugins = Plugins()

    for file in plugins.pluginList:
        print file
        print ""
        cprint("Currently executing plugin: " + ( str(file)).split('/')[-1], 'blue', 'on_grey')
        print ""
        subprocess.call(["python", file])
        raw_input("Press any key to continue...")

# Most likely this is now dead code.
#    if DEBUG:
#        plugins.debugPrint()

if __name__ == "__main__":
    main()