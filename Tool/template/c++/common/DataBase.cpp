#include "DataBase.h"

std::string DataBase::m_defaultPath = "";

void DataBase::SetDataPath(std::string path)
{
	m_defaultPath = path;
}

std::string DataBase::GetDataPath()
{
	return m_defaultPath;
}

BinData* DataBase::OpenBin(std::string fileName)
{
	int count = m_defaultPath.length() + 1 + fileName.length();
	char* cstr1 = new char[count];
	strcpy_s(cstr1, m_defaultPath.length()+1,m_defaultPath.c_str());
	strcat_s(cstr1, count,fileName.c_str());
	std::string fullPath = cstr1;
	delete[] cstr1;
	BinData* bin = new BinData(fullPath);
	return bin;
}