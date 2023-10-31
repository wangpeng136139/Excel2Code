#include "TemplateClass.h"

std::vector<TemplateClass*>* TemplateClass::m_Datas;

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



void TemplateClass::Load(BinData *bin)
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
			m_Datas = new std::vector<Test*>(count);
			for (int i = 0; i < count; ++i)
			{
				TemplateClass * data = new TemplateClass();
				data->Load(bin);
				m_Datas->push_back(data);
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

	for (std::vector<Test*>::iterator it = m_Datas->begin(); it != m_Datas->end(); it++) {
		delete *it;
	}

	m_Datas->clear();
	delete m_Datas;
	m_Datas = NULL;
}


