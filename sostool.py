#!/usr/bin/python

__author__ = 'Sterling Alexander'

import sys, os, imp, subprocess
from fnmatch import fnmatch

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

def main():

    if len(sys.argv) > 1:
        DEBUG = sys.argv[1]
    else:
        DEBUG = 0

    plugins = Plugins()
    for file in plugins.pluginList:
        print "I want to execute " + str(file)
        subprocess.call(["python", file])

    if DEBUG:
        plugins.debugPrint()

if __name__ == "__main__":
    main()