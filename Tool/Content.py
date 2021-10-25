from typing import List
import Derictory
import os


class Content:
    listContent: List
    tableStr: str

    def __init__(self):
        self.tableStr = ""
        self.listContent = []

    def StartBlock(self) -> None:
        contentStr = self.tableStr + "{"
        self.listContent.append(contentStr)
        self.tableStr += "\t"

    def EndBlock(self) -> None:
        self.EndBlockAppendStr("")

    def EndBlockAppendStr(self, endStr: str) -> None:
        if len(self.tableStr) != 0:
            self.tableStr = self.tableStr[::-1].replace('\t', '', 1)[::-1]
        contentStr = self.tableStr + "}"
        if len(endStr) > 0:
            contentStr = contentStr + endStr
        self.listContent.append(contentStr)
        
    def AddSpace(self) -> None:
        self.listContent.append("\n")

    def WriteLine(self, str: str) -> None:
        content = self.tableStr + str
        self.listContent.append(content)
    
    def ClearContent(self) -> None:
        self.tableStr = ""
        self.listContent = {}
    
    def WriteFile(self, path: str) -> None:
        Derictory.CreateDir(os.path.dirname(path))
        with open(path, "w") as f:
            content: str = ""
            for item in self.listContent:
                content = content + item + "\n"
            f.write(content)
        


        