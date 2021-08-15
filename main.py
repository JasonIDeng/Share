#!/usr/bin/python
# coding: UTF-8
 
"""This script parse stock info"""

from numpy import NaN
import heapq 
import pandas as pd
import numpy as np
import tushare as ts
import os 
from itertools import chain

cha_60_120=[]
#cha_20_60_k = {"max":[],"time_g":[],"min":[],"time_d":[]}

#k=1
for filename in os.listdir():
	#print(k,filename)
	stock_data = pd.read_csv(filename, parse_dates=[1])
	if int(len(stock_data))==0:
		continue
	stock_data.sort_values(by='date',ascending=False,  inplace=True)

	newest=stock_data['MA_60_120'][0]
	max=newest
	min=0
	
	
	k=1
	cha_60_120_k = {"max":[],"time_g":[],"min":[],"time_d":[]}
	#print(max,min,k,len(stock_data))
	while k<int(len(stock_data['MA_60_120'])) and ~np.isnan(stock_data['MA_60_120'][k]):	
		while stock_data['MA_60_120'][k]>=0 :
			#print(k,stock_data['MA_60_120'][k],max,min)
			if stock_data['MA_60_120'][k]>max:
				max=stock_data['MA_60_120'][k]  
			k=k+1
		cha_60_120_k['max'].append(max)
		cha_60_120_k['time_g'].append(k-1)
		max=0
		#print(cha_20_60_k)
	
		while stock_data['MA_60_120'][k]<=0 :
			#print(k,stock_data['MA_20_60'][k],max,min)
			if stock_data['MA_60_120'][k]<min:
				min=stock_data['MA_60_120'][k]  
			k=k+1
		cha_60_120_k['min'].append(min)
		cha_60_120_k['time_d'].append(k-1)
		min=0

	l=[]
	l.append(filename[0:6])
	l.append(newest)

	m=0
	while m <int(len(cha_60_120_k['max'])):
		l.append(cha_60_120_k['max'][m])
		l.append(cha_60_120_k['time_g'][m])
		l.append(cha_60_120_k['min'][m])
		l.append(cha_60_120_k['time_d'][m])
		m=m+1
	print(l[0:6])
	cha_60_120.append(l)
	cha_60_120_k.clear()
	

frame=pd.DataFrame(cha_60_120)
frame.to_csv('/Users/Deng/Desktop/股票数据/main.csv')
