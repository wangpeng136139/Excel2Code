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
import ColorHelper
import CommonType
from CommonType import VariableType;
from CommonType import CodeType;


class ConfigExcelData:
    def __init__(self, value, valueName, type, mark, isTitle) -> None:
        self.m_enum = "";
        self.m_value = value
        self.m_typeStr = type;
        self.m_typeStr  = self.m_typeStr.replace(" ","");
        self.m_valueType = CommonType.GetStrToType(self.m_typeStr);
        self.m_mark = mark
        mainIndex = valueName.find("(FirstKey)")
        secondIndex = valueName.find("(SecondKey)")
        self.m_bMainKey = False;
        self.m_bSecondKey = False;    
        if mainIndex > -1:
            self.m_bMainKey = True
            valueName = valueName.replace("(FirstKey)", "")
        if secondIndex > -1:
            self.m_bSecondKey = True    
            valueName = valueName.replace("(SecondKey)", "")
        self.m_valueName = valueName;
        if not isTitle:
            self.TypeToValue()
       
        if self.m_typeStr.find("enum") > -1:
                self.m_enum = (self.m_typeStr.split('.')[1])


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


    def TypeIsInt(self):
        return VariableType.INT16 == self.m_valueType or VariableType.INT32 == self.m_valueType  or VariableType.INT64 == self.m_valueType or VariableType.UINT16 == self.m_valueType or VariableType.UINT32 == self.m_valueType  or VariableType.UINT64 == self.m_valueType;
    
    def TypeIsFloat(self):
        return VariableType.FLOAT == self.m_valueType or VariableType.DOUBLE == self.m_valueType;

    def TypeToValue(self):
        value = str(self.m_value);
        if self.TypeIsInt() == True:
           value = self.StrToInt(value)
        elif VariableType.BOOL == self.m_valueType:
            if len(value) < 1:
                value = False
            else:
                value = bool(value)
        elif self.TypeIsFloat() == True:
            if len(value) < 1:
                value = 0
            else:
                value = float(value)
        elif VariableType.ENUM == self.m_valueType:
            list = value.split(".")
            if len(list) < 2:
                ColorHelper.printRed("value is error:" + value)
                exit()
            value = EnumUtils.GetIndex(list[0], list[1])
            value = int(value)
        self.m_value = value
        
    def GetMark(self) -> str:
        return  self.m_mark;

    def IsMainKey(self):
        return self.m_bMainKey

    def IsSecondKey(self):
        return self.m_bSecondKey

    def GetBytes(self):
        value = self.m_value
        binValue = ""
        if self.m_valueType == VariableType.INT16:
            binValue = struct.pack("h", value)
        if self.m_valueType == VariableType.INT32:
            binValue = struct.pack("i", value)
        elif self.m_valueType == VariableType.INT64:
            binValue = struct.pack("l", value)
        elif self.m_valueType == VariableType.UINT16:
            binValue = struct.pack("H", value)
        elif self.m_valueType == VariableType.UINT32:
            binValue = struct.pack("I", value)
        elif self.m_valueType == VariableType.UINT64:
            binValue = struct.pack("L", value)
        elif self.m_valueType == VariableType.BOOL:
            binValue = struct.pack("?", value)
        elif self.m_valueType == VariableType.FLOAT:
            binValue = struct.pack("f", value)
        elif self.m_valueType == VariableType.DOUBLE:
            binValue = struct.pack("d", value)
        elif self.m_valueType == VariableType.ENUM:
            binValue = struct.pack("i", value)
        elif self.m_valueType == VariableType.STRING:
            value = value.encode("utf-8")
            binValue = struct.pack("i%ds" % len(value), len(value), value)
        else:
            value = value.encode("utf-8")
            binValue = struct.pack("i%ds" % len(value), len(value), value)
        return binValue


    def GetValue(self):
        return self.m_value

    def IsEnum(self) -> bool:
        if self.m_typeStr.find("enum") > -1:
            return True
        return False

    def GetVariableType(self,codeType:CodeType):
        if codeType == CodeType.CS:
            if self.IsEnum():
                return self.m_enum;
            return CommonType.GetTypeToStr(self.m_valueType,codeType);
        elif codeType == CodeType.CPP:
            if self.IsEnum():
                return self.m_enum;
            return CommonType.GetTypeToStr(self.m_valueType,codeType);


    def GetVariable(self,codeType:CodeType):
        if codeType == CodeType.CS:
            if self.IsEnum():
                return "private "+self.m_enum+" m_" + self.m_valueName + ";"
            return "private "+CommonType.GetTypeToStr(self.m_valueType,codeType)+" m_" + self.m_valueName + ";"
        elif codeType == CodeType.CPP:
            if self.IsEnum():
                return self.m_enum+" m_" + self.m_valueName + ";"
            return CommonType.GetTypeToStr(self.m_valueType,codeType)+" m_" + self.m_valueName + ";"

    def GetGetVariableRead(self,codeType:CodeType):
        if codeType == CodeType.CS:
            if self.IsEnum():
                return "public "+self.m_enum+" " + self.m_valueName + " => " + " m_" + self.m_valueName + ";"
            return "public "+CommonType.GetTypeToStr(self.m_valueType,codeType)+" " + self.m_valueName + " => " + " m_" + self.m_valueName + ";"
        elif codeType == CodeType.CPP:
            if self.IsEnum():
                return self.m_enum +" Get" + self.m_valueName + "(){ return m_" + self.m_valueName + ";};"
            return CommonType.GetTypeToStr(self.m_valueType,codeType)+" Get" + self.m_valueName + "(){ return m_" + self.m_valueName + ";};"

    def GetTypeToRead(self,codeType:CodeType):
        readContent =  CommonType.GetTypeToRead(self.m_valueType,codeType,self.m_enum);
        return " m_" + self.m_valueName + " = " + readContent;
