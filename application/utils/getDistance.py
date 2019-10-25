from math import sin, asin, cos, radians, fabs, sqrt

EARTH_RADIUS=6371   # 地球平均半径，6371km

def hav(theta):
    s = sin(theta / 2)
    return s * s

# 通过经纬度得到景点直线间的距离
# 参数：两个景点的经纬度
# 返回：景点间的距离
def twoPointDistance(lat0, lng0, lat1, lng1):
    lat0, lng0, lat1, lng1 = float(lat0), float(lng0), float(lat1), float(lng1)
    # "用haversine公式计算球面两点间的距离。"
    # 经纬度转换成弧度
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lng0 = radians(lng0)
    lng1 = radians(lng1)

    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))

    return distance
