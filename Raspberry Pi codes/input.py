# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 20:25:13 2020

@author: Anand
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:18:45 2020

@author: Anand
"""

import socket 
import time
import paho.mqtt.publish as publish
import re
import os
from datetime import date
from datetime import datetime


def msg_fmt(RXData):
    polData=RXData.strip().decode('utf-8')
    data1=re.sub('\s+',' ',polData)
    s1=data1.split("A")
    devID=s1[0].split(":")[1].split("A")[0].strip(" ")
    s2=s1[1].split(",")
    gyx=s2[0]
    gyy=s2[1]
    gyz=s2[2]
    axx=s2[3]
    axy=s2[4]
    axz=s2[5]
    temp=s2[6].split("C")[0]

    print("DIAL/"+str(devID)+"/accel "+str(axx)+" "+str(axy)+" "+str(axz)) #testing for format errors
    print("DIAL/"+str(devID)+"/gyro "+str(gyx)+" "+str(gyy)+" "+str(gyz)) #testing for format errors
    print("DIAL/"+str(devID)+"/temp "+str(temp)) #testing for format errors
  
    publish.single("DIAL/Temperature", temp, hostname="172.18.0.4")    





UDP_IP = "13.86.105.227" 
UDP_PORT = 9000

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    RXData,addr=sock.recvfrom(1024)
    msg_fmt(RXData)

    