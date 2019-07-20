from __future__ import print_function
import numpy as np
#查看numpy版本
print(np.__version__)

#对两个数组的逐个字符串元素进行连接
x1=np.array(['hello','say'],dtype=np.str)
x2=np.array(['world','something'],dtype=np.str)
out=np.char.add(x1,x2)
print(out)

#返回按元素多重连接后的字符串
x=np.array(['hello','say'],dtype=np.str)
out=np.char.multiply(x,3)
print(out)

#字母大小写转换
x=np.array(['hello woRld','Say someThing'],dtype=np.str)
capitalized=np.char.capitalize(x)
lowered=np.char.lower(x)
uppered=np.char.upper(x)
swapcased=np.char.swapcase(x)
titlecased=np.char.title(x)
print("capitalized:",capitalized,"\nlowered:",lowered,'\nuppered:',uppered,"\nswapcased:",\
    swapcased,"\ntitlecased:",titlecased)
