from EnumData import EnumData


__enumDic = {}


def AddEnum(enum: str, value: str, index: int) -> bool:
    if len(enum) < 1 or len(value) < 1:
        return False
    item = EnumData(value, enum, index)
    dicList = []
    if enum in __enumDic:
        dicList = __enumDic[enum]
    dicList.append(item)
    __enumDic[enum] = dicList
    return True


def GetIndex(enum: str, value: str) -> int:
    dicList = []
    if enum in __enumDic:
        dicList = __enumDic[enum]
    for item in dicList:
        if item.value == value:
            return item.value
    return -1


def ClearEnum() -> None:
    enumDic = {}



    

