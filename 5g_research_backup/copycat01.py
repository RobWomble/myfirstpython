#!/usr/bin/env python3
""" Alta3 Research || Rob Womble"""

import shutil
import os

def main():
    """ main code """
    os.chdir("/home/student/mycode/")
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    shutil.copytree("5g_research/", "5g_research_backup/")

main()
