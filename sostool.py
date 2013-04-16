#!/usr/bin/python
__author__ = 'Sterling Alexander'

import sys, os, imp, subprocess, ConfigParser
from fnmatch import fnmatch
from os.path import expanduser

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

def main():

    if len(sys.argv) > 1:
        DEBUG = sys.argv[1]
    else:
        DEBUG = 0

    sostool = Sostool()
    print "Sawce config read"
    plugins = Plugins()
    for file in plugins.pluginList:
        print "Currently executing plugin: " + ( str(file)).split('/')[-1]
        print ""
        subprocess.call(["python", file])

    if DEBUG:
        plugins.debugPrint()

if __name__ == "__main__":
    main()