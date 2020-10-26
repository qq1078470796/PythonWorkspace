"""图数据的基类"""
class BaseData:
    id = 0
    hobbys = []

    def __init__(self,id,hobbys=[]):
        self.id = id
        for hobby in hobbys:
           self.hobbys.append(hobby)
