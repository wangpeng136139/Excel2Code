#pragma once

#include "DataBase.h"
#include "BinData.h"
#include <map>


class TemplateClass :DataBase
{
public:
	static int GetCount();
	static TemplateClass* Get(FirstKeyType FirstKey);
	static std::vector<TemplateClass*>* GetDatas();
	static void Load();
	static void Reload();
	static void Unload();
public:
ValueContentFunction
private:
	void Load(BinData* bin);
private:
	static std::vector<TemplateClass*>* m_Datas;
	static std::map<FirstKeyType,TemplateClass*>* m_DatasDic;
private:
ValueContent
};
