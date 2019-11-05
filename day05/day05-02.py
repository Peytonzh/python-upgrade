#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import shutil

file1 = sys.argv[1]
file2 = sys.argv[2]
shutil.copyfile(file1,file2)

