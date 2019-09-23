#! /usr/bin/python

import sys

if len(sys.argv) != 3:
	print("You must provide exactly one parameter that is the file to read the data from.")
	exit(1)

fin = open(sys.argv[1], 'r')
datain = eval(fin.read())
fin.close()

#print(data)

#months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
months = ['Jan', 'Feb', 'Mar', 'Apr']

data = {}
hoursTot = 0
hoursProj = 0
i = 0

def calcRatio(proj,tot):
	if tot == 0:
		if proj == 0:
			return 0
		else:
			# Raise error
			proj / tot
	else:
		return proj / tot

for m in months:
	i = i + 1
	
	data[i] = {}
	
	if m in datain:
		tot = datain[m]['Hours_total']
		proj = datain[m]['Hours_project']
		
		if 'Desc' in datain[m]:
			data[i]['Desc'] = datain[m]['Desc']
		else:
			data[i]['Desc'] = ""
	else:
		tot = 0
		proj = 0
		data[i]['Desc'] = ""
	
	data[i]['tot'] = tot
	data[i]['proj'] = proj
	
	data[i]['ratio'] = calcRatio(proj, tot)
	
	
	hoursTot += data[i]['tot']
	hoursProj += data[i]['proj']

ratio = hoursProj / hoursTot

print(data)
print(ratio)
