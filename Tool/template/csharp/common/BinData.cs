using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace TableConfig
{
	public unsafe class BinData
	{
		
		static readonly UTF8Encoding encoding = new UTF8Encoding();
		private  byte[] m_buffer;
		private string[] commonstring = null;
		private int position;
		public BinData(byte[] bytes)
		{
			this.m_buffer = bytes;
		}

		public unsafe int ReadInt32()
		{
			var v =  (int) this.m_buffer[position] | (int) this.m_buffer[position+1] << 8 | (int) this.m_buffer[position+2] << 16 | (int) this.m_buffer[position+3] << 24;
			position += 4;
			return v;
		}

		public unsafe void ReadStringArray()
		{
			int count = 0;
			count = ReadInt32();
			commonstring = new string[count];
			string str = string.Empty;
			for (int i = 0; i < count; ++i)
			{
				commonstring[i] = ReadCommonString();
			}
		}


		public unsafe Int64 ReadInt64()
		{
			var v =  (long) (uint) ((int) this.m_buffer[position+4] | (int) this.m_buffer[position+5] << 8 | (int) this.m_buffer[position+6] << 16 | (int) this.m_buffer[position+7] << 24) << 32 | (long) (uint) ((int) this.m_buffer[position+0] | (int) this.m_buffer[position+1] << 8 | (int) this.m_buffer[position+2] << 16 | (int) this.m_buffer[position+3] << 24);
			position += 8;
			return v;
		}

		public unsafe Int16 ReadInt16()
		{
			var v =  (short) ((int) this.m_buffer[position] | (int) this.m_buffer[position+1] << 8);
			position += 2;
			return v;
		}

		public unsafe UInt16 ReadUInt16()
		{
			var v = (ushort) ((uint) this.m_buffer[position] | (uint) this.m_buffer[position+1] << 8);
			position += 2;
			return v;
		}
		public unsafe UInt32 ReadUInt32()
		{
			var v = (uint) ((int) this.m_buffer[position] | (int) this.m_buffer[position+1] << 8 | (int) this.m_buffer[position+2] << 16 | (int) this.m_buffer[position+3] << 24);
			position += 4;
			return v;
		}
		public unsafe UInt64 ReadUInt64()
		{
			var v = (ulong)((int) this.m_buffer[position+4] | (int) this.m_buffer[position+5] << 8 | (int) this.m_buffer[position+6] << 16 | (int) this.m_buffer[position+7] << 24) << 32 | (ulong) (uint) ((int) this.m_buffer[position] | (int) this.m_buffer[position+1] << 8 | (int) this.m_buffer[position+2] << 16 | (int) this.m_buffer[position+3] << 24);
			position += 8;
			return v;
		}
		public unsafe float ReadFloat()
		{
			float a = 0;
			byte i;
			void* pf;
			pf = &a;
			float v;
			fixed (byte* start = m_buffer)
			{
				byte* px = start + position;
				for (i = 0; i < 4; i++)
				{
					*((byte*)pf + i) = *(px + i);
				}
				v = a;
			}
			position += 4;
			return v;
		}
		
		public unsafe double ReadDouble()
		{
			double a = 0;
			byte i;
			void* pf;
			pf = &a;
			double v;
			fixed (byte* start = m_buffer)
			{
				byte* px = start + position;
				for (i = 0; i < 8; i++)
				{
					*((byte*)pf + i) = *(px + i);
				}
				v = a;
			}
			position += 8;
			return v;
		}
		public bool ReadBoolean()
		{
			var v = this.m_buffer[position] > (byte) 0;
			position += 1;
			return v;
		}
		
		public sbyte Readsbyte()
		{
			var v = (sbyte)this.m_buffer[position];
			position += 1;
			return v;
		}
		public string ReadCommonString()
		{
			var len = ReadInt32();
			if(len < 0)
			{
				return string.Empty;
			}
			var v = commonstring[len];
			return v;
		}


		public string ReadString()
		{
			var len = ReadInt32();
			if(len < 0)
			{
				return string.Empty;
			}
			string v = encoding.GetString(m_buffer,position , (int)len);
			position += len;
			return v;

		}

		public void Close()
		{
			m_buffer = null;
			commonstring = null;
		    position = 0;
		}
	}
}
