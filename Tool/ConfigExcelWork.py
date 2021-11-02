from typing import Dict
from typing import List
from ConfigExcelSheel import ConfigExcelSheel
from ConfigExcelData import ConfigExcelData
from Content import Content
from BinWrite import BinWrite
import xlrd
import ExcelUtils
import os
import Derictory


class ConfigExcelWork:
    __sheetList: List = []
    __sheetDic: Dict = {}
    __workName: str = ""

    def __init__(self, path: str) -> None:
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

    def ExportBin(self, path: str):
        Derictory.CreateDir(path)

        path = os.path.join(path, self.__workName + ".bin")
        path = path.replace("\\", "/")
        rowCount = self.GetRowCount()
        dataCount = self.GetDataCount()
        binWrite = BinWrite(path)
        binWrite.WriteInt(dataCount)
        for sheet in self.__sheetList:
            list = sheet.GetBinList()
            binWrite.WriteList(list)
        binWrite.EndWrite()

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

    def GetCSGetValueList(self) -> List:
        return self.__sheetList[0].GetCSGetValueList()

    def GetCSClassValue(self) -> List:
        return self.__sheetList[0].GetCSClassValue()

    def ExportCS(self, path: str):
        path = os.path.join(path, self.__workName + ".cs")
        content = Content()
        
        workName = self.__workName
        listKey = self.GetKeyList()

        MainData:ConfigExcelData = listKey[0]
        SecondData:ConfigExcelData = None
        listKeyCount = len(listKey)
        if listKeyCount > 1:
            SecondData = listKey[1]

        content.WriteLine("using UnityEngine;")
        content.WriteLine("using System.Collections.Generic;")
        content.WriteLine("using System.IO;")
        content.WriteLine("using System;")
        content.WriteLine("namespace Config")
        content.StartBlock()
        content.WriteLine("public class "+workName+" : DataBase") 
        content.StartBlock()
        content.WriteLine("#region value")
        valueList = self.GetCSClassValue()
        valueGetList = self.GetCSGetValueList()
        for i in range(len(valueList)):
            value = valueList[i]
            valueGet = valueGetList[i]
            content.WriteLine(value)
            content.WriteLine(valueGet)

        content.WriteLine("#endregion")
        content.WriteLine("#region load and get funtion")
        content.WriteLine("private static Dictionary<"+MainData.GetCSType() + "," + workName +"> m_DicDatas = null;")
        content.WriteLine("public static Dictionary<"+MainData.GetCSType() + ", "+workName+"> DicDatas")
        content.StartBlock()
        content.WriteLine("get")
        content.StartBlock()
        content.WriteLine("Load();")
        content.WriteLine("return m_DicDatas;")
        content.EndBlock()
        content.EndBlock()
        content.WriteLine("private static List<"+workName+"> m_Datas = null;")
        content.WriteLine("public static List<"+workName+"> Datas")
        content.StartBlock()
        content.WriteLine("get")
        content.StartBlock()
        content.WriteLine("Load();")
        content.WriteLine("return m_Datas;")
        content.EndBlock()
        content.EndBlock()
        content.WriteLine("public static int Count")
        content.StartBlock()
        content.WriteLine("get")
        content.StartBlock()
        content.WriteLine("Load();")
        content.WriteLine("return m_Datas.Count;")
        content.EndBlock()
        content.EndBlock()
        content.WriteLine("public static void Load()")
        content.StartBlock()
        content.WriteLine("if (m_DicDatas == null || m_Datas == null)")
        content.StartBlock()
        content.WriteLine("Stream fs = OpenData(\""+workName+".bin\");")
        content.WriteLine("if (fs != null)")
        content.StartBlock()
        content.WriteLine("BinaryReader br = new BinaryReader(fs);")
        content.WriteLine("int dataNum = br.ReadInt32();")
        content.WriteLine("m_DicDatas = new Dictionary<"+MainData.GetCSType() + ", "+workName+">(dataNum + 1);")
        content.WriteLine("m_Datas = new List<"+workName+">(dataNum + 1);")
        content.WriteLine("for (int i = 0; i < dataNum; ++i)")
        content.StartBlock()
        content.WriteLine(""+workName+" data = new "+workName+"();")
        content.WriteLine("data.Load(br);")
        content.WriteLine("if (m_DicDatas.ContainsKey(data." + MainData.GetValueName() + "))")
        content.StartBlock()
        content.WriteLine("Debug.LogError(\"fuck you mate, ID:\" + data.ID + \" already exists in "+workName+"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\");")
        content.WriteLine("continue;")
        content.EndBlock()
        content.WriteLine("m_DicDatas.Add(data." + MainData.GetValueName() + ", data);")
        content.WriteLine("m_Datas.Add(data);")
        content.EndBlock()
        content.WriteLine("br.Close();")
        content.WriteLine("br = null;")
        content.WriteLine("fs.Close();")
        content.WriteLine("fs = null;")
        content.EndBlock()
        content.EndBlock()
        content.EndBlock()
        content.WriteLine("public static "+workName+" Get("+MainData.GetCSType() + " MainKey)")
        content.StartBlock()
        content.WriteLine("Load();")
        content.WriteLine(""+workName+" data = null;")
        content.WriteLine("if(m_DicDatas.TryGetValue(MainKey, out data))")
        content.StartBlock()
        content.WriteLine("return data;")
        content.EndBlock()
        content.WriteLine("return null;")
        content.EndBlock()
        content.WriteLine("public static void Reload()")
        content.StartBlock()
        content.WriteLine("Unload();")
        content.WriteLine("Load();")
        content.EndBlock()
        content.WriteLine("public static void Unload()")
        content.StartBlock()
        content.WriteLine("bool bGC = false;")
        content.WriteLine("if(m_DicDatas != null)")
        content.StartBlock()
        content.WriteLine("m_DicDatas.Clear();")
        content.WriteLine("m_DicDatas = null;")
        content.WriteLine("bGC = true;")
        content.EndBlock()
        content.WriteLine("if(m_Datas != null)")
        content.StartBlock()
        content.WriteLine("m_Datas.Clear();")
        content.WriteLine("m_Datas = null;")
        content.WriteLine("bGC = true;")
        content.EndBlock()
        content.WriteLine("if(bGC)")
        content.StartBlock()
        content.WriteLine("System.GC.Collect();")
        content.EndBlock()
        content.EndBlock()
        content.WriteLine("public void Load(BinaryReader pStream)")
        content.StartBlock()
        valueReadList = self.GetCSReadValueList()
        for value in valueReadList:
            content.WriteLine(value)
        content.EndBlock()
        content.WriteLine("#endregion")

        content.EndBlock()
        content.EndBlock()
        content.WriteFile(path)

        
        

    
