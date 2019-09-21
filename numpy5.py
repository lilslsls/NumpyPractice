import numpy as np
from datetime import date
#打印今天的日期
print(date.today())

#单个数组文件存储与读取
x=np.arange(10)
print(x)
np.save('temp.npy',x)
import os
if os.path.exists('temp.npy'):
    x2=np.load('temp.npy')
    print(x2)
    print(np.array_equal(x,x2))
#多个数组文件存储与读取
x=np.arange(10)
y=np.arange(11,12)
print(x)
print(y)
np.savez('temp1.npz',x=x,y=y)

with np.load('temp1.npz')as data:
    x2=data['x']
    y2=data['y']
    print(np.array_equal(x,x2))
    print(np.array_equal(y,y2))

#单个数组文件存储与读取 txt
x=np.arange(10).reshape(2,5)
header='num1 num2 num3 num4 num5'
np.savetxt('temp.txt',x,fmt="%d",header=header)
y=np.loadtxt('temp.txt')
print(y)

# 多个数组文件存储与读取 txt
x = np.arange(10)
y = np.arange(11, 21)
z = np.arange(22, 32)
np.savetxt('temp.txt', (x, y, z), fmt='%d')
d=np.loadtxt('temp.txt')
print(d)

#数组转bytes bytes转数组
x = np.array([1, 2, 3, 4])
x_bytes = x.tostring() 
print(x_bytes)
x2 = np.fromstring(x_bytes, dtype=x.dtype)
print(np.array_equal(x, x2))

#数组列表转换
a=[[1,2],[3,4]]
x=np.array(a)
a2=x.tolist()
print(a==a2)

#数组字符串转换
x = np.arange(10).reshape(2,5)
x_str = np.array_str(x)
print(x_str, "\n", type(x_str))
x_str = x_str.replace("[", "") 
x_str = x_str.replace("]", "")
print(x_str)
x2 = np.fromstring(x_str, dtype=x.dtype, sep=" ").reshape(x.shape)
assert np.array_equal(x, x2)

#设定精度打印所有元素
x = np.random.uniform(size=[10,100])
np.set_printoptions(precision=2, suppress=True)
print(x)

#将数字转换为二进制 十六进制
out1 = np.binary_repr(12)
out2 = np.base_repr(12, base=2)
assert out1 == out2 
print(out1)
print(out2)
out3 = np.base_repr(1100, base=16)
print(out3)