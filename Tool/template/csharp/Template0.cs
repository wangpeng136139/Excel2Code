using System.Collections.Generic;
using System.IO;
using System;
using TableConfig;
namespace  TableConfig
{
	public class TemplateClass :DataBase
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

		private void Load(BinData bin)
		{
ReadValueLoadContent		
		}


		public static void Load()
		{
			BinData bin = OpenData("TemplateClass.bin");
			if (bin != null)
			{
				try
				{
					var count = bin.ReadInt32();
					m_Datas = new TemplateClass[count];
					for (int i = 0; i < count; ++i)
					{
						TemplateClass data = new TemplateClass();
						data.Load(bin);
						m_Datas[i] = data;
					}
				}
				catch(Exception e)
				{
					ConfigDebugEx.LogException(e);
				}
			}
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
