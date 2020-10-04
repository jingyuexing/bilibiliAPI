# BiliBili API

详细API可参见[API](data/API.json)
 BiliBili.py 则是具体发起请求方法

 多数的BilibiliAPI项目由于年久失修,所以有了写这个项目想法

 ![](https://img.shields.io/badge/language-python-blue.svg)
 ![](https://img.shields.io/badge/API-bilibili-fb7299.svg)
## API
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

* 获取文章信息

```py
getArticleInfo(articleID=0)
```

* 获取在线人数

```py
getOnlineNumber()
```

* 获取

```py
getUserInfoCard(userID)
```

* 发送信息(聊天)

```py
sendMsg(yourID, elseID, content='')
```

* 视频是否投过币

```py
isCoins(avID=None, bvID="")
```

* 视频是否收藏过

```py
isFavorite(avID=None, bvID="")
```

```py
vedioTagDelete(AID=0, tagID=0)
```

```py
getDanmuku(cid: int=None)
```

Vedio 类
```py
Vedio(vedioID='')

# method:
# 类当中的方法
getVedio(qn=0) #获取视频真实链接
getUser() # 获取视频作者信息
getDamku() #获取视频弹幕
sendDamku(color: str = '#ffffff', fontsize: int = 25, mode: int = 1, pool: int = 1, content: str = '') #发送弹幕
isCoins() #是否投币
isFavorite() #是否收藏
isLike()  #是否点赞
pageList() # 视频分页信息

```


User类
```
User{
    mid:  #用户id
    name: #昵称
    sex: #性别
    face: #头像
    birthday: #生日
    rank: #排序
    level: #等级
    vip: #是否是VIP
}
```

## LICENSE

MIT


