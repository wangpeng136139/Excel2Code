
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
import struct


class ExcelData:
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

    def __init__(self, value, type, valueName, mark) -> None:
        self.m_value = value
        self.m_type = type
        self.m_valueName = valueName
        self.m_mark = mark
        mainIndex = valueName.find("(Main)")
        secondIndex = valueName.find("(Second)")
        if mainIndex > -1:
            self.m_bMainKey = True
        if secondIndex > -1:
            self.m_bSecondKey = True
        self.TypeToValue()
        
    def TypeToValue(self):
        value = self.m_value
        type = self.m_type
        if type == "int":
            value = int(value)
        elif type == "bool":
            value = bool(value)
        elif type == "float":
            value = float(value)
        self.m_value = value
        
    def IsMainKey(self):
        return self.m_bMainKey

    def IsSecondKey(self):
        return self.m_bSecondKey

    def GetBytes(self):
        value = self.m_value
        binValue = ""
        if type == "int":
            binValue = struct.pack("i", value)
        elif type == "bool":
            binValue = struct.pack("?", value)
        elif type == "float":
            binValue = struct.pack("f", value)
        else: 
            binValue = struct.pack("s", value)
        return binValue

    def GetValue(self):
        return self.m_value
        
    