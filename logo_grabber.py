# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:40:25 2015

@author: cristhiandick
"""

import requests

def logo_grabber(cmpny):
    url = 'https://logo.clearbit.com/' + cmpny #+ '.com'
    page = requests.get(url)
    filename = cmpny.rstrip('.com') + 'logo'

    if page.status_code == 200:
        with open (filename, 'wb') as testurl:
            testurl.write(page.content)
        
    #r = ('https://autocomplete.clearbit.com/v1/companies/suggest?query=' + cmpny) 
    #r2 = requests.get(r) 
          
    #print (r2.content);
    print (filename);     