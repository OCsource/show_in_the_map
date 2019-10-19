from DataBase import DB

# 通过标签找到对应的景点
# 参数：标签列表
# 返回：成功景点字典 key（包括景点名称，经度纬度）value：出现的数量，失败false
def getScenery(labelList):
    dictScenery = {}
    sceneryData = []
    operation = DB.operateDB()
    for label in labelList:
        result = operation.sreachSceneryByLabel(label)
        for r in result:
            if r[0] not in sceneryData:
                sceneryData.append(r[0])
            dictScenery[r[0]] = dictScenery.get(r[0], 0) + 1
    return sceneryData, dictScenery