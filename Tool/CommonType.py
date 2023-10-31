from enum import Enum
class VariableType(Enum):
    INT16  = 0
    INT32  = 1
    INT64  = 2
    UINT16  = 3
    UINT32  = 4
    UINT64  = 5
    STRING = 6
    FLOAT = 7
    DOUBLE = 8
    BOOL = 9
    ENUM = 10

class CodeType(Enum):
    CS = 0
    CPP = 1
    JAVA = 2
    LUA = 3


def GetStrToType(codeStr:str):
    codeStr = codeStr.lower();
    if codeStr == "int16" or codeStr == "short":
        return VariableType.INT16;
    
    if codeStr == "int32" or  codeStr == "int":
        return VariableType.INT32;

    if codeStr == "int64" or  codeStr == "long":
        return VariableType.INT64;


    if codeStr == "uint16" or  codeStr == "unsigned int16":
        return VariableType.UINT16;


    if codeStr == "uint32" or  codeStr == "unsigned int":
        return VariableType.UINT32;


    if codeStr == "uint64" or  codeStr == "unsigned long":
        return VariableType.UINT64;

    if codeStr == "string":
        return VariableType.STRING;

    if codeStr == "float":
        return VariableType.FLOAT;

    if codeStr == "double":
        return VariableType.DOUBLE;
    
    if codeStr == "bool":
        return VariableType.DOUBLE;

    if codeStr.find("enum.") > -1:
        return VariableType.ENUM;



def GetTypeToRead(etype:VariableType,codeType:CodeType,enumName:str):
    if etype == VariableType.INT16:
        if codeType == CodeType.CS:
            return "bin.ReadInt16();";
        elif codeType == CodeType.CPP:
            return "bin->ReadInt16();";
           

    if etype == VariableType.INT32:
        if codeType == CodeType.CS:
            return "bin.ReadInt32();";
        elif codeType == CodeType.CPP:
            return "bin->ReadInt32();";


    if etype == VariableType.INT64:
        if codeType == CodeType.CS:
            return "bin.ReadInt64();";
        elif codeType == CodeType.CPP:
            return "bin->ReadInt64();";

    if etype == VariableType.UINT16:
        if codeType == CodeType.CS:
            return "bin.ReadUInt16();";
        elif codeType == CodeType.CPP:
            return "bin->ReadUInt16();";

    if etype == VariableType.UINT32:
        if codeType == CodeType.CS:
            return "bin.ReadString();";
        elif codeType == CodeType.CPP:
            return "bin->ReadString();";


    if etype == VariableType.UINT64:
        if codeType == CodeType.CS:
            return "bin.ReadUInt64();";
        elif codeType == CodeType.CPP:
            return "bin->ReadUInt64();";

    if etype == VariableType.STRING:
        if codeType == CodeType.CS:
            return "bin.ReadString();";
        elif codeType == CodeType.CPP:
            return "bin->ReadString();";


    if etype == VariableType.FLOAT:
        if codeType == CodeType.CS:
            return "bin.ReadFloat();";
        elif codeType == CodeType.CPP:
            return "bin->ReadFloat();";

    if etype == VariableType.DOUBLE:
        if codeType == CodeType.CS:
            return "bin.ReadDouble();";
        elif codeType == CodeType.CPP:
            return "bin->ReadDouble();";


    if etype == VariableType.BOOL:
        if codeType == CodeType.CS:
            return "bin.ReadBoolean();";
        elif codeType == CodeType.CPP:
            return "bin->ReadBoolean();";


    if etype == VariableType.ENUM:
        if codeType == CodeType.CS:
            return "("+enumName + ")bin.ReadInt32();";
        elif codeType == CodeType.CPP:
            return "("+enumName + ")bin->ReadInt32();";
    return "GetTypeToRead error";
        
 
def GetTypeToStr(etype:VariableType,codeType:CodeType):
    if etype == VariableType.INT16:
        if codeType == CodeType.CS:
            return "Int16";
        elif codeType == CodeType.CPP:
            return "short";

    if etype == VariableType.INT32:
        if codeType == CodeType.CS:
            return "Int32";
        elif codeType == CodeType.CPP:
            return "int";


    if etype == VariableType.INT64:
        if codeType == CodeType.CS:
            return "Int64";
        elif codeType == CodeType.CPP:
            return "long";

    if etype == VariableType.UINT16:
        if codeType == CodeType.CS:
            return "UInt16";
        elif codeType == CodeType.CPP:
            return "unsigned short";

    if etype == VariableType.UINT32:
        if codeType == CodeType.CS:
            return "UInt32";
        elif codeType == CodeType.CPP:
            return "unsigned int";


    if etype == VariableType.UINT64:
        if codeType == CodeType.CS:
            return "UInt64";
        elif codeType == CodeType.CPP:
            return "unsigned long";


    if etype == VariableType.STRING:
        if codeType == CodeType.CS:
            return "string";
        elif codeType == CodeType.CPP:
            return "std::string";


    if etype == VariableType.FLOAT:
        if codeType == CodeType.CS:
            return "float";
        elif codeType == CodeType.CPP:
            return "float";

    if etype == VariableType.DOUBLE:
        if codeType == CodeType.CS:
            return "double";
        elif codeType == CodeType.CPP:
            return "double";


    if etype == VariableType.BOOL:
        if codeType == CodeType.CS:
            return "bool";
        elif codeType == CodeType.CPP:
            return "bool";


    if etype == VariableType.ENUM:
       return "enum";

    return "GetTypeToStr error";