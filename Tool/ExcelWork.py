from typing import Dict
from typing import List
from Content import Content
from ExcelSheel import ExcelSheel
from BinWrite import BinWrite
import xlrd
import ExcelUtils
import os


class ExcelWork:
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
            excelSheet = ExcelSheel(sheet)
            self.__sheetList.append(excelSheet)
            self.__sheetDic[excelSheet.GetName()] = excelSheet

    def ExportBin(self, path: str):
        path = os.path.join(path, self.__workName + ".bin")
        rowCount = self.GetRowCount()   
        binWrite = BinWrite(path)
        binWrite.WriteInt(rowCount)
        for sheet in self.__sheetList:
            list = sheet.GetBinList()
            binWrite.WriteBin(list)

    def GetRowCount(self) -> int:
        count = 0
        for sheet in self.__sheetList:
            count = count + sheet.GetRowCountself()
        return count

    def ExportCS(self, path: str):
        path = os.path.join(path, self.__workName + ".cs")
        content = Content()
        
        content.WriteLine("using UnityEngine;")
        content.WriteLine("using System.Collections.Generic;")
        content.WriteLine("using System.IO;")
        content.WriteLine("using System;")
        content.WriteLine("namespace Config")
        content.StartBlock()
        content.WriteLine("public class Templet : DataBase") 
        content.StartBlock()
        content.WriteLine("#region load and get funtion")
        content.WriteLine("private static Dictionary<TemKey, Templet> m_DicDatas = null;")
        content.WriteLine("public static Dictionary<TemKey, Templet> DicDatas")
        content.StartBlock()
        content.WriteLine("get")
        content.StartBlock()
        content.WriteLine("Load();")
        content.WriteLine("return m_DicDatas;")
        content.EndBlock()
        content.EndBlock()
        content.WriteLine("private static List<Templet> m_Datas = null;")
        content.WriteLine("public static List<Templet> Datas")
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
        content.WriteLine("Stream fs = OpenData(\"Templet.bin\");")
        content.WriteLine("if (fs != null)")
        content.StartBlock()
        content.WriteLine("BinaryReader br = new BinaryReader(fs);")
        content.WriteLine("ushort dataNum = br.ReadUInt16();")
        content.WriteLine("m_DicDatas = new Dictionary<TemKey, Templet>(dataNum + 1);")
        content.WriteLine("m_Datas = new List<Templet>(dataNum + 1);")
        content.WriteLine("for (int i = 0; i < dataNum; ++i)")
        content.StartBlock()
        content.WriteLine("Templet data = new Templet();")
        content.WriteLine("data.Load(br);")
        content.WriteLine("if (m_DicDatas.ContainsKey(data.MainKey))")
        content.StartBlock()
        content.WriteLine("Debug.LogError(\"fuck you mate, ID:\" + data.ID + \" already exists in Templet!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\");")
        content.WriteLine("continue;")
        content.EndBlock()
        content.WriteLine("m_DicDatas.Add(data.MainKey, data);")
        content.WriteLine("m_Datas.Add(data);")
        content.EndBlock()
        content.WriteLine("br.Close();")
        content.WriteLine("br = null;")
        content.WriteLine("fs.Close();")
        content.WriteLine("fs = null;")
        content.EndBlock()
        content.EndBlock()
        content.EndBlock()
        content.WriteLine("public static Templet Get(TemKey MainKey)")
        content.StartBlock()
        content.WriteLine("Load();")
        content.WriteLine("Templet data = null;")
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
        content.WriteLine("#endregion")

        ReadContent
        content.EndBlock()
        content.EndBlock()

        
        

    
