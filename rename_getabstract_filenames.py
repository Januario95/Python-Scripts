#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 08:05:23 2022

@author: Januario Cipriano
"""

import os
from glob import glob

files = glob('*.pdf')
for file in files:
    try:
        os.rename(file, file.replace('-', ' ').title())
    except Exception as exc:
        print(exc)
