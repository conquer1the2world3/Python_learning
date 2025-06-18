import os
import time

file = open("IO\\input.py","r",encoding="utf-8")
print("文件名："+file.name)
print("文件是否关闭：",file.closed)
print("访问模式：",file.mode)
print("文件是否可读：",file.readable())
print("文件是否可写：",file.writable())
print("文件是否可追加：",file.seekable())

str = file.read(10)
print("读取的数据：\n",str)

position = file.tell()
print("当前文件位置：",position)

##指针定位
position = file.seek(0,1)
str = file.read(10)
print("读取的数据：\n",str)

fid = file.fileno()
print("文件描述符：",fid)

is_tty = file.isatty()
print("是否是终端：",is_tty)

line = file.readline()
print("读取的数据：\n",line)



file.close()

# os.rename("IO\\input.py","IO\\input1.py")
# os.mkdir("IO\\test")
# time.sleep(1)
# os.rmdir("IO\\test")
os.chdir("IO")
print("当前工作目录：",os.getcwd())

