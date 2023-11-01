#include "TemplateClass.h"

std::vector<TemplateClass*>* TemplateClass::m_Datas = NULL;
std::map<FirstKeyType, TemplateClass*>* TemplateClass::m_DatasDic = NULL;

int TemplateClass::GetCount()
{
	if(m_Datas == NULL)
	{
		return NULL;
	}
    return m_Datas->size();
}

std::vector<TemplateClass*>* TemplateClass::GetDatas()
{
    return m_Datas;
}

TemplateClass* TemplateClass::Get(FirstKeyType FirstKey)
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
			m_Datas = new std::vector<TemplateClass*>(count);
			m_DatasDic = new std::map<FirstKeyType, TemplateClass*>();
			for (int i = 0; i < count; ++i)
			{
				TemplateClass * data = new TemplateClass();
				data->Load(bin);
				m_Datas->push_back(data);
				if(Get(data->GetFirstKey()) == NULL)
				{
					m_DatasDic->insert(std::make_pair(data->GetFirstKey(), data));
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
   if (m_Datas == NULL)
	{
		return;
	}

	for (std::vector<TemplateClass*>::iterator it = m_Datas->begin(); it != m_Datas->end(); it++) {
		delete *it;
	}

	m_Datas->clear();
	m_DatasDic->clear();
	delete m_Datas;
	delete m_DatasDic;
	m_Datas = NULL;
	m_DatasDic = NULL;
}


