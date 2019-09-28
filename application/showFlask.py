from flask import Flask
from flask import render_template
from DataBase import DB
import json
app = Flask(__name__)

# 设置主页面
@app.route('/')
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

if __name__ == '__main__':
    app.run()