# Type symbol	Type number	Python value
# XL_CELL_EMPTY	0	empty string ''
# XL_CELL_TEXT	1	a Unicode string
# XL_CELL_NUMBER	2	float
# XL_CELL_DATE	3	float
# XL_CELL_BOOLEAN	4	int; 1 means TRUE, 0 means FALSE
# XL_CELL_ERROR	5	int representing internal Excel codes; for a text representation, refer to the supplied dictionary error_text_from_code
# XL_CELL_BLANK	6	empty string ''. Note: this type will appear only when open_workbook(..., formatting_info=True) is used.


# x	pad byte	no value	 	 
# c	char	string of length 1	1	 
# b	signed char	integer	1	(3)
# B	unsigned char	integer	1	(3)
# ?	_Bool	bool	1	(1)
# h	short	integer	2	(3)
# H	unsigned short	integer	2	(3)
# i	int	integer	4	(3)
# I	unsigned int	integer	4	(3)
# l	long	integer	4	(3)
# L	unsigned long	integer	4	(3)
# q	long long	integer	8	(2), (3)
# Q	unsigned long long	integer	8	(2), (3)
# f	float	float	4	(4)
# d	double	float	8	(4)
# s	char[]	string	1	 
# p	char[]	string	 	 
# P	void *	integer	 	(5), (3)
from re import search
import struct
import EnumUtils


class ConfigExcelData:
    # 内容
    m_value: str 
    # 类型
    m_type: str
    # 变量名称
    m_valueName: str
    # 注释
    m_mark: str
    # 是否为主键
    m_bMainKey: bool = False
    # 是否为第二主键
    m_bSecondKey: bool = False
    # 所有枚举
    m_enum: str = ""

    def __init__(self, value, valueName, type, mark, isTitle) -> None:
        self.m_value = value
        self.m_type = type
        self.m_valueName = valueName
        self.m_mark = mark
        mainIndex = valueName.find("(Main)")
        secondIndex = valueName.find("(Second)")
        if mainIndex > -1:
            self.m_bMainKey = True
            valueName = valueName.replace("(Main)", "")
        if secondIndex > -1:
            self.m_bSecondKey = True    
            valueName = valueName.replace("(Second)", "")
        
        if not isTitle:
            self.TypeToValue()
       
        if self.m_type.find("enum") > -1:
                self.m_enum = (self.m_type.split('.')[1])


    def GetValueName(self):
        return self.m_valueName

    def StrToInt(self, strValue: str):    
        if len(strValue) < 1:
            return 0
        index = strValue.find(".") 
        if index > -1:
           strValue = strValue[0:index]

        if len(strValue) < 1:
            return 0
        
        return int(strValue)

    def TypeToValue(self):
        value = str(self.m_value)
        type = self.m_type
        if type == "int":
           value = self.StrToInt(value)
        elif type == "bool":
            if len(value) < 1:
                value = False
            else:
                value = bool(value)
        elif type == "long" or type == "int64_t" or type == "uint64_t":
            value = self.StrToInt(value)
        elif type == "short":
            value = self.StrToInt(value)
        elif type == "float":
            if len(value) < 1:
                value = 0
            else:
                value = float(value)
        elif type.find("enum") > -1:
            list = value.split(".")
            if len(list) < 2:
                print("value is error:" + value)
                exit()
            value = EnumUtils.GetIndex(list[0], list[1])
            value = int(value)
        self.m_value = value
        
    def GetMark(self) -> str:
        return "//" + self.GetMark()

    def IsMainKey(self):
        return self.m_bMainKey

    def IsSecondKey(self):
        return self.m_bSecondKey

    def GetBytes(self):
        value = self.m_value
        binValue = ""
        type = self.m_type
        if type == "int":
            binValue = struct.pack("i", value)
        elif type == "bool":
            binValue = struct.pack("?", value)
        elif type == "float":
            binValue = struct.pack("f", value)
        elif type.find("enum") > -1:
            binValue = struct.pack("i", value)
        elif type == "short":
            binValue = struct.pack("h", value)
        else:
            value = value.encode("utf-8")
            binValue = struct.pack("h%ds" % len(value), len(value), value)
        return binValue

    def GetCSType(self):
        return self.m_type

    def GetValue(self):
        return self.m_value

    def IsEnum(self) -> bool:
        if self.m_type.find("enum") > -1:
            return True
        return False

    def GetCSClassValue(self):
        if self.IsEnum():
             return "private "+self.m_enum+" m_" + self.m_valueName + ";"
        return "private "+self.m_type+" m_" + self.m_valueName + ";"

    def GetCSGetValue(self):
        if self.IsEnum():
            return "public "+self.m_enum+" " + self.m_valueName + " => " + " m_" + self.m_valueName + ";"
        return "public "+self.m_type+" " + self.m_valueName + " => " + " m_" + self.m_valueName + ";"

    def GetCSReadValue(self):
        content: str = ""
        type = self.m_type
        if type == "int":
            content = "pStream.ReadInt32();"
        elif type == "bool":
            content = "pStream.ReadBoolean();"
        elif type == "float":
            content = "pStream.ReadSingle();"
        elif type == "short":
            content = "pStream.ReadInt16();"
        elif type == "int64":
            content = "pStream.ReadLong();"
        elif type.find("enum") > -1:
            content = "(" + self.m_enum + ")pStream.ReadInt32();"
        elif type == "string":
            content = "ReadUTF8String(pStream);"
        else: 
            print("type is error:" + type)
            exit()
        return " m_" + self.m_valueName + " = " + content