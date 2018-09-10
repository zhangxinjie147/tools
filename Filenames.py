# -*- coding: utf-8 -*-
"""
Created on Thu Sep 06 11:58:19 2018

@author: zhang
"""

import glob
import os
import os.path
import shutil
import time
from lxml import etree
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def write_file(targetdir):
    title=targetdir
#    title=r'D:\xinjie'
    rootdir = str(title).strip().decode('utf-8')
    #rootdir=r'D:\Tools\tomcat'
    subjects=[]
    for parent,dirnames,filenames in os.walk(rootdir):
        for dirname in dirnames:
            for filename in filenames:
                fullpath = os.path.join(parent, dirname, filename)
        #        index_num=str('50')
        #        if dirname.find(index_num)>=0:
                if fullpath not in subjects:
                    subjects.append(fullpath)
    print subjects
    target_file =os.path.join(rootdir,'files.txt')
    fileH=open(target_file,'wb')
    for subjectname in subjects:
        fileH.write(subjectname)
        fileH.write('\n')
    fileH.close()

def main(argv=None):
    if argv is None:
        argv = sys.argv
        print argv
    if len(argv)==2 :
        rootdir= argv[1]
    else:
        print " please input parm rootdir "
  #      parmpath='M:\BaiduNetdiskDownload\CBpreprocessed\COBRE\Test\Parm_lin.xls'
        rootdir=r'D:\temp'
    
    write_file(rootdir)
    

if __name__ == "__main__":
    sys.exit(main())

