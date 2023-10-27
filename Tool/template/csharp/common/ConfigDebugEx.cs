using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace TableConfig
{
	public unsafe class ConfigDebugEx
	{
		public static void LogException(Exception ex)
		{
			Console.WriteLine($"[{DateTime.Now.ToString("yy:MM:dd HH-mm-ss-ffff")}]{ex.ToString()}");
		}

	}
}
