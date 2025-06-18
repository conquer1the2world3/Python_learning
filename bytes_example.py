# 创建字节字符串
byte_str = b'Hello World'
print("字节字符串:", byte_str)
print("类型:", type(byte_str))

# 字节字符串的索引和切片
print("\n第一个字节:", byte_str[0])  # 返回ASCII码值
print("前5个字节:", byte_str[:5])

# 字节字符串和普通字符串的转换
normal_str = "Hello World"
# 字符串转字节
bytes_from_str = normal_str.encode('utf-8')
print("\n字符串转字节:", bytes_from_str)

# 字节转字符串
str_from_bytes = bytes_from_str.decode('utf-8')
print("字节转字符串:", str_from_bytes)

# 字节字符串的常见操作
print("\n字节字符串长度:", len(byte_str))
print("是否包含特定字节:", b'World' in byte_str)

# 处理二进制数据示例
binary_data = b'\x48\x65\x6c\x6c\x6f'  # "Hello" 的十六进制表示
print("\n二进制数据:", binary_data)
print("解码为字符串:", binary_data.decode('utf-8')) 