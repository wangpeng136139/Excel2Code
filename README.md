# Excel2Code
Excel To  Code

### Environment
python-3.10.4

pip install xlrd==1.2.0

pip install pyyaml


### __Path.yaml    
basic configuration

Path:

  CodePath: ../Data/Code
  
  XlsxPath: ../Config
  
  BinPath: ../Data/Bin
  
  CodeType: csharp   

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
