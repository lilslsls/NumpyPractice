import numpy as np

#点乘 矩阵相乘 内积 * 等
x = [3,2]
y = [[4, 1], [2, 2]]
print (np.dot(x, y))
print (np.dot(y, x))
print (np.matmul(x, y))
print (np.matmul(y, x))
print (np.inner(x, y))
print (np.inner(y, x))
x = np.array([[1, 4], [5, 6]])
y = np.array([[4, 1], [2, 2]])
print (np.vdot(x, y))
print (np.vdot(y, x))
print(x.flatten())
print (np.dot(x.flatten(), y.flatten()))
print (np.inner(x.flatten(), y.flatten()))
print ((x*y).sum())
print(x*y)
x = np.array(['a', 'b'], dtype=object)
y = np.array([1, 2])
print (np.inner(x, y))
print (np.inner(y, x))
print (np.outer(x, y))
print (np.outer(y, x))

#cholesky分解
x = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]], dtype=np.int32)
print(x)
L = np.linalg.cholesky(x)
print (L)
assert np.array_equal(np.dot(L, L.T.conjugate()), x)

#qr分解
x = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]], dtype=np.float32)
q, r = np.linalg.qr(x)
print ("q=\n", q, "\nr=\n", r)
assert np.allclose(np.dot(q, r), x)

#svd分解
x = np.array([[1, 0, 0, 0, 2], [0, 0, 3, 0, 0], [0, 0, 0, 0, 0], [0, 2, 0, 0, 0]], dtype=np.float32)
U, s, V = np.linalg.svd(x, full_matrices=False)
print ("U=\n", U, "\ns=\n", s, "\nV=\n", V)
assert np.allclose(np.dot(U, np.dot(np.diag(s), V)), x)

#计算特征值和特征向量
x = np.diag((1, 2, 3))
eigenvals = np.linalg.eig(x)[0]
print(eigenvals)
eigenvals_ = np.linalg.eigvals(x)
assert np.array_equal(eigenvals, eigenvals_)
print ("eigenvalues are\n", eigenvals)
eigenvecs = np.linalg.eig(x)[1]
print ("eigenvectors are\n", eigenvecs)
print(np.dot(x,eigenvecs))
print(eigenvals*eigenvecs)

#计算f范数和矩阵条件数
x = np.arange(1, 10).reshape((3, 3))
print (np.linalg.norm(x, 'fro'))
print (np.linalg.cond(x, 'fro'))

#计算行列式
x = np.arange(1, 5).reshape((2, 2))
out1 = np.linalg.det(x)
out2 = x[0, 0] * x[1, 1] - x[0, 1] * x[1, 0]
assert np.allclose(out1, out2)
print (out1)

#计算矩阵的秩
x = np.eye(4)
print(x)
out1 = np.linalg.matrix_rank(x)
out2 = np.linalg.svd(x)[1].size
assert out1 == out2
print (out1)

#计算行列式的符号和自然对数
x = np.arange(1, 5).reshape((2, 2))
sign, logdet = np.linalg.slogdet(x)
det = np.linalg.det(x)
assert sign == np.sign(det)
assert logdet == np.log(np.abs(det))
print (sign, logdet)

#计算矩阵的逆
x = np.array([[1., 2.], [3., 4.]])
out1 = np.linalg.inv(x)
assert np.allclose(np.dot(x, out1), np.eye(2))
print (out1)

