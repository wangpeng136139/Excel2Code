#pragma once
#include <fstream>
#include <string>

class BinData
{
public:
    BinData(std::string path);
    void ReadStringArray();
    int ReadInt32();
    long ReadInt64();
    short ReadInt16();
    unsigned short ReadUInt16();
    unsigned int ReadUInt32();
    unsigned long ReadUInt64();
    float ReadFloat();
    double ReadDouble();
    bool ReadBoolean();
    char Readsbyte();
    std::string ReadCommonString();
    std::string ReadString();
    void Close();
    bool IsOpen();
private:
    void Open(std::string path);
private:
    std::string* commonString;
    std::ifstream m_fin;
};