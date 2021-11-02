set CurPath=%~dp0
set ConfigPath=%CurPath%Config
set CsPath=%CurPath%ToolExcel/Assets/Configs
set BinPath=%CurPath%ToolExcel/Assets/StreamingAssets/Bin
python Tool/exportbin.py %ConfigPath% %CsPath% %BinPath%
pause