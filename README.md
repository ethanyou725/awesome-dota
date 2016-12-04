# awesome-dota
## Python requests 爬虫脚本抓起dota2max的数据
### 主要的数据有英雄头像(包括url),胜率,使用次数
#### 抓取的数据保存到mongodb,后来改为保存为csv文件,每天一个文件
#### 网站构建基于flask
```
if __name__ =="__main__":
    app.config.update(
        DEBUG=True,
        TEMPLATES_AUTO_RELOAD=True,
    )
    extra_dir = os.path.dirname(os.path.abspath("."))
    extra_files=[]


    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = os.path.join(dirname, filename)
            if os.path.isfile(filename):
                extra_files.append(filename)
    app.run(extra_files=extra_files)
```
###### 可以使jinjia2模版实时刷新(stackoverflow)
###### 前端ajax和后端交互
###### 图表采用highcharts
###### 在windows下可能跑步起来,因为编码问题?暂时没搞清楚
###### 出场次数的数据曲线这样子,因为在曲线低谷的几天是下午五六点抓的数据,后面基本在晚上23点左右抓的数据
###### 爬虫脚本可以每天定时执行
###### 代码有待优化
####目录说明
* 1 data 数据文件csv目录
* 2 scripts 爬虫脚本目录,和处理数据脚本目录
* 3 showapp 主程序目录
* 4 static 静态资源目录
* 5 testapp 测试app目录
待优化,考虑用数据库存放数据
