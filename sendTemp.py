#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Adafruit_DHT as dht
import time
import math
import numpy as np
from matplotlib import pyplot as plt

RANGE_XTIME = 60


#h,t = dht.read_retry(dht.AM2302,4)
h,t = dht.read_retry(dht.DHT11,4)


tempList = np.array([float(round(t,2)) for _ in range(RANGE_XTIME)])
humdList = np.array([float(round(h,2)) for _ in range(RANGE_XTIME)])

loopCount = 0
loopList = np.zeros(RANGE_XTIME)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax2 = ax1.twinx()
lax1, = ax1.plot(loopList, tempList, color='red', label="Temperture")
lax2, = ax2.plot(loopList, humdList, color='blue', label="Humidity")

ax1.set_ylim(20,30)
ax1.set_xlabel("time[s]")
ax1.set_ylabel("Temperature")
ax2.set_ylabel("Humidity")

while True:
#for i in range(5):
    # time.sleep(0.1)
    #h,t = dht.read_retry(dht.AM2302,4)
    h,t = dht.read_retry(dht.DHT11,4)

    data = {
        "temperature":t,
        "humidity":h
    }

    print("send:{}".format(data))

    if abs(t - tempList[-1]) < 20:
        tempList = np.append(tempList,float(round(t,2)))
    else:
        tempList = np.append(tempList,float(round(tempList[-1],2)))
    tempList = np.delete(tempList,0)

    if abs(h - humdList[-1]) < 20:
        humdList = np.append(humdList,float(round(h,2)))
    else:
        humdList = np.append(humdList,float(round(humdList[-1],2)))
    humdList = np.delete(humdList,0)

    loopList = np.append(loopList,float(loopCount))
    loopList = np.delete(loopList,0)
    
    
    lax1.set_data(loopList, tempList)
    lax2.set_data(loopList, humdList)
 
    plt.xlim(min(loopList),max(loopList))
    ax1.set_ylim(min(tempList)-0.1,max(tempList)+0.1)
    ax2.set_ylim(min(humdList)-0.1,max(humdList)+0.1)


    h1,l1 = ax1.get_legend_handles_labels()
    h2,l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1+h2,l1+l2,loc='best')

    plt.pause(0.1)
    loopCount += 1


