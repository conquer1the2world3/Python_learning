import os,sys

##检查文件权限
ret = os.access("IO\\input.py",os.F_OK)
print("F_OK",ret)

ret = os.access("IO\\input.py",os.R_OK)
print("R_OK",ret)

ret = os.access("IO\\input.py",os.W_OK)
print("W_OK",ret)

ret = os.access("IO\\input.py",os.X_OK)
print("X_OK",ret)

##切换工作目录
retval = os.getcwd()
print("当前工作目录：",retval)
retval = os.chdir("D:\\Python_learning\\OS")
print("当前工作目录：",retval)

retval = os.getcwd()
print("当前工作目录：",retval)






