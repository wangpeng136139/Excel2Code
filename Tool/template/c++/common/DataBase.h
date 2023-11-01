#pragma once
#include <string>;
#include <vector>;
#include "BinData.h";
#include "CommonEnum.h"

class DataBase
{
public:
	static void SetDataPath(std::string path);
	static std::string GetDataPath();
	static BinData* OpenBin(std::string fullPath);
private:
	static std::string m_defaultPath;
};

