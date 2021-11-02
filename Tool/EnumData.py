class EnumData:
    # 枚举
    __value: str = ""
    # 所属枚举
    __enum: str = ""  
    # int值
    __index: int = 0
    # 注释
    __des: str = ""
    def __init__(self, value, enum, index, des) -> None:
        self.__value = value
        self.__enum = enum
        if type(index) != int:
            self.__index = int(index)
    
    def GetValue(self) -> str:
        return self.__value

    def GetValueStr(self) -> str:
        return str(self.__value)

    def GetEnum(self) -> str:
        return self.__enum

    def GetInt(self) -> int:
        return int(self.__index)

    def GetIntStr(self) -> int:
        return str(int(self.__index))

    def GetDes(self) -> int:
        return str(self.__des)


    

    