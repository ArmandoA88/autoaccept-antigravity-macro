Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
scriptDir = fso.GetParentFolderName(Wscript.ScriptFullName)
' Run the batch file invisible (0)
WshShell.Run chr(34) & scriptDir & "\run_macro.bat" & chr(34), 0
Set WshShell = Nothing
