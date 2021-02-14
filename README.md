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


* 获取粉丝列表 `已经移入User`

```py
getFanList(mid:int, pageNumber:int, limit:int)
```

* 获取用户的视频列表 `已经移入User`

```py
getUserVideoList(userMID:int,limit:int,tagID:int,pageNumber:int,order:str)
```

* 获取历史弹幕

```py
getHistoryMsg(tp:int,oid:int,date:date):
```

* 获取视频的分享数、点赞数、硬币数、播放数等数据

```py
getVideoStat(aid:int)
```

* 获取视频的详细信息

```py
getVideoInfo(bvid:int,avid:int)
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
* 删除视频上的一个标签
```py
videoTagDelete(AID=0, tagID=0)
```
* 获取弹幕
```py
getDanmuku(cid:int=None)
```
* 获取视频评论(在`Video`当中)
```py
getReply(self, pageNumber=1, typeis=1, sort=2)
```

## Cookies 类
```py

setCookies(key, value)
getCookies(key)
getCookiesAll()
parserCookies(cookies='')
toString()
```

## Video 类
|类型|名称|意义|
|:----:|:----|----:|
|属性|avid|av号|
|属性|bvid|bv号|
|属性|cover|视频封面|
|属性|tagID|标签id|
|属性|title|视频标题|
|属性|oid|视频分p号|
|属性|tag|标签|
|属性|owner|视频拥有者|
|属性|createTime|发布时间|
|属性|coin|硬币数|
|属性|like|点赞数|
|属性|favorite|收藏数|
|属性|share|分享数|
|属性|view|观看数|
|属性|reply|评论数|
|方法|`getVideo()`|获取视频真实链接|
|方法|`getUser()`|获取视频作者信息|
|方法|`getDamku()`|获取弹幕|
|方法|`sendDamku()`|发送弹幕|
|方法|`sendDamku()`|发送弹幕|
|方法|`isCoins()`|是否投币|
|方法|`isFavorite()`|是否收藏|
|方法|`isLike()`|是否点赞|
|方法|`pageList()`|视频分P列表|
|方法|`getReply()`|视频评论|


## Article类
|类型|名称|意义|
|:----:|:----|----:|
|属性|like|点赞数|
|属性|coin|硬币数|
|属性|read|阅读数|
|属性|reply|回复数|
|属性|share|分享数|
|属性|uid|作者uid|
|方法|`getArticleInfo()`|获取专栏文章信息|
|方法|`getUserInfo()`|获取专栏作者信息|
|方法|`getArticleList()`|获取专栏全部文章信息|

## task

- ☐ 增加发布接口(视频、音频)
- ☐ 增加爬虫搜索


## LICENSE

[MIT](LICENSE)


