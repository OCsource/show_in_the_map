---
**将数据库的评论分析后展示排名**
---

入口函数：showFlask.py

包说明：

DataBase：连接数据库

static：存放一些静态资源，如：css，img，js等等

label_get_scenerys：通过标签查找景点（模块）

mappingScenery：通过标签名找到景点

relatedSites：寻找关联景点

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
                  
                  ---- static ---- css ---- chooseLabel.css
                                
                              ---- js ---- jquery.min.js
                              
                                      ---- mapjson.js
                              
                              ---- img ---- 0.png
                              
                                       ---- 1.png
                                       
                                       ---- 2.png
                  
                  ---- templates ---- index.html
                  
                                 ---- chooseLabel.html
                   
                  ---- logs ---- DB_log.log
                            
                  ---- utils ---- logUtil.py
                  
                  ---- label_get_scenerys ---- mappingScenery ---- findScenery.py
                  
                                          ---- relatedSites ---- Apriori.py
                                          
                                                            ---- dealData.py
                                                            
                                                            ---- matvhing.py
                                          
                                          ---- moduleInterface.py        
                                          
                  ---- main.py
                  
                  ----README.md
       
---
**依赖包**
---

flask： python的Web框架

pymysql：用于连接数据库

---
**添加**
---
将模块五的标签查找景点功能整合了进来