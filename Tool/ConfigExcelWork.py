from typing import Dict
from typing import List
from ConfigExcelData import ConfigExcelData
from ConfigExcelSheel import ConfigExcelSheel
from Content import Content
from BinWrite import BinWrite
import xlrd
import ExcelUtils
import os
import Derictory
import ColorHelper;
import sys;
from CommonType import VariableType;
from CommonType import CodeType;


class ConfigExcelWork:
    def __init__(self, path: str) -> None:
        self.__sheetList = [];
        self.__sheetDic: Dict = {}
        self.__workName = "";
        workBook = ExcelUtils.GetXLSX(path)
        if workBook is None:
            print("path is error:" + path)
            return
        self.__workName = os.path.basename(path).split('.')[0]
        workSheets = workBook.sheets()
        if workSheets is None:
            print("sheets is none:" + path)
        for sheet in workSheets:
            excelSheet = ConfigExcelSheel(sheet)
            self.__sheetList.append(excelSheet)
            self.__sheetDic[excelSheet.GetName()] = excelSheet

    def ExportBin(self, binPath: str):
        try:
            binPath = os.path.join(binPath, self.__workName + ".bin")
            binPath = binPath.replace("\\", "/");
            rowCount = self.GetRowCount()
            dataCount = self.GetDataCount()
            binWrite = BinWrite(binPath)
            binWrite.WriteInt(dataCount)
            for sheet in self.__sheetList:
                binlist = sheet.GetBinList()
                binWrite.WriteList(binlist)
            binWrite.EndWrite()
        except:
            ColorHelper.printRed(binPath + " is error");
            sys.exit();

    def GetDataCount(self) -> int:
        rowCount = self.GetRowCount()
        dataCount = rowCount - 3
        return dataCount

    def GetRowCount(self) -> int:
        count = 0
        for sheet in self.__sheetList:
            count = count + sheet.GetRowCount()
        return count

    def GetKeyList(self) -> List:
        return self.__sheetList[0].GetMainKey()

    def GetGetVariableRead(self,codeType:CodeType) -> List:
        return self.__sheetList[0].GetGetVariableRead(codeType);

    def GetMarkList(self) -> List:
        return self.__sheetList[0].GetMarkList()

    def GetVariableType(self,codeType:CodeType):
        return self.__sheetList[0].GetVariableType(codeType);

    def GetVariable(self,codeType:CodeType) -> List:
        return self.__sheetList[0].GetVariable(codeType)

    def GetTypeToRead(self,codeType:CodeType) -> List:
        return self.__sheetList[0].GetTypeToRead(codeType)
        
    def GetMarkList(self) -> List:
        return self.__sheetList[0].GetMarkList()




    def ExportCS(self, path: str,templatePath:str):
        path = os.path.join(path, self.__workName + ".cs")
        path = path.replace("\\","/");
        workName = self.__workName
        listKey = self.GetKeyList()

        MainData:ConfigExcelData = None;
        SecondData:ConfigExcelData = None
        listKeyCount = len(listKey)
        if listKeyCount > 0:
            MainData = listKey[0]

        if listKeyCount > 1:
            SecondData = listKey[1]

        try:
            templatePath = os.path.join(templatePath,"Template"+str(listKeyCount) + ".cs");
            templatePath = templatePath.replace("\\","/");
            f = open(templatePath,'r',encoding='utf-8')
            cscontent = f.read();
        except:
            ColorHelper.printRed(path +" is error");
            sys.exit();

        valueList = self.GetVariable(CodeType.CS);
        valueGetList = self.GetGetVariableRead(CodeType.CS);
        markList = self.GetMarkList();
        valueContent = "";
        for i in range(len(valueList)):
            value = valueList[i]
            valueGet = valueGetList[i]
            valueMark = markList[i];
            valueContent = valueContent + "\t\t//" + valueMark + "\n";
            valueContent = valueContent + "\t\t" + value + "\n";
            valueContent = valueContent + "\t\t" + valueGet + "\n";

        cscontent = cscontent.replace("TemplateClass",workName);
        if MainData != None:
            cscontent = cscontent.replace("FirstKeyType",MainData.GetVariableType(CodeType.CS));
            cscontent = cscontent.replace("FirstKey",MainData.GetValueName());
            
        if SecondData != None:    
            cscontent = cscontent.replace("SecondKeyType",SecondData.GetVariableType(CodeType.CS));
            cscontent = cscontent.replace("SecondKey",SecondData.GetValueName());
         
        cscontent = cscontent.replace("ValueContent",valueContent);



        valueContent = "";
        valueReadList = self.GetTypeToRead(CodeType.CS);
        for value in valueReadList:
            valueContent = valueContent + "\t\t\t"+ value + "\n";

        cscontent = cscontent.replace("ReadValueLoadContent",valueContent);   
        with open(path, "w") as f:
            f.write(cscontent) 





    def ExportJava(self, path: str,templatePath:str):
        path = os.path.join(path, self.__workName + ".java")
        path = path.replace("\\","/");
        workName = self.__workName
        listKey = self.GetKeyList()

        MainData:ConfigExcelData = None;
        SecondData:ConfigExcelData = None
        listKeyCount = len(listKey)
        if listKeyCount > 0:
            MainData = listKey[0]

        if listKeyCount > 1:
            SecondData = listKey[1]

        try:
            templatePath = os.path.join(templatePath,"Template"+str(listKeyCount) + ".java");
            templatePath = templatePath.replace("\\","/");
            f = open(templatePath,'r',encoding='utf-8')
            cscontent = f.read();
        except:
            ColorHelper.printRed(path +" is error");
            sys.exit();

        valueList = self.GetVariable(CodeType.JAVA);
        valueGetList = self.GetGetVariableRead(CodeType.JAVA);
        markList = self.GetMarkList();
        valueContent = "";
        for i in range(len(valueList)):
            value = valueList[i]
            valueGet = valueGetList[i]
            valueMark = markList[i];
            valueContent = valueContent + "\t//" + valueMark + "\n";
            valueContent = valueContent + "\t" + value + "\n";
            valueContent = valueContent + "\t" + valueGet + "\n";

        cscontent = cscontent.replace("TemplateClass",workName);
        if MainData != None:
            cscontent = cscontent.replace("FirstKeyType",MainData.GetVariableType(CodeType.JAVA));
            cscontent = cscontent.replace("FirstKey",MainData.GetValueName());
            
        if SecondData != None:    
            cscontent = cscontent.replace("SecondKeyType",SecondData.GetVariableType(CodeType.JAVA));
            cscontent = cscontent.replace("SecondKey",SecondData.GetValueName());
         
        cscontent = cscontent.replace("ValueContent",valueContent);



        valueContent = "";
        valueReadList = self.GetTypeToRead(CodeType.JAVA);
        for value in valueReadList:
            valueContent = valueContent + "\t\t"+ value + "\n";

        cscontent = cscontent.replace("ReadValueLoadContent",valueContent);   
        with open(path, "w") as f:
            f.write(cscontent) 




    def ExportCpp(self, path: str,templatePath:str):

        pathh = os.path.join(path, self.__workName + ".h")
        pathh = pathh.replace("\\","/");

        pathcpp = os.path.join(path, self.__workName + ".cpp")
        pathcpp = pathcpp.replace("\\","/");
        workName = self.__workName
        listKey = self.GetKeyList()

        MainData:ConfigExcelData = None;
        SecondData:ConfigExcelData = None
        listKeyCount = len(listKey)
        if listKeyCount > 0:
            MainData = listKey[0]

        if listKeyCount > 1:
            SecondData = listKey[1]

        try:
            templateCppPath = os.path.join(templatePath,"Template"+str(listKeyCount) + ".cpp");
            templateCppPath = templateCppPath.replace("\\","/");
            fCpp = open(templateCppPath,'r',encoding='utf-8')
            cppcontent = fCpp.read();

            templatehPath = os.path.join(templatePath,"Template"+str(listKeyCount) + ".h");
            templatehPath = templatehPath.replace("\\","/");
            fh = open(templatehPath,'r',encoding='utf-8')
            hcontent = fh.read();
        except Exception as e:
            ColorHelper.printRed(pathcpp +" is error");
            sys.exit();

        valueList = self.GetVariable(CodeType.CPP);
        valueGetList = self.GetGetVariableRead(CodeType.CPP);
        markList = self.GetMarkList();
        valueContent = "";
        valueGetContent = "";
        for i in range(len(valueList)):
            value = valueList[i]
            valueGet = valueGetList[i]
            valueMark = markList[i];
            valueContent = valueContent + "\t//" + valueMark + "\n";
            valueContent = valueContent + "\t" + value + "\n";
            valueGetContent = valueGetContent + "\t" + valueGet + "\n";

        hcontent = hcontent.replace("ValueContentFunction",valueGetContent);
        hcontent = hcontent.replace("ValueContent",valueContent);
        hcontent = hcontent.replace("TemplateClass",workName);
         
        cppcontent = cppcontent.replace("TemplateClass",workName);
        if MainData != None:
            hcontent = hcontent.replace("FirstKeyType",MainData.GetVariableType(CodeType.CPP));
            hcontent = hcontent.replace("FirstKey",MainData.GetValueName());
            cppcontent = cppcontent.replace("FirstKeyType",MainData.GetVariableType(CodeType.CPP));
            cppcontent = cppcontent.replace("FirstKey",MainData.GetValueName());
            
        if SecondData != None:    
            hcontent = hcontent.replace("SecondKeyType",SecondData.GetVariableType(CodeType.CPP));
            hcontent = hcontent.replace("SecondKey",SecondData.GetValueName());
            cppcontent = cppcontent.replace("SecondKeyType",SecondData.GetVariableType(CodeType.CPP));
            cppcontent = cppcontent.replace("SecondKey",SecondData.GetValueName());
         
       



        valueContent = "";
        valueReadList = self.GetTypeToRead(CodeType.CPP);
        for value in valueReadList:
            valueContent = valueContent + "\t" + value + "\n";

        cppcontent = cppcontent.replace("ReadValueLoadContent",valueContent);   
        with open(pathcpp, "w") as f:
            f.write(cppcontent) 

        with open(pathh, "w") as f:
            f.write(hcontent) 

        
        

    
