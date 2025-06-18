@echo off
echo 正在禁用 Thumbs.db 文件创建...

reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "DisableThumbnailCache" /t REG_DWORD /d 1 /f

echo 设置完成！请重启电脑使更改生效。
pause 