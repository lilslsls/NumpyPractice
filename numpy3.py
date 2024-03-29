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

#字符串居中，左，右,大小填充为20
x=np.array(['hello world','say something'],dtype=str)
centered=np.char.center(x,20,fillchar="1")
left=np.char.ljust(x,20,fillchar='2')
right=np.char.rjust(x,20,fillchar="3")
print("centered:",centered,"\nleft:",left,"\nright:",right)

#cp500 编码解码
x=np.array(['hello world','say something'],dtype=str)
encoded=np.char.encode(x,'cp500')
decoded=np.char.decode(encoded,'cp500')
print("encoded:",encoded,"\ndecoded:",decoded)

#通过指定分隔符来连接数组中的元素
x=np.array(['hello world','say something'],dtype=str)
out=np.char.join("  ",x)
print(out)

#移除字符串空格
x=np.array(['  hello world ',' say something '],dtype=str)
out1=np.char.strip(x)
out2=np.char.lstrip(x)
out3=np.char.rstrip(x)
print("out1:",out1,"\nout2:",out2,"\nout3:",out3)

#分离字符串字符,按换行符分割
x=np.array(['hello \nmy name is world'],dtype=str)
out=np.char.splitlines(x)
print(out)

#字符填充
x=np.array(['343'],dtype=str)
zfill=np.char.zfill(x,7)
print(zfill)

#字符串替换字符
x=np.array(['hello my name is ls' ],dtype=str)
out=np.char.replace(x,"ls","s")
print(out)

#比较2个数组中的字符
x1=np.array(['hello','my','name','is','join'],dtype=str)
x2=np.array(['hello','my','name','is','joi'],dtype=str)
out=np.char.equal(x1,x2)
print(out)

x1=np.array(['hello','my','name','is','join'],dtype=str)
x2=np.array(['hello','my','name','is','joi'],dtype=str)
out=np.char.not_equal(x1,x2)
print(out) 

#计算字符中指定字母的数目
x1=np.array(['hello','my','name','is','join'],dtype=str)
out=np.char.count(x1,"n")
print(out)

#找出指定字母在字符中出现的第一个位置
x1=np.array(['henllo','my','name','is','jnoin'],dtype=str)
out=np.char.find(x1,"n")
print(out)

#检查字符是否仅由数字或小写字母或大写字母组成
x=np.array(["Hello","you","Are","20","Years","old"],dtype=np.str)
out1=np.char.isdigit(x)
out2=np.char.isupper(x)
out3=np.char.islower(x)
print(out1,"\n",out2,"\n",out3)
    
#检查字符串是否是以指定子字符串开头
x=np.array(["he",'his',"him",'his'],dtype=np.str)
out=np.char.startswith(x,"hi")
print(out)