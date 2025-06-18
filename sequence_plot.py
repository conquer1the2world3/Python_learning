import numpy as np
import matplotlib.pyplot as plt

# 计算数列
def calculate_sequence(n):
    return n**(1/n) - ((-1)**n/n)

# 生成数据点
n_values = np.arange(1, 101)  # 计算前100项
sequence_values = [calculate_sequence(n) for n in n_values]

# 创建图像
plt.figure(figsize=(10, 6))
plt.plot(n_values, sequence_values, 'b.-', label='n^(1/n)-((-1)^n/n)')
plt.grid(True)
plt.xlabel('n')
plt.ylabel('a(n)')
plt.title('数列 n^(1/n)-((-1)^n/n) 的图像')
plt.legend()

# 显示图像
plt.show() 