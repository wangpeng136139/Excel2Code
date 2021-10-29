import os
from typing import List
import struct
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
class BinWrite:
    m_path: str
    m_listContent: List = []
    
    def __init__(self, path) -> None:
        self.m_path = path

    def StartWrite(self):
        return

    def WriteBin(self, value) -> None:
        self.m_listContent.append(value)

    def WriteList(self, value: List) -> None:
        self.m_listContent.extend(value)

    def WriteInt(self, value: int) -> None:
        binValue = struct.pack("i", value)
        self.WriteBin(binValue)     

    def EndWrite(self):
        with open(self.m_path, 'wb') as wb:
            for value in self.m_listContent:
                wb.write(value)
        print("写入："+self.m_path)
    
        