#pragma once

#include "DataBase.h"
#include "BinData.h"
#include <map>


class TemplateClass :DataBase
{
public:
	static int GetCount();
	static std::vector<TemplateClass*>* Get(FirstKeyType FirstKey);
	static std::vector<TemplateClass*>* GetDatas();
	static TemplateClass* Get(FirstKeyType FirstKey,SecondKeyType SecondKey);
	static void Load();
	static void Reload();
	static void Unload();
public:
ValueContentFunction
private:
	void Load(BinData* bin);
private:
	static std::vector<TemplateClass*>* m_Datas;
	static std::map<FirstKeyType,std::vector<TemplateClass*>*>* m_DatasDic;
	static std::map<std::pair<FirstKeyType, SecondKeyType>, TemplateClass*>* m_DatasDicDic;
private:
ValueContent
};
