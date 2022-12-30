## Usage

没啥技术含量  就是利用cookie post个数据包。

首先到土司网站利用bp进行签到抓包，同时获取个人Cookie字段和data。

Cookie示例：

```
smile=xxx;
*****
UTH_sid=xxx
```

data示例：

```
formhash=xxx&signsubmit=apply
```

分别填入脚本21行Cookie和39行data。

pushplus为可选，如果不想使用注释掉就好，推送是为了后面定时任务每天推送。

运行脚本，根据status结果判断签到是否成功。

![image-20221230110323895](https://zebpic-1301715962.cos.ap-nanjing.myqcloud.com/blog/image-20221230110323895.png)

定时任务效果：

![](https://zebpic-1301715962.cos.ap-nanjing.myqcloud.com/blog/202212301105936.png)

土司应该是出于某种考虑，Cookie字段可以重复使用，不需要担心登出失效。

但是时效大概是四五十天？？具体时间不甚清楚。

crontab运行了两个多月了，中间断过一次。总体来说还是可以接受。
