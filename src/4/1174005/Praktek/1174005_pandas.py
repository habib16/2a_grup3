# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 21:34:22 2019

@author: user
"""

import pandas

#Jawaban No. 3
def bukaModeListPandas():
    df = pandas.read_csv('teori.csv')
    dt = pandas.DataFrame(df)
    print(dt['npm'])

#Jawaban No. 4
def bukaModeDictPandas():
    df = pandas.read_csv('teori.csv')
    dt = pandas.DataFrame(df)
    print(dt['npm'])
    
bukaModeDictPandas()