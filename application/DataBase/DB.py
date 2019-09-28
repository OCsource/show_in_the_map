import pymysql
from utils import logUtil

logger = logUtil.getLogger(0)

class operateDB:
    def __init__(self):
        self.__dbName = 'qunarNew'
        self.__user = 'root'
        self.__password = '123456'
        self.__host = 'localhost'
        self.__char = 'utf8'

    # 查找所有有权重值的景点名称，景点经纬度，景点权重
    # 返回：成功上面的信息，失败
    def sreachSceneryAndPostion(self):
        db = pymysql.connect(host=self.__host, user=self.__user, password=self.__password, db=self.__dbName, charset=self.__char)
        cur = db.cursor()
        sql = "SELECT scenery_table.scenery_name,scenery_table.longitude,scenery_table.latitude,scenery_weight.weight FROM scenery_table,scenery_weight WHERE scenery_weight.scenery_number = scenery_table.scenery_number order by scenery_weight.weight DESC"
        try:
            cur.execute(sql)
            result = cur.fetchall()
            return result
        except:
            db.rollback()
            logger.error('查找数据库失败')
            return False
        finally:
            db.close()

    # 查找相应景点的经纬度
    # 参数：景点名
    # 返回：成功景点经纬度信息，失败false
    def sreachPostion(self, scenery_name):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cur = db.cursor()
        sql = "SELECT longitude,latitude FROM scenery_table WHERE scenery_name = '%s';"%(scenery_name)
        try:
            cur.execute(sql)
            result = cur.fetchall()
            return result
        except:
            db.rollback()
            logger.error('查找数据库失败')
            return False
        finally:
            db.close()
