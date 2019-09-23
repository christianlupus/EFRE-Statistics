#! /usr/bin/python

import sys

if len(sys.argv) != 4:
	print("You must provide exactly tree parameters.")
	exit(1)

fin = open(sys.argv[1], 'r')
datain = eval(fin.read())
fin.close()

dataout = open(sys.argv[2], 'w+')
texout = open(sys.argv[3], 'w+')


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

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

dataout.write('Month Project_Hours Total_Hours Ext_Hours Ratio\n')

for m in months:
	i = i + 1
	
	data[i] = {}
	
	if m in datain:
		tot = datain[m]['Hours_total']
		proj = datain[m]['Hours_project']
		
		ratio = calcRatio(proj, tot)
		
		hoursProj += proj
		hoursTot  += tot
		
		dataout.write("%s %d %d %d %f\n" % (m, proj, tot, (tot-proj), ratio))
		
ratio = calcRatio(hoursProj, hoursTot)

texout.write('\\def\\totalratio{%f}\n' % ratio)
