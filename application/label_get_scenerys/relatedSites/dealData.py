from label_get_scenerys.relatedSites import Apriori as ap
from label_get_scenerys.relatedSites import matchingFunc as mf
from DataBase import DB

# 获取数据（不同的存储结构可以有不同的实现）
# 参数：文本路径没有默认为“0”
# 返回两个值，一个为字典列表key:为名称value:为统计数，另一个是一个存储原始数据的二维数组
def getOriginalData(city_number):
    operation = DB.operateDB()
    originalDic = {}
    originalData = []
    tempList = []
    results = operation.getAllLink()
    sceneryRS = operation.sreachSceneryName()
    sceneryList = []
    for scenery in sceneryRS:
        sceneryList.append(scenery[0])
    i = 0
    for result in results:
        if result[1] not in sceneryList: continue
        if i != result[0]:
            i = result[0]
            if len(tempList) > 1: originalData.append(tempList)
            tempList = []
        tempList.append(result[1])
        if result[1] not in originalDic:
            originalDic[result[1]] = 1
        else:
            originalDic[result[1]] += 1
    originalData.append(tempList)
    ListDic = sorted(originalDic.items(),key = lambda x:x[1],reverse = True)
    return ListDic, originalData

# 统计候选项集与频繁项集的个数
# 参数：C候选项集，L频繁项集，originalData原始事物数据
# 返回两个字典
def countCL(C, L, originalData):
    CDic = {}
    LDic = {}
    # 统计候选集元素的个数
    for tempC1 in C:
        for tempC2 in tempC1:
            tempC2 = set(tempC2)
            for tempO in originalData:
                if tempC2.issubset(tempO):
                    CDic[",".join(tempC2)] = CDic.get(",".join(tempC2), 0) + 1
    # 统计频繁项集元素的个数
    for tempL1 in L:
        for tempL2 in tempL1:
            tempL2 = set(tempL2)
            for tempO in originalData:
                if tempL2.issubset(tempO):
                    LDic[",".join(tempL2)] = LDic.get(",".join(tempL2), 0) + 1
    return CDic, LDic

# 规范化最终关联规则
# 参数：关联规则数据（里面元素是元组）
# 返回关联规则字典
def formatRule(resultList):
    resultDic = {}
    for result in resultList:
        resultDic[",".join(list(result[0])) + "=>" + ",".join(list(result[1]))] = result[2]
    return resultDic

# 调用Apriori算法+ adapARM（最小支持度与最小置信度自适应算法）(用于数据量比较大，且每个数据项的比例非常小的场景)
# 参数：txtPath文本地址
# 返回三个列表：候选项集，频繁项集，结果集
def getResultByARM(city_number):
    ListDic, originalData = getOriginalData(city_number)
    minSupport = int(mf.main(ListDic))  # 是个大于一的整数
    C, L, supportData = ap.apriori(originalData, minSupport, 1)
    sortSupportData = sorted(supportData.items(),key = lambda x:x[1],reverse = True)
    minConfidence = mf.main(sortSupportData, flag=1)
    resultList = ap.getRule(L, minConfidence, supportData)
    CDic, LDic = countCL(C, L, originalData)
    resultDic = formatRule(resultList)
    return [CDic, LDic, resultDic]

if __name__ == '__main__':
    CDic, LDic, resultDic = getResultByARM(86)
    print(CDic)
    print(LDic)
    print(resultDic)
