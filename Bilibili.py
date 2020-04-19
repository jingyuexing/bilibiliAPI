# -*- coding: utf-8 -*-
# @Author: Moid
# @Date:   2020-04-19 18:30:33
# @Last Modified by:   Jingyuexing
# @Last Modified time: 2020-04-19 20:12:00

import json
import urllib3

http = urllib3.PoolManager()
head = {
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
with open("data/API.json", "r", encoding='utf-8') as file:
    api = json.loads(file.read())
    file.close()

def requests(method='',url='',parma={}):
  '''发起请求
  
  [description]
  
  Keyword Arguments:
    method {str} -- 方式(POST|GET|DELETE) (default: {''})
    url {str} -- 链接 (default: {''})
    parma {dict} -- 参数 (default: {{}})
  
  Returns:
    {dict} -- 返回数据
  '''
  req = http.request(method=method,url=url,fields=parma,headers=head)
  if req.status == 200:
    return json.loads(req.data,encoding='utf-8')

def getRank(rankID=0,day=3,typer=1,arc_type=0):
    config = api[0]
    method = config['method']
    url = config['link']
    parma ={
      "rid":rankID,
      'day':day,
      'type':typer,
      'arc_type':arc_type,
      'jsonp':'jsonp'
    }
    return requests(method=method,url=url,fields=parma)

def getUserInfor(userid=0):
    config:dict = api[2]
    method = config["method"]
    url = config["link"]
    parma = {
        "mid": str(userid),
        "jsonp": "jsonp"
    }
    return requests(method=method,url=url,fields=parma)


def getFanList(mid=0, pageNumber=1, limit=20):
    '''获取粉丝列表

    [description]

    Keyword Arguments:
      mid {number} -- 用户id (default: {0})
      pageNumber {number} -- 列表页数 (default: {1})
      limit {number} -- 信息条数 (default: {20})

    Returns:
      {dict} -- 返回的数据
    '''
    config:dict = api[3]
    method = config['method']
    url = config['link']
    parma = {
        "vmid": mid,
        "pn": pageNumber,
        "ps": limit,
        "order": "desc",
        "jsonp": "jsonp"
    }
    return requests(method=method,url=url,fields=parma)

