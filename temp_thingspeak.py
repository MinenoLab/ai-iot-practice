#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Adafruit_DHT as dht
import numpy as np
from matplotlib import pyplot as plt
import requests

# thingspeakに送る処理
def sendToThingSpeak(t,h):
    url = "https://api.thingspeak.com/update"
    params = {
        "api_key":"99KW92UCI5DT8QKN",
        "filed0":t,
        "field1":h
    }
    requests.get(url,params=params)

RANGE_XTIME = 60


h,t = dht.read_retry(dht.DHT11,4)

# ---データ格納場所の用意---
tempList = np.array([float(round(t,2)) for _ in range(RANGE_XTIME)])
humdList = np.array([float(round(h,2)) for _ in range(RANGE_XTIME)])
# ---データ格納場所の用意---

loopCount = 0
loopList = np.zeros(RANGE_XTIME)

# ---グラフ描画の準備---
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax2 = ax1.twinx()
lax1, = ax1.plot(loopList, tempList, color='red', label="Temperture")
lax2, = ax2.plot(loopList, humdList, color='blue', label="Humidity")

ax1.set_ylim(20,30)
ax1.set_xlabel("time[s]")
ax1.set_ylabel("Temperature")
ax2.set_ylabel("Humidity")
# ---グラフの準備---

while True:
    # 温湿度データの取得
    h,t = dht.read_retry(dht.DHT11,4)

    # ---取得したデータをターミナルに表示---
    data = {
        "temperature":t,
        "humidity":h
    }
    print("send:{}".format(data))
    # ---取得したデータをターミナルに表示---

    # thingspeakに送信
    sendToThingSpeak(t,h)

    # 温度データをグラフ描画のために保管
    if abs(t - tempList[-1]) < 20:
        tempList = np.append(tempList,float(round(t,2)))
    else:
        tempList = np.append(tempList,float(round(tempList[-1],2)))

    # 一番古い温度データを削除
    tempList = np.delete(tempList,0)

    # 湿度データをグラフ描画のために保管
    if abs(h - humdList[-1]) < 20:
        humdList = np.append(humdList,float(round(h,2)))
    else:
        humdList = np.append(humdList,float(round(humdList[-1],2)))

    # 一番古い湿度データを削除
    humdList = np.delete(humdList,0)

    # 取得時刻を保管
    loopList = np.append(loopList,float(loopCount))

    # 削除した古い温湿度データの取得時刻を削除
    loopList = np.delete(loopList,0)

pp    # ---グラフに描画するための準備---
    lax1.set_data(loopList, tempList)
    lax2.set_data(loopList, humdList)

    plt.xlim(min(loopList),max(loopList))
    ax1.set_ylim(min(tempList)-0.1,max(tempList)+0.1)
    ax2.set_ylim(min(humdList)-0.1,max(humdList)+0.1)

    h1,l1 = ax1.get_legend_handles_labels()
    h2,l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1+h2,l1+l2,loc='best')
    # ---グラフに描画するための準備---

    # グラフに描画
    plt.pause(0.1)
    loopCount += 1
