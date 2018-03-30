__author__ = 'lsz'
#程序向目标uil发送get请求
import requests
import re
url="http://www.jingcaiyuedu.com/book/183935.html"
response = requests.get(url)
response.encoding ="utf-8"#编码方式
html=response.text#网页源码储存
#小说名字
title = re.findall(r' <meta property="og:title" content="(.*?)"/>',html)[0]
#新建文本保存小说
fb = open('%s.txt' % title,'w',encoding ="utf-8")
#新建文本保存小说

#获取每一章节
dl = re.findall(r'<dl id="list">.*?</dl>',html,re.S)[0]#正则表达式 0：列表
chapter_info_list = re.findall(r'href="(.*?)">(.*?)<',dl)# i*? =匹配 list 格式

#循环
for chapter_info in chapter_info_list:
    chapter_title = chapter_info[1]
    chapter_url = chapter_info[0]
     #前两句等价于 这句 chapter_url,chapter_title = chapter_info
    chapter_url="http://www.jingcaiyuedu.com%s" % chapter_url#补完整章节url
    #下载章节内容
    chapter_response=requests.get(chapter_url) #进入章节url
    chapter_response.encoding = "utf-8"
    chapter_html = chapter_response.text# 获取章节源码

    #提取源码的 章节内容
    chapter_content = re.findall(r'<script>a1\(\);</script>(.*?)<script>a2\(\);</script>', chapter_html,re.S)[0]#括号要转义一下
    #清洗数据
    chapter_content = chapter_content.replace(' ','')
    chapter_content = chapter_content.replace('<br/> ','')
    chapter_content = chapter_content.replace('<br>','')
    chapter_content = chapter_content.replace(':<br/><br/>','')
    chapter_content = chapter_content.replace('”<br/><br/>','')
    chapter_content = chapter_content.replace('（.vodtw.）<br/><br/>','')
    chapter_content = chapter_content.replace('<br/><br/>','')
    #保存章节内容
    fb.write(chapter_title)
    fb.write(chapter_content)
    fb.write('\n')





