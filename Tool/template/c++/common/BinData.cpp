#include "BinData.h"
#include <fstream>

BinData::BinData(std::string path)
{
	Open(path);
}

std::string BinData::ReadString()
{
	int length = ReadInt32();
	std::string str;
	str.reserve(length);
	m_fin.read((char*)str.c_str(), length);
	return std::string();
}

unsigned long BinData::ReadUInt64()
{
	unsigned long s;
	m_fin.read((char*)&s, sizeof(s));
	return s;
}


bool BinData::IsOpen()
{
	return m_fin.is_open();
}

float BinData::ReadFloat()
{
	float s;
	m_fin.read((char*)&s, sizeof(s));
	return s;
}

double BinData::ReadDouble()
{
	double s;
	m_fin.read((char*)&s, sizeof(s));
	return s;
}

bool BinData::ReadBoolean()
{
	bool s = false;
	m_fin.read((char*)&s, sizeof(s));
	return s;
}

char BinData::Readsbyte()
{
	char s;
	m_fin.read((char*)&s, sizeof(s));
	return s;
}

std::string BinData::ReadCommonString()
{
	int index = ReadInt32();
	return commonString[index];
}



void BinData::Close()
{
	delete[] commonString;
	commonString = NULL;

	m_fin.close();
}

void BinData::Open(std::string path)
{
	m_fin.open(path,std::ios::in);//默认是ios::trunc
	if (!m_fin)
	{
		return;
	}
}

void BinData::ReadStringArray()
{
	int len = ReadInt32();
	commonString = new std::string[len];
	for (int i = 0; i < len; ++i)
	{
		commonString[i] = ReadString();
	}
}


int BinData::ReadInt32()
{
	int s = 0;
	m_fin.read((char*)&s, sizeof(s));
	return s;
}

long BinData::ReadInt64()
{
	long s = 0;
	m_fin.read((char*)&s, sizeof(s));
	return s;
}

short BinData::ReadInt16()
{
	short s = 0;
	m_fin.read((char*)&s, sizeof(s));
	return s;
}


unsigned short BinData::ReadUInt16()
{
	unsigned short s = 0;
	m_fin.read((char*)&s, sizeof(s));
	return s;
}

unsigned int BinData::ReadUInt32()
{
	unsigned int s = 0;
	m_fin.read((char*)&s, sizeof(s));
	return s;
}


