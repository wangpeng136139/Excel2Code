class ExcelCell:
    # 内容
    m_value: str

    def __init__(self, value) -> None:
        self.m_value = value

    def GetValue(self):
        return self.m_value

    def GetValueStr(self):
        return str(self.m_value)
