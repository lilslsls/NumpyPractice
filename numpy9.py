import numpy as np

#计算正弦、余弦、正切
x=np.array([0., 1., 30, 90])
print ("sine:", np.sin(x))
print("cosine:", np.cos(x))
print("tangent:", np.tan(x))

#计算反正弦、反余弦、反正切
x = np.array([-1., 0, 1.])
print("arcsine:",np.arcsin(x))
print("arccosine:",np.arccos(x))
print("arctangent:",np.arctan(x))

#将角度从弧度转换为度数
x=np.array([-np.pi,-np.pi/2,np.pi/2,np.pi])
out1=np.degrees(x)
out2=np.rad2deg(x)
assert np.array_equiv(out1,out2)
print(out1)

#将角度从度数转换为弧度
x=np.array([-180.,-90.,90.,180.])
out1=np.radians(x)
out2=np.deg2rad(x)
assert np.array_equiv(out1,out2)
print(out1)
