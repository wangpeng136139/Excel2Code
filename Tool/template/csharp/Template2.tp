using System.Collections.Generic;
using System.IO;
using System;
using TableConfig;
namespace  TableConfig
{
	public class TemplateClass:DataBase
	{
		#region value
ValueContent
		#endregion
		#region load and get funtion
		private static TemplateClass[] m_Datas = null;
		public static TemplateClass[] Datas
		{
			get
			{
				#if UNITY_ART || WINFORM
				Load();
				#endif
				return m_Datas;
			}
		}


		private static Dictionary<FirstKeyType, Dictionary<SecondKeyType, TemplateClass>> m_DicDicDatas = null;
		public static Dictionary<FirstKeyType, Dictionary<SecondKeyType, TemplateClass>> DicDicDatas
		{
			get
			{
				Load();
				return m_DicDicDatas;
			}
		}
		private static Dictionary<FirstKeyType, List<TemplateClass>> m_DicListDatas = null;
		public static Dictionary<FirstKeyType, List<TemplateClass>> DicListDatas
		{
			get
			{
				Load();
				return m_DicListDatas;
			}
		}

		
		public static int Count
		{
			get
			{
				Load();
				if(Datas == null)
				{
					return 0;
				}
				return Datas.Length;
			}
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
					var count = bin.ReadInt32();
					m_Datas = new TemplateClass[count];
					m_DicDicDatas = new Dictionary<FirstKeyType, Dictionary<SecondKeyType, TemplateClass>>();
					m_DicListDatas = new Dictionary<FirstKeyType, List<TemplateClass>>();
					for (int i = 0; i < count; ++i)
					{
						TemplateClass data = new TemplateClass();
						data.Load(bin);
						m_Datas[i] = data;
						if(false == m_DicDicDatas.TryGetValue(data.FirstKey,out var dicData))
						{
							dicData = new Dictionary<SecondKeyType, TemplateClass>();
							m_DicDicDatas.Add(data.FirstKey, dicData);
						}
						if(false == m_DicListDatas.TryGetValue(data.FirstKey,out var dataList))
						{
							dataList = new List<TemplateClass>();
							m_DicListDatas.Add(data.FirstKey, dataList);
						}
						dicData.Add(data.SecondKey, data);
						dataList.Add(data);
					}
				}
				catch(Exception e)
				{
					ConfigDebugEx.LogException(e);
				}
			}
		}

		public static TemplateClass Get(FirstKeyType FirstKey,SecondKeyType SecondKey)
		{
			Get(FirstKey,SecondKey,out var data);
			return data;
		}
		
		public static bool Get(FirstKeyType FirstKey, SecondKeyType SecondKey , out TemplateClass data)
		{
			Load();
			bool b = false;
			data = null;
			if(m_DicDicDatas.TryGetValue(FirstKey, out var dicData))
			{
				if(dicData.TryGetValue(SecondKey,out data))
				{
					b = true;
				}
			}
			return b;
		}
		public static List<TemplateClass> Get(FirstKeyType FirstKey)
		{
			Get(FirstKey,out var data);
			return data;
		}
		public static bool Get(FirstKeyType FirstKey,out List<TemplateClass> data)
		{
			Load();
			bool b = m_DicListDatas.TryGetValue(FirstKey, out data);
			return b;
		}

		public static void Reload()
		{
			Unload();
			Load();
		}


		public static void Unload()
		{
			bool bGC = false;
			if(m_Datas != null)
			{
				m_Datas = null;
				m_DicDicDatas = null;
				m_DicListDatas = null;
				bGC = true;
			}
			if(bGC)
			{
				System.GC.Collect();
			}
		}
		#endregion
}
}
