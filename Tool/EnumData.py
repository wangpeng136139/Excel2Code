class EnumData:
    # 枚举
    __value: str = ""
    # 所属枚举
    __enum: str = ""  
    # int值
    __index: int = 0
    
    def __init__(self, value, enum, index) -> None:
        self.__value = value
        self.__enum = enum
        self.__index = index
    
    def GetValue(self) -> str:
        return self.__value

    def GetEnum(self) -> str:
        return self.__enum

    def GetInt(self) -> int:
        return self.__index

    

    