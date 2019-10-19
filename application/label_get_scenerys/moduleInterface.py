from label_get_scenerys.mappingScenery import findScenery
from label_get_scenerys.relatedSites import dealData

# 通过标签列表返回景点以及关联经典
# 参数：标签列表
# 返回：景点列表
def main(labelList):
    sceneryData, dictScenery = findScenery.getScenery(labelList)
    CDic, LDic, resultDic = dealData.getResultByARM('86')
    for k in resultDic:
        front = k.split('=>')[0]
        after = k.split('=>')[1]
        tempList = front.split(',')
        if tempList in sceneryData:
            dictScenery[after] = dictScenery.get(after, 0) + 1
    sortScenery = sorted(dictScenery.items(), key = lambda x:x[1],reverse = True)
    return sortScenery

if __name__ == '__main__':
    labelList = ['鳄鱼']
    sortScenery = main(labelList)
    print(sortScenery)