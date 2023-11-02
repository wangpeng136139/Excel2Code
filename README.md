# Excel2Code
Excel To  Code

### Environment
python-3.10.4

pip install xlrd==1.2.0

pip install pyyaml

### Excel
The first line in Excel is the variable name

The second line in Excel is a comment

The third line in Excel is the variable type

### __Path.yaml    
basic configuration

Path:
```
#    CS = 0,
#    CPP = 1,
#    JAVA = 2,
#    LUA = 3,

  CodePath: ../Data/Code
  
  XlsxPath: ../Config
  
  BinPath: ../Data/Bin
  
  CodeType: 1   

  JavaPackageName: TableConfig
```


### Example
csharp:
```
 DataBase.SetDataPath("E:/Bin/");
 Test.Load();
 Test1.Load();
 Test2.Load();
```
java
```
 DataBase.SetDataPath("E:/Bin/");
 Test.Load();
 Test1.Load();
 Test2.Load();
```

C++
```
DataBase::SetDataPath("E:/project/ExportExcel/Data/Bin/");
Test::Load();
Test1::Load();
Test2::Load();
```
### Run

Use exceltool.sh


### support languange:
C++

CSharp

Java

Lua


![image](https://github.com/wangpeng136139/Excel2Code/assets/29979682/23267a84-d8f9-4175-990a-04cf13dc7a83)


