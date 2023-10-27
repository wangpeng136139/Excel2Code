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

    def GetCSReadValueList(self) -> List:
        return self.__sheetList[0].GetCSReadValueList()

    def GetCSMarkList(self) -> List:
        return self.__sheetList[0].GetCSMarkList()

    def GetCSGetValueList(self) -> List:
        return self.__sheetList[0].GetCSGetValueList()

    def GetCSClassValue(self) -> List:
        return self.__sheetList[0].GetCSClassValue()

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
            templatePath = os.path.join(templatePath,"Template"+str(listKeyCount) + ".tp");
            templatePath = templatePath.replace("\\","/");
            f = open(templatePath,'r',encoding='utf-8')
            cscontent = f.read();
        except:
            ColorHelper.printRed(path +" is error");
            sys.exit();

        valueList = self.GetCSClassValue()
        valueGetList = self.GetCSGetValueList();
        markList = self.GetCSMarkList();
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
            cscontent = cscontent.replace("FirstKeyType",MainData.GetCSType());
            cscontent = cscontent.replace("FirstKey",MainData.GetValueName());
            
        if SecondData != None:    
            cscontent = cscontent.replace("SecondKeyType",SecondData.GetCSType());
            cscontent = cscontent.replace("SecondKey",SecondData.GetValueName());
         
        cscontent = cscontent.replace("ValueContent",valueContent);



        valueContent = "";
        valueReadList = self.GetCSReadValueList()
        for value in valueReadList:
            valueContent = valueContent + "\t\t\t"+ value + "\n";

        cscontent = cscontent.replace("ReadValueLoadContent",valueContent);   
        with open(path, "w") as f:
            f.write(cscontent) 

        
        

    
