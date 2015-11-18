# -*- coding: utf-8 -*-
__author__ = 'WangFeng'
import numpy as np
import csv
def readdata():
    data=np.loadtxt('csv_practice.csv',dtype=str,delimiter=',',skiprows=1)
    temp=[]
    for specificdata in data:
        #print(specificdata)
        temp.append(  ( specificdata[0],processAge(specificdata[1]),specificdata[2],specificdata[3],specificdata[4]) )
    writecsv(temp)
def processAge(age):
    ages=int(age)
    if ages<20:
        return '0'
    else:
        return str( ages//3+0)

def writecsv(s):
    csvfile = file('csv_test.csv', 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(['id','age','degree','gender','major'])
    writer.writerows(s)

    csvfile.close()
if __name__=='__main__':
    readdata()