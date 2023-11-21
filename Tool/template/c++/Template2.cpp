#include "TemplateClass.h"

std::vector<TemplateClass*>* TemplateClass::m_Datas = NULL;
std::map<FirstKeyType, std::vector<TemplateClass*>*>* TemplateClass::m_DatasDic = NULL;
std::map<std::pair<FirstKeyType, SecondKeyType>, TemplateClass*>* TemplateClass::m_DatasDicDic = NULL;

int TemplateClass::GetCount()
{
	if(m_Datas == NULL)
	{
		return 0;
	}
    return m_Datas->size();
}

std::vector<TemplateClass*>* TemplateClass::GetDatas()
{
    return m_Datas;
}

std::vector<TemplateClass*>*  TemplateClass::Get(FirstKeyType FirstKey)
{
	if(m_DatasDic == NULL)
	{
		return NULL;
	}

	auto it = m_DatasDic->find(FirstKey);
	if (it != m_DatasDic->end()) {
		// 键存在于map中
		return it->second; // 访问键对应的值
	}
	else {
		return NULL;
	}
}

TemplateClass* TemplateClass::Get(FirstKeyType FirstKey,SecondKeyType SecondKey)
{
	if(m_DatasDicDic == NULL)
	{
		return NULL;
	}

	std::pair<FirstKeyType, SecondKeyType>> keyPair;
	keyPair.first = FirstKey;
	keyPair.second = SecondKey;
	auto it = m_DatasDicDic->find(keyPair);
	if (it != m_DatasDicDic->end()) {
		// 键存在于map中
		return it->second; // 访问键对应的值
	}
	else {
		return NULL;
	}
}

void TemplateClass::Load(BinData* bin)
{
ReadValueLoadContent	
}



void TemplateClass::Load() 
{
	BinData* bin = OpenBin("TemplateClass.bin");
	if (bin != NULL && bin->IsOpen())
	{
		try
		{
			int count = bin->ReadInt32();
			m_Datas = new std::vector<Test2*>();
			m_DatasDic = new std::map<FirstKeyType, std::vector<Test2*>*>();
			m_DatasDicDic = new std::map<std::pair<FirstKeyType, SecondKeyType>>, Test2*>();
			for (int i = 0; i < count; ++i)
			{
				TemplateClass * data = new TemplateClass();
				data->Load(bin);
				m_Datas->push_back(data);
				auto it = m_DatasDic->find(data->GetFirstKey());
				if (it == m_DatasDic->end()) {
					std::vector<TemplateClass*> *pVec = new std::vector<TemplateClass*>();
					m_DatasDic->insert(std::make_pair(data->GetFirstKey(), pVec));
					pVec->push_back(data);
				}
				else
				{
					it->second->push_back(data);
				}
				
				std::pair<FirstKeyType, SecondKeyType>> keyPair;
				keyPair.first = data->GetFirstKey();
				keyPair.second = data->GetSecondKey();
				auto itDic = m_DatasDicDic->find(keyPair);
				if (itDic == m_DatasDicDic->end()) {
					m_DatasDicDic->insert(std::make_pair(keyPair, data));
				}
				
				
			}
		}
		catch (const std::exception& e)
		{

		}
		bin->Close();
		delete bin;
		bin = NULL;
	}
}

void TemplateClass::Reload()
{
    Unload();
    TemplateClass::Load();
}

void TemplateClass::Unload()
{
	for (std::vector<TemplateClass*>::iterator it = m_Datas->begin(); it != m_Datas->end(); it++) {
		delete *it;
	}


	m_DatasDicDic->clear();
	m_Datas->clear();
	m_DatasDic->clear();
	delete m_Datas;
	delete m_DatasDic;
	delete m_DatasDicDic;
	m_Datas = NULL;
	m_DatasDic = NULL;
	m_DatasDicDic = NULL;
}


