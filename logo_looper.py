# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:48:31 2015

@author: cristhiandick
"""

import pandas as pd
import csv
import time
import logo_grabber as r



xy = pd.read_csv('SP500WEBSITES.csv')

for index, row in xy.iterrows():
   cmpny = (row['website'])   
   cmpny = cmpny.lstrip('http://www.')
   #time.sleep(1)
   r.logo_grabber(cmpny)

