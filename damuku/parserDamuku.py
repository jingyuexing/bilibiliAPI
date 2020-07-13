# -*- coding: utf-8 -*-
# @Author: Jingyuexing
# @Date:   2020-04-30 15:48:44
# @Last Modified by:   Admin
# @Last Modified time: 2020-07-14 00:58:37

import xml.etree.cElementTree as cET


class Danmaku:
    """弹幕类
    ```xml
    <d p="16.67500,1,25,16777215,1588305968,0,b00ca606,32067442918293507">借你吉言</d>
    ```
    第一个 是stime 0 然后是mode 1  再是size 2 再是color 3 再是date 4 再是pool 5 再是uhash 6 再是dmid 7
    """
    __color__:int = None
    __date__:int = None
    __dmid__:int = None
    __pool__:int = None
    __stime__:float = None
    __mode__:int = None
    __text__:str = ''
    __uhash__:str = ''
    __size__:int = None
    __content__:str = ""
    data:list = []

    def __init__(self, data):
        if(data != ''):
            elements = cET.fromstring(data).findall("d")
            for ele in elements:
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
                tempdict["content"] = ele.text
                self.data.append(tempdict)

    def getDanmu(self, index=0):
        data = self.data[index]
        danmu = Danmaku("")
        danmu.__uhash__ = data['uhash']
        danmu.__date__ = data['date']
        danmu.__pool__ = data['pool']
        danmu.__size__ = data['size']
        danmu.__dmid__ = data['dmid']
        danmu.__mode__ = data['mode']
        danmu.__stime__ = data['stime']
        danmu.__color__ = data['color']
        danmu.__content__ = data['content']
        return danmu

    def getDanmuUser(self, content=''):
        '''获取弹幕发送着uid

        [description]

        Keyword Arguments:
            content {str} -- [description] (default: {''})

        Returns:
            [int] -- [uid]
        '''
        import binascii
        if content != '':
            for i in range(1, 100000000):
                if str(binascii.crc32(str(i).encode("utf-8"))) == self.__uhash__:
                    return i
        else:
            for ele in self.data:
                if(ele['content'] == content):
                    self.__uhash__ = ele['uhash']
                    return self.getDanmuUser()

    def getElement(self, index):
        return self.data[index]
