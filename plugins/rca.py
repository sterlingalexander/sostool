__author__ = 'sterling'

import re, ConfigParser
from termcolor import colored, cprint
from os.path import expanduser

SPACER = "    "
LINESPACER = " -- "
ERROR = " === Error === | "

# class rcaReport:
#
#     def __init__(self):
#         cfgpath = expanduser("~/.sostool_config")
#         self.kdumpOptions = []
#         self.files = {}
#         self.sysctl = []
#         self.memory = []
#         self.storage = []
#         cfg = ConfigParser.ConfigParser()
#         cfg.read(cfgpath)
#         for section in cfg.sections():
#         #            print section
#             for option in cfg.options(section):
#                 line = cfg.get(section,option)
#                 line = line.split(',')
#                 for entry in line:
#                 #                   print "option => " + option.strip() + " entry => " + entry.strip()
#                     self.files[option.strip()] = entry.strip()
#
#     def parseFiles(self):
#         try:
#             self.hostname = open(self.files["hostname"]).readline()
#         except Exception:
#             self.hostname = "===!!! Unable to determine !!!==="
#         #        try:
#         #            self.hostname = open(self.files["chkconfig"]).readline()
#         #        except Exception:
#         #            self.hostname = "===!!! Unable to determine !!!==="
#         try:
#             self.release = open(self.files["redhat-release"]).readline()
#         except Exception:
#             self.release = "===!!! Unable to determine !!!==="
#         try:
#             self.cmdline = open(self.files["cmdline"]).readline()
#         except Exception:
#             self.cmdline = "===!!! Unable to determine !!!==="
#         try:
#             for line in open(self.files["installed-rpms"]):
#                 if "kexec-tools" in line:
#                     self.toolsVersion = line
#         except Exception:
#             self.toolsVersion = "===!!! Unable to determine !!!==="
#         try:
#             for line in open(self.files['kdump']):
#                 if line[0] != '#' and line[0] != '\n':
#                     self.kdumpOptions.append(line.rstrip('\n'))
#         except Exception:
#             self.kdumpOptions.append("===!!! Unable to determine !!!===")
#         try:
#             for line in open(self.files['sysctl']):
#                 if 'panic' in line or 'sysrq' in line:
#                     self.sysctl.append(line.rstrip('\n'))
#         except Exception:
#             self.sysctl.append("===!!! Unable to determine !!!===")
#
#         try:
#             for line in open(self.files["free"]).readlines():
#                 self.memory.append(line.rstrip('\n'))
#         except Exception:
#             self.memory.append("===!!! Unable to determine !!!===")
#         try:
#             for line in open(self.files["df"]).readlines():
#                 self.storage.append(line.rstrip('\n'))
#         except Exception:
#             self.storage.append("===!!! Unable to determine !!!===")
#
# def main():
#     cprint("====================| kernel capture report |====================", 'yellow', 'on_grey')
#     dump = dumpReport()
#     dump.parseFiles()
#     print "\n" +  LINESPACER + "Hostname:\t\t\t" + dump.hostname.rstrip()
#     print LINESPACER + "OS Version:\t\t\t" + dump.release.rstrip()
#     print LINESPACER + "kexec-tools version:\t" + "  ".join(dump.toolsVersion.split())
#     print LINESPACER + "Cmdline:\t\t\t" + dump.cmdline
#     cprint("=====| Current kdump.conf options |=====", 'yellow', 'on_grey')
#     print ""
#     if (len(dump.kdumpOptions) == 0):
#         print SPACER,
#         cprint("===!!! Kdump configuration file using default (empty) options !!!===", 'red', 'on_blue')
#         print ""
#     else:
#         for line in dump.kdumpOptions:
#             print LINESPACER + line
#         print ""
#     cprint("=====| sysctl parameters |=====", 'yellow', 'on_grey')
#     print ""
#     for line in dump.sysctl:
#         print LINESPACER + line
#     print ""
#     cprint("=====| System memory |=====", 'yellow', 'on_grey')
#     print ""
#     for line in dump.memory:
#         print LINESPACER + line
#     print ""
#     cprint("=====| System storage |=====", 'yellow', 'on_grey')
#     print ""
#     for line in dump.storage:
#         print LINESPACER + line
#     print ""
#
# if __name__ == "__main__":
#     main()