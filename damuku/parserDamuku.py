# -*- coding: utf-8 -*-
# @Author: Jingyuexing
# @Date:   2020-04-30 15:48:44
# @Last Modified by:   Jingyuexing
# @Last Modified time: 2020-05-02 00:12:28

import xml.etree.ElementTree as ET

class Danmaku:
    """弹幕类
    ```xml
    <d p="16.67500,1,25,16777215,1588305968,0,b00ca606,32067442918293507">借你吉言</d>
    ```
    第一个 是stime 0 然后是mode 1  再是size 2 再是color 3 再是date 4 再是pool 5 再是uhash 6 再是dmid 7
    """
    color:int
    date:int
    dmid:int
    pool:int
    stime:float
    mode:int
    text:str
    uhash:str
    size:int
    data:list
    def __init__(self,data):
        if(data!=''):
            root = ET.parse(data)
            rootEle = root.getroot()
            for ele in rootEle.findall('d'):
                tempdict = {}
                attribList = ele.attrib['p'].split(',')
                tempdict['uhash'] = attribList[6]
                tempdict['date'] = int(attribList[4])
                tempdict['pool'] = int(attribList[5])
                tempdict['color'] = int(attribList[3])
                tempdict['size'] = int(attribList[2])
                tempdict['dmid'] = attribList[7]
                tempdict['mode'] = int(attribList[1])
                tempdict['stime'] = float(attribList[0])
                self.data.append(tempdict)
    def getDanmu(self,index=0):
        data = self.data[index]
        danmu = Danmaku("")
        danmu.uhash = data['uhash']
        danmu.date = data['date']
        danmu.pool = data['pool']
        danmu.size = data['size']
        danmu.dmid = data['dmid']
        danmu.mode = data['mode']
        danmu.stime = data['stime']
        danmu.color = data['color']
        return danmu

