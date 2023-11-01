package TableConfig;

public class DataBase
{
	private static String DefaultFolder = "";
	public static void SetDataPath(String path)
	{
		DefaultFolder = path;
	}

	public static BinData OpenData(String fileName)
	{
		StringBuilder stringBuilder = new StringBuilder();
		stringBuilder.append(DefaultFolder);
		stringBuilder.append(fileName);
		String fullPath = stringBuilder.toString();
		return OpenBin(fullPath);
	}

	public static BinData OpenBin(String fullPath)
	{
		BinData bin = null;
		try
		{
			bin =  new BinData(fullPath);
			return bin;
		}
		catch (Exception e)
		{

		}
		return bin;
	}
}