
---
**将数据库的评论分析后展示排名**
---

入口函数：showFlask.py

包说明：

DataBase：连接数据库

static：存放一些静态资源，如：css，img，js等等

templates：存放页面的地方

logs：存放日志

utils：工具

---
**技术栈**
---

python(python3.7 x64)：有一定的python基础，https://www.runoob.com/python/python-tutorial.html

Flask：是一个 web 框架。也就是说 Flask 为你提供工具，库和技术来允许你构建一个 web 应用程序。https://blog.csdn.net/mookee_cc/article/details/52947332

---
**包的层次结构**
---

make_word_cloud ---- DataBase ---- DB.py
                  
                  ---- static ---- css ----
                                
                              ---- js ---- jquery.min.js
                              
                                      ---- mapjson.js
                              
                              ---- img ---- 0.png
                              
                                       ---- 1.png
                                       
                                       ---- 2.png
                  
                  ---- templates ---- index.html
                   
                  ---- logs ---- DB_log.log
                            
                  ---- utils ---- logUtil.py
                  
                  ---- main.py
                  
                  ----README.md
       
---
**依赖包**
---

flask： 用于分词

pymysql：用于连接数据库
