import numpy as np

#判断数组是否有0元素
x = np.array([1,2,3])
print (np.all(x))
x = np.array([1,0,3])
print (np.all(x))
x = np.array([1,0,0])
print (np.any(x))
x = np.array([0,0,0])
print (np.any(x))

#测试元素的有限性（不是无穷大或不是数字） 元素级别的为NaN测试并将结果作为布尔数组返回 对正或负无穷大进行元素级别测试
x = np.array([1, 0, np.nan, np.inf])
print(x)
print (np.isfinite(x))
print(np.isnan(x))
print(np.isinf(x))



#数组类型测试
# iscomplex(x) 返回一个bool数组，如果输入元素很复杂，则返回True
# isreal(x) 返回一个bool数组，如果输入元素是实数，则返回True。
# isscalar(num) 如果num的类型是标量类型，则返回True。
x = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
print(":::::::/n")
print(np.iscomplex(x))
print(np.isreal(x))
print(np.isscalar(3))
print(np.isscalar([3]))
print(np.isscalar(True))

#且 或 异或 非
print (np.logical_and([True, False], [False, False]))
print (np.logical_or([True, False, True], [True, False, False]))
print (np.logical_xor([True, False, True], [True, False, False]))
print (np.logical_not([True, False, 0, 1]))

#比较大小
x = np.array([4, 5])
y = np.array([2, 5])
print (np.greater(x, y))
print (np.greater_equal(x, y))
print (np.less(x, y))
print (np.less_equal(x, y))
print (np.equal([1, 2], [1, 2.000001]))
print (np.isclose([1, 2], [1, 2.000001]))
123
