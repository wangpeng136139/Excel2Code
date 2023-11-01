package TableConfig;

import java.io.*;

public class BinData
{
	private String[] commonstring = null;
	private FileInputStream fileInputStream = null;
	private DataInputStream dataInputStream = null;
	public BinData(String path)
	{
		try {
			fileInputStream = new FileInputStream(path);
			dataInputStream = new DataInputStream(fileInputStream);
			 // 执行文件操作
		 } catch (FileNotFoundException e) {
			 e.printStackTrace();
		 }
	
	}

	public  int ReadInt32()
	{
		try {
			int ch1 = fileInputStream.read();
			int ch2 = fileInputStream.read();
			int ch3 = fileInputStream.read();
			int ch4 = fileInputStream.read();
			if ((ch1 | ch2 | ch3 | ch4) < 0)
				throw new EOFException();
        	return ((ch1) + (ch2 << 8) + (ch3 << 16) + (ch4 << 24));
			 // 执行文件操作
		 } catch (Exception e) {
			 e.printStackTrace();
		 }
		 
		return 0;
	}

	public void ReadStringArray()
	{
		int count = 0;
		count = ReadInt32();
		commonstring = new String[count];
		for (int i = 0; i < count; ++i)
		{
			commonstring[i] = ReadString();
		}
	}


	public long ReadInt64()
	{
		try {

			int ch1 = fileInputStream.read();
			int ch2 = fileInputStream.read();
			int ch3 = fileInputStream.read();
			int ch4 = fileInputStream.read();
			int ch5 = fileInputStream.read();
			int ch6 = fileInputStream.read();
			int ch7 = fileInputStream.read();
			int ch8 = fileInputStream.read();
			return (((long)ch8 << 56) +
                ((long)(ch7 & 255) << 48) +
                ((long)(ch6 & 255) << 40) +
                ((long)(ch5 & 255) << 32) +
                ((long)(ch4 & 255) << 24) +
                ((ch3 & 255) << 16) +
                ((ch2 & 255) <<  8) +
                ((ch1 & 255) <<  0));
			 // 执行文件操作
		 } catch (Exception e) {
			 e.printStackTrace();
		 }
		return 0;
	}

	public short ReadInt16()
	{
		try {
			int ch1 = fileInputStream.read();
			int ch2 = fileInputStream.read();
			if ((ch1 | ch2) < 0)
				throw new EOFException();
        	return (short)((ch1) + (ch2 << 8));
			 // 执行文件操作
		 } catch (Exception e) {
			 e.printStackTrace();
		 }
		return 0;
	}

	public short ReadUInt16()
	{
		 return ReadInt16();
	}
	public int ReadUInt32()
	{ 
		return ReadInt32();
	}
	public long ReadUInt64()
	{
		return ReadInt64();
	}
	public float ReadFloat()
	{
		return Float.intBitsToFloat(ReadInt32());
	}
	
	public double ReadDouble()
	{
		return Double.longBitsToDouble(ReadInt64());
	}

	public boolean ReadBoolean()
	{
		try {
			return dataInputStream.readBoolean();
			 // 执行文件操作
		 } catch (Exception e) {
			 e.printStackTrace();
		 }
		return false;
	}
	
	public char Readsbyte()
	{
	   try {
			return dataInputStream.readChar();
			 // 执行文件操作
		 } catch (Exception e) {
			 e.printStackTrace();
		 }
		return 0;
	}

	public String ReadCommonString()
	{
		int id = ReadInt32();
		if(id < 0)
		{
			return "";
		}
		return commonstring[id];
	}


	public String ReadString()
	{
		int len = ReadInt32();
		if(len < 0)
		{
			return "";
		}

		try {
			byte[] bytes = new byte[len];
			dataInputStream.readFully(bytes);
			String v = new String(bytes, "UTF-8");
			return v;
			 // 执行文件操作
		 } catch (Exception e) {
			 e.printStackTrace();
		 }
		return "";
	}

	public void Close()
	{
		try
		{
			dataInputStream.close();
			fileInputStream.close();
			commonstring = null;
		}
		catch (Exception e) {
			 e.printStackTrace();
		 }
	}
}