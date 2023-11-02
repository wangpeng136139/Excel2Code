using System;
using System.Collections.Generic;
using System.IO;
namespace TableConfig
{
	public class DataBase
	{
		private static string DefaultFolder = "";
		public static void SetDataPath(string path)
		{
			DefaultFolder = path;
		}

		public static BinData OpenData(string fileName)
		{
		    var filePath = 	System.IO.Path.Combine(DefaultFolder ,fileName);
			filePath = filePath.Replace("\\","/");
			return OpenBin(filePath);V
		}

		public static BinData OpenBin(string fullPath)
		{
			BinData bin = null;
			try
			{
				var bytes = File.ReadAllBytes(fullPath);
				bin =  new BinData(bytes);
				return bin;
			}
			catch (Exception e)
			{

			}
			return bin;
		}
		
		public virtual void Load(BinData pStream) { }
	}
}
