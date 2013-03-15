#!/usr/bin/python

__author__ = 'Sterling Alexander'

import sys, os, imp
from imp_get_suffixes import module_types
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
                    print " --> " + os.path.join(path, name)
                    plist.append(name)
        return plist

    def debugPrint(self):
        print "Current Plugin List:"
        print self.pluginList
        print "Current script root:\t" + self.root
        print "Plugin parse pattern:\t" + self.pattern
        print "Current pwd:\t\t" + self.sosPwd

def main():
    plugins = Plugins()

    print 'Package:'
    f, filename, description = imp.find_module('example')
    print module_types[description[2]], filename
    print

    print 'Sub-module:'
    f, filename, description = imp.find_module('submodule', ['./example'])
    print module_types[description[2]], filename
    if f: f.close()
    plugins.debugPrint()

if __name__ == "__main__":
    main()