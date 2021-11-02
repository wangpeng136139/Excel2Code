using UnityEngine;
using System.Collections.Generic;
using System.IO;
using System;
namespace Config
{
	public class UIModeConfigData : DataBase
	{
		#region value
		private int m_ID;
		public int ID =>  m_ID;
		private bool m_Name;
		public bool Name =>  m_Name;
		private string m_id;
		public string id =>  m_id;
		private string m_ResNor;
		public string ResNor =>  m_ResNor;
		private string m_ResSelect;
		public string ResSelect =>  m_ResSelect;
		private int m_permissionIndex;
		public int permissionIndex =>  m_permissionIndex;
		private CommonType m_aaa;
		public CommonType aaa =>  m_aaa;
		#endregion
		#region load and get funtion
		private static Dictionary<int,UIModeConfigData> m_DicDatas = null;
		public static Dictionary<int, UIModeConfigData> DicDatas
		{
			get
			{
				Load();
				return m_DicDatas;
			}
		}
		private static List<UIModeConfigData> m_Datas = null;
		public static List<UIModeConfigData> Datas
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
				return m_Datas.Count;
			}
		}
		public static void Load()
		{
			if (m_DicDatas == null || m_Datas == null)
			{
				Stream fs = OpenData("UIModeConfigData.bin");
				if (fs != null)
				{
					BinaryReader br = new BinaryReader(fs);
					int dataNum = br.ReadInt32();
					m_DicDatas = new Dictionary<int, UIModeConfigData>(dataNum + 1);
					m_Datas = new List<UIModeConfigData>(dataNum + 1);
					for (int i = 0; i < dataNum; ++i)
					{
						UIModeConfigData data = new UIModeConfigData();
						data.Load(br);
						if (m_DicDatas.ContainsKey(data.ID))
						{
							Debug.LogError("fuck you mate, ID:" + data.ID + " already exists in UIModeConfigData!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
							continue;
						}
						m_DicDatas.Add(data.ID, data);
						m_Datas.Add(data);
					}
					br.Close();
					br = null;
					fs.Close();
					fs = null;
				}
			}
		}
		public static UIModeConfigData Get(int MainKey)
		{
			Load();
			UIModeConfigData data = null;
			if(m_DicDatas.TryGetValue(MainKey, out data))
			{
				return data;
			}
			return null;
		}
		public static void Reload()
		{
			Unload();
			Load();
		}
		public static void Unload()
		{
			bool bGC = false;
			if(m_DicDatas != null)
			{
				m_DicDatas.Clear();
				m_DicDatas = null;
				bGC = true;
			}
			if(m_Datas != null)
			{
				m_Datas.Clear();
				m_Datas = null;
				bGC = true;
			}
			if(bGC)
			{
				System.GC.Collect();
			}
		}
		public void Load(BinaryReader pStream)
		{
			 m_ID = pStream.ReadInt32();
			 m_Name = pStream.ReadBoolean();
			 m_id = ReadUTF8String(pStream);
			 m_ResNor = ReadUTF8String(pStream);
			 m_ResSelect = ReadUTF8String(pStream);
			 m_permissionIndex = pStream.ReadInt32();
			 m_aaa = (CommonType)pStream.ReadInt32();
			 Debug.Log($"m_aaa{m_aaa}");
			 
		}
		#endregion
	}
}
