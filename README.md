# BiliBili API

详细API可参见[API](data/API.json)
 BiliBili.py 则是具体发起请求方法

 多数的BilibiliAPI项目由于年久失修,所以有了写这个项目想法

# API

```py
getRank(rankID:int,day:int,typer:int,arc_type:int)
```
```py
getUserInfor(userid:int):
```
```py
getFanList(mid:int, pageNumber:int, limit:int)
```
```py
getFanList(mid:int, pageNumber:int, limit:int)
```
```py
getUserVedioList(userMID:int,limit:int,tagID:int,pageNumber:int,order:str)
```
```py
getHistoryMsg(tp:int,oid:int,date:date):
```
```py
getStat(aid:int)
```
```py
getVedioInfo(bvid:int,avid:int)
```


#LICENSE
MIT


