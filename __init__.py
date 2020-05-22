# -*- coding: utf-8 -*-
# @Author: jingyuexing
# @Date:   2020-05-03 01:39:29
# @Last Modified by:   Jingyuexing
# @Last Modified time: 2020-05-20 21:14:23

from .Bilibili import *
from .damuku.parserDamuku import Danmaku

__doc__ ="""
this is a simple about Bilibili-API modules
"""
__package__ = [
    "Bilibili",
    "parserDamuku"
]

version="0.1"



if __name__ != '__main__':
    print("Power By Jingyuexing,this modules version is",version)