using System;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
namespace Config
{
	public class Vec3Vec
	{
		public int x = 0;
		public int y = 0;
		public int z = 0;
	}
	public class DataBase
	{
		#if UNITY_EDITOR || UNITY_STANDALONE_WIN 
		private static string DefaultFolder = Path.Combine(Application.streamingAssetsPath,"Bin");
		#elif  UNITY_IOS || UNITY_ANDROID
		private static string DefaultFolder = Path.Combine(Application.persistentDataPath,"Bin/");
		#endif
		public static Stream OpenData(string fileName)
		{
			var filePath = DefaultFolder + fileName;
			#if UNITY_EDITOR || UNITY_STANDALONE_WIN || UNITY_IOS
			filePath = filePath.Replace(file://, );
			#elif UNITY_ANDROID
			filePath = filePath.Replace(file:///, );
			#endif
			return OpenFileStream(filePath);
		}
		public static System.IO.Stream OpenFileStream(string fullPath)
		{
			long streamLength = 0;
			return OpenFileStream(fullPath, out streamLength);
		}
		public static System.IO.Stream OpenFileStream(string fullPath, out long streamLength)
		{
			Stream filestream = null;
			streamLength = 0;
			try
			{
				filestream = File.OpenRead(fullPath);
				streamLength = filestream.Length;
				return filestream;
			}
			catch (Exception e)
			{
				filestream = null;
				UnityEngine.Debug.LogException(e);
			}
			return filestream;
		}
		public virtual void Load(BinaryReader pStream) { }
		public static void ReadIntList(BinaryReader pStream, ref List<int> intList)
		{
			int num = pStream.ReadInt16();
			for (int i = 0; i < num; i++)
			{
				if (intList == null)
				{
					intList = new List<int>();
				}
				intList.Add(pStream.ReadInt32());
			}
		}
		 public static void ReadShortList(BinaryReader pStream, ref List<short> intList)
		{
			int num = pStream.ReadInt16();
			for (int i = 0; i < num; i++)
			{
				if (intList == null)
				{
					intList = new List<short>();
				}
				intList.Add(pStream.ReadInt16());
			}
		}
		public static void ReadByteList(BinaryReader pStream, ref List<sbyte> intList)
		{
			int num = pStream.ReadInt16();
			for (int i = 0; i < num; i++)
			{
				if (intList == null)
				{
					intList = new List<sbyte>();
				}
				intList.Add(pStream.ReadSByte());
			}
		}
		public static void ReadFloatList(BinaryReader pStream, ref List<float> intList)
		{
			int num = pStream.ReadInt16();
			for (int i = 0; i < num; i++)
			{
				if (intList == null)
				{
					intList = new List<float>();
				}
				intList.Add(pStream.ReadSingle());
			}
		}
		public static void ReadStringList(BinaryReader pStream, ref List<string> strList)
		{
			int num = pStream.ReadInt16();
			for (int i = 0; i < num; i++)
			{
				if (strList == null)
				{
					strList = new List<string>();
				}
				strList.Add(pStream.ReadString());
			}
		}
		public static void ReadIntDictionary(BinaryReader pStream, ref Dictionary<int, int> intDictionary)
		{
			int num = pStream.ReadInt16();
			for (int i = 0; i < num; i++)
			{
				if (intDictionary == null)
				{
					intDictionary = new Dictionary<int, int>();
				}
				intDictionary[pStream.ReadInt32()] = pStream.ReadInt32();
			}
		}
		public static void ReadByteListList(BinaryReader pStream, ref List<List<sbyte>> intListList)
		{
			int listNum = pStream.ReadInt16();
			for (int i = 0; i < listNum; i++)
			{
				if (intListList == null)
				{
					intListList = new List<List<sbyte>>();
				}
				int intNum = pStream.ReadInt16();
				List<sbyte> intData = new List<sbyte>();
				for (int j = 0; j < intNum; j++)
				{
					intData.Add(pStream.ReadSByte());
				}
				intListList.Add(intData);
			}
		}
		public static void ReadShortListList(BinaryReader pStream, ref List<List<short>> intListList)
		{
			int listNum = pStream.ReadInt16();
			for (int i = 0; i < listNum; i++)
			{
				if (intListList == null)
				{
					intListList = new List<List<short>>();
				}
				int intNum = pStream.ReadInt16();
				List<short> intData = new List<short>();
				for (int j = 0; j < intNum; j++)
				{
					intData.Add(pStream.ReadInt16());
				}
				intListList.Add(intData);
			}
		}
		public static void ReadIntListList(BinaryReader pStream, ref List<List<int>> intListList)
		{
			int listNum = pStream.ReadInt16();
			for (int i = 0; i < listNum; i++)
			{
				if (intListList == null)
				{
					intListList = new List<List<int>>();
				}
				int intNum = pStream.ReadInt16();
				List<int> intData = new List<int>();
				for (int j = 0; j < intNum; j++)
				{
					intData.Add(pStream.ReadInt32());
				}
				intListList.Add(intData);
			}
		}
		public static void ReadFloatListList(BinaryReader pStream, ref List<List<float>> floatListList)
		{
			int listNum = pStream.ReadInt16();
			for (int i = 0; i < listNum; i++)
			{
				if (floatListList == null)
				{
					floatListList = new List<List<float>>();
				}
				int floatNum = pStream.ReadInt16();
				List<float> floatData = new List<float>();
				for (int j = 0; j < floatNum; j++)
				{
					floatData.Add(pStream.ReadSingle());
				}
				floatListList.Add(floatData);
			}
		}
		public object GetValue(string propertyName)
		{
			var info = this.GetType().GetProperty(propertyName);
			if (info != null)
			{
				return info.GetValue(this, null);
			}
			else
			{
				return null;
			}
		}
		public static void ReadVec3VecList(BinaryReader pStream, ref List<Vec3Vec> Vec3VecList)
		{
			int listNum = pStream.ReadInt16();
			if (Vec3VecList == null)
			{
				Vec3VecList = new List<Vec3Vec>();
			}
			for (int i = 0; i < listNum; ++i)
			{
				Vec3Vec data = new Vec3Vec();
				data.x = pStream.ReadInt32();
				data.y = pStream.ReadInt32();
				data.z = pStream.ReadInt32();
				Vec3VecList.Add(data);
			}
		}
		public static void ReadVec3Vec(BinaryReader pStream, ref Vec3Vec Vec3Vect)
		{
			if (Vec3Vect == null)
			{
				Vec3Vect = new Vec3Vec();
			}
			Vec3Vect.x = pStream.ReadInt32();
			Vec3Vect.y = pStream.ReadInt32();
			Vec3Vect.z = pStream.ReadInt32();
		}
	}
}
