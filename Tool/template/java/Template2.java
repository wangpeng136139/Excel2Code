package TableConfig;
import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.ArrayList;
import javafx.util.Pair;

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


	private static Map<Pair<FirstKeyType, SecondKeyType>, TemplateClass> m_DicDicDatas = null;
	public static Map<Pair<FirstKeyType, SecondKeyType>, TemplateClass> GetDicDicDatas()
	{
		return m_DicDicDatas;
	}

	private static Map<FirstKeyType, List<TemplateClass>> m_DicListDatas = null;
	public static Map<FirstKeyType, List<TemplateClass>> GetDicListDatas()
	{
		return m_DicListDatas;
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
				m_DicDicDatas = new HashMap<>();
				m_DicListDatas = new HashMap<>();
				for (int i = 0; i < count; ++i)
				{
					TemplateClass data = new TemplateClass();
					data.Load(bin);
					m_Datas[i] = data;
					Pair<FirstKeyType, SecondKeyType> mainKey =  new Pair<>(data.GetFirstKey(),data.GetSecondKey());
					if(null == m_DicDicDatas.get(mainKey))
					{
						m_DicDicDatas.put(mainKey, data);
					}

					List<TemplateClass> dataList = m_DicListDatas.get(data.GetFirstKey());
					if(dataList == null)
					{
						dataList = new ArrayList();
						m_DicListDatas.put(data.GetFirstKey(), dataList);
					}
					dataList.add(data);
				}
			}
			catch(Exception e)
			{
				
			}
		}
	}

	public static TemplateClass Get(FirstKeyType FirstKey,SecondKeyType SecondKey)
	{
		Pair<FirstKeyType, SecondKeyType> mainKey =  new Pair<>(FirstKey,SecondKey);
		return m_DicDicDatas.get(mainKey);
	}
	

	public static List<TemplateClass> Get(FirstKeyType FirstKey)
	{
		return m_DicListDatas.get(FirstKey);
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