from flask import Flask,session,render_template,request
from DataBase import DB
from datetime import timedelta
import json,redis,os
from label_get_scenerys import moduleInterface as mf
from utils import logUtil

logger = logUtil.getLogger(0)
app = Flask(__name__)
# 静态模板自动刷新
# 开发用
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)  # 修改缓存时间，秒做单位
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=1)  # 修改回话存活时间，秒做单位
# 开启session
# app.config['SECRET_KEY'] = os.urandom(24)   # 从 0-9，a-z A-Z中随机选中24个字符串用做加密session的秘钥
# 使用redis
# app.config['SESSION_TYPE'] = 'redis'  # session类型为redis
# app.config['SESSION_PERMANENT'] = False  # 如果设置为True，则关闭浏览器session就失效。
# app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
# app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀
# app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port='6379')  # 用于连接redis的配置
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)
# session.permanent = True

# 设置主页面
@app.route('/')
@app.route('/index')
def index():
    operation = DB.operateDB()
    results = operation.sreachSceneryAndPostion()
    num = len(results)
    json_list = []
    for i in range(num):
        json_dict = {}
        json_dict['scenery_name'] = results[i][0]
        json_dict['longitude'] = results[i][1]
        json_dict['latitude'] = results[i][2]
        if i < int(num / 3) + 1:
            json_dict['flag'] = '2'
        elif i < int(num / 3 * 2) + 1:
            json_dict['flag'] = '1'
        else:
            json_dict['flag'] = '0'
        json_list.append(json_dict)
    return render_template('index.html',result=json.dumps(json_list))

# 设置标枪选择页面
@app.route('/chooseLabel')
def choosePage():
    bigLabels = ['动物', '景色', '历史', '特殊']
    smallLabelss = [['海鸥', '老虎', '螃蟹', '鳄鱼'],['大海', '公园', '树木', '山顶'],['博物馆', '抗日', '监狱', '纪念馆'],['教育', '雕塑', '海鲜', '健身']]
    return render_template('chooseLabel.html',bigLabels=bigLabels, smallLabelss=smallLabelss)

@app.route('/getLabel',methods=["post"])
def getLabel():
    labels = request.form.getlist("labels[]") # 由于返回什么就写什么
    # 调用标签找景点的模块
    results = mf.main(labels)
    json_list = []
    if len(results) != 0:
        operation = DB.operateDB()
        for result in results:
            json_dict = {}
            json_dict['scenery_name'] = result[0]
            r = operation.sreachPostion(json_dict['scenery_name'])
            if len(r) > 1:
                logger.warning('该景点有两个以上的经纬度，先返回一个')
            json_dict['longitude'] = r[0][0]
            json_dict['latitude'] = r[0][1]
            json_list.append(json_dict)
    return json.dumps(json_list) # 要有返回值

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.run(debug=True)