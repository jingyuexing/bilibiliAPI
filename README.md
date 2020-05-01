# BiliBili API

详细API可参见[API](data/API.json)
 BiliBili.py 则是具体发起请求方法

 多数的BilibiliAPI项目由于年久失修,所以有了写这个项目想法

# API
---

* 获取排行榜视频列表

```py
getRank(rankID:int,day:int,typer:int,arc_type:int)
```

* 获取用户信息

```py
getUserInfor(userid:int):
```

* 获取粉丝列表

```py
getFanList(mid:int, pageNumber:int, limit:int)
```

* 获取用户的视频列表

```py
getUserVedioList(userMID:int,limit:int,tagID:int,pageNumber:int,order:str)
```

* 获取历史弹幕

```py
getHistoryMsg(tp:int,oid:int,date:date):
```

* 获取视频的分享数、点赞数、硬币数、播放数等数据

```py
getVedioStat(aid:int)
```

* 获取视频的详细信息

```py
getVedioInfo(bvid:int,avid:int)
```

* 上传图片

```py
uploadImage(img:str,imgType:str)
```

* 获取直播房间信息

```py
getRoomInfo(img:str,imgType:str)
```

* 获取登陆链接

```py
getLoginUrl()
```

* 获取粉丝列表(如果登陆了则可以查看全部粉丝)

```py
getFollowsList(userID:int,limit:int,pageNumber:int)
```

* 获取小黑屋内的用户列表

```py
getBlackList(btype:None,otype:int,pn:int)
```

* 获取小黑屋内的用户的详情

```py
getBlockedInfo(userID:int)
```


#LICENSE
MIT


