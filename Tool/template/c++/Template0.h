#pragma once

#include "DataBase.h"
#include "BinData.h"


class TemplateClass :DataBase
{
public:
	static std::vector<TemplateClass*>* GetDatas();
	static int GetCount();
	static void Load();
	static void Reload();
	static void Unload();
public:
ValueContentFunction
private:
	void Load(BinData *bin);
private:
	static std::vector<TemplateClass*>* m_Datas;
private:
ValueContent
};

