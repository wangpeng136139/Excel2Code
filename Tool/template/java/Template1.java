package TableConfig;
import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.ArrayList;

public class TemplateClass extends DataBase
{
	//region value
ValueContent
	//endregion
    //region load and get funtion
	private static TemplateClass[] m_Datas = null;
	public static TemplateClass[] GetDatas()
	{
		return m_Datas;
	}

	
	public static int GetCount()
	{
		if(m_Datas == null)
		{
			return 0;
		}
		return m_Datas.length;
	}


	private static Map<FirstKeyType,TemplateClass> m_DicDatas = null;
	public static Map<FirstKeyType, TemplateClass> GetDicDatas()
	{
		return m_DicDatas;
	}
	


	private void Load(BinData bin)
	{
ReadValueLoadContent		
	}

	public static void Load()
	{
		BinData bin = OpenData("TemplateClass.bin")	;
		if (bin != null)
		{
			try
			{
				int count = bin.ReadInt32();
				m_Datas = new TemplateClass[count];
				m_DicDatas = new HashMap<>();
				for (int i = 0; i < count; ++i)
				{
					TemplateClass data = new TemplateClass();
					data.Load(bin);
					m_Datas[i] = data;
					m_DicDatas.put(data.GetFirstKey(), data);
				}
			}
			catch(Exception e)
			{
				
			}
		}
	}



	public static TemplateClass Get(FirstKeyType FirstKey)
	{
		TemplateClass data = m_DicDatas.get(FirstKey);
		return data;
	}



	public static void Reload()
	{
		Unload();
		Load();
	}

	public static void Unload()
	{
		boolean bGC = false;
		if(m_Datas != null)
		{
			m_Datas = null;
			bGC = true;
		}
		if(bGC)
		{
			System.gc();
		}
	}
	//endregion
}
