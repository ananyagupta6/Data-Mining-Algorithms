import numpy as np  
import matplotlib.pyplot as plt  
#import pandas as pd 
import itertools
import copy
import csv
records = [] 
row_count=0
cols=0
row_count = sum(1 for row in csv.reader( open('Test1.csv') ) )
min_support=int(input("Enter minimum support: "))
#records=[['A','C','D'],['B','D'],['A','B','C','E'],['B','D','F']]
with open('Test1.csv', 'rb') as f:
    reader = csv.reader(f)
    records=list(reader)
for i in records:
	while ' ' in i:
		i.remove(' ')
	while '' in i:
		i.remove('')
c1=[]
for i in range(0, len(records)):
	for j in range(0,len(records[i])):
		if records[i][j] not in c1:
			c1.append(records[i][j])
freq={}
for i in range(0, len(records)):
	for j in range(0,len(records[i])):
		if records[i][j] not in freq:
			freq[records[i][j]]=1
		else:
			freq[records[i][j]]=freq[records[i][j]]+1
l=[[]]
print("First frequent item set is: ")
for i in range(0,len(c1)):
	if freq[c1[i]]>=min_support:
		l[0].append(c1[i])
		print(c1[i])
c2=list(itertools.combinations(l[0], 2))
for k in c2:
	for i in range(0, len(records)):
		if k[0] in records[i] and k[1] in records[i]:
			if k not in freq:
				freq[tuple(k)]=1
			else:
				freq[tuple(k)]=freq[tuple(k)]+1
x=[]
l.append([])
print("Second frequent item set is: ")
for i in c2:
	if i in freq and freq[i]>=min_support:
		l[1].append(i)
		print(i)
		for k in i:
			if k not in x:
				x.append(k)
count=2
while x:
	count=count+1
	c=list(itertools.combinations(x, count))
	check=1
	temp=copy.deepcopy(c)
	for i in c:
		#apriori property-pruning
		for j in i:
			if j not in l[0]:
				temp.remove(i)
				break
		check=1
		for j in range(2,len(i)):
			if check==0:
				break
			subs=list(itertools.combinations(i,j))
			for k in subs:
				if k not in l[j-1]:
					temp.remove(i)
					check=0
					break
	c=temp
	for j in c:
		for i in records:
			check=1
			for k in j:
				if k not in i:
					check=0
					break
			if check==1:
				if j not in freq:
					freq[j]=1
				else:
					freq[j]=freq[j]+1
	x=[]
	l.append([])
	for j in c:
		if freq[j]>=min_support:
			l[count-1].append(j)
			for k in j:
				x.append(k)
	if x:
		print("Next frequent item set is: ")
		print(l[count-1])


