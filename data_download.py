#!/usr/bin/python
# coding: UTF-8
 
"""This script parse stock info"""

import heapq 
import pandas as pd
import numpy
import tushare as ts

#dim k as int
 

stock_info = ts.get_stock_basics()    
#frame1 = pd.DataFrame(stock_info)
#frame1.to_csv('D20190916.csv')
k=0
for i in stock_info.index:
	df = ts.get_k_data(i,start='2014-01-01')
	if df is None:
		continue
	frame=pd.DataFrame(df)
	frame.to_csv(str(i)+'.csv')
	k=k+1
	print(i,k)
	#if input()=='n':
	#	break
