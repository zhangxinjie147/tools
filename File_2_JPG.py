# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import glob
import os
import os.path
import time
from lxml import etree
import sys
import getopt
import pandas as pd

import os,os.path
import zipfile
#import xnat as xnatpy

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
#rootdir = "D:\\zjpg\\"
rootdir="D:\\xinjie\\xj2017\\02读书笔记\\张荫南\\张荫南  思维活动网络初探(1)"
from PIL import Image
for parent,dirnames,filenames in os.walk(rootdir):
        for filename in filenames:
            print filename
            if filename.find('png')>0:
                file_full=os.path.join(parent,filename)
                img = Image.open(file_full)
                dest = str(file_full.split('.')[-2])+'.jpg'
                img.save(dest)
#                img.show()