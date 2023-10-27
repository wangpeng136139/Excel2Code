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
				Load();
				return m_Datas;
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

		private static Dictionary<FirstKeyType,TemplateClass> m_DicDatas = null;
		public static Dictionary<FirstKeyType, TemplateClass> DicDatas
		{
			get
			{
				Load();
				return m_DicDatas;
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
					m_DicDatas = new Dictionary<FirstKeyType,TemplateClass>(count);
					for (int i = 0; i < count; ++i)
					{
						TemplateClass data = new TemplateClass();
						data.Load(bin);
						m_Datas[i] = data;
						m_DicDatas.Add(data.FirstKey, data);
					}
				}
				catch(Exception e)
				{
					ConfigDebugEx.LogException(e);
				}
			}
		}



		public static TemplateClass Get(FirstKeyType FirstKey)
		{
			Get(FirstKey,out var data);
			return data;
		}

		public static bool Get(FirstKeyType FirstKey,out TemplateClass data)
		{
			Load();
			bool b = m_DicDatas.TryGetValue(FirstKey, out data);
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
				m_DicDatas = null;
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
