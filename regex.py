import re
print(re.match(r'www','www.baidu.com').span())
print(re.match(r'com','www.baidu.com'))

print(re.search(r'www','www.baidu.com').span())
print(re.search(r'com','www.baidu.com').span())

line = "Cats are smarter than dogs"

searchObj = re.search(r'(.*) are (.*?) .*',line,re.M|re.I)

if searchObj:
    print("search --> searchObj.group() : ", searchObj.group())
    print("search --> searchObj.group(1) : ", searchObj.group(1))
    print("search --> searchObj.group(2) : ", searchObj.group(2))
else:
    print("No match!!")

phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print("电话号码是 : ", num)

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)


# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'a12b26c300'
print(re.sub(r'(?P<value>\d+)',double,s))

# 查找字符串中的所有数字
pattern = re.compile(r'\d+')
print(pattern.findall('runoob 123 google 456'))
print(pattern.findall('run88oob123google456',0,10))

result = re.findall(r'\d+','runoob 123 google 456')
print(result)

it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
    print(match.group())


s = re.split(r'\s+','runoob google taobao')
print(s)
s = re.split(r'a','runoob google taobao')
print(s)


