# coding=utf-8
from numpy import shape, zeros
import matplotlib.pyplot as plt
import pca


sampMtx=pca.loadDataSet("testSet3.txt")
lowDDataMat, reconMat=pca.pca(sampMtx,2)
print shape(lowDDataMat)
print lowDDataMat
print '-------'
print reconMat
fig =plt.figure()
ax= fig.add_subplot('221')
ax.scatter(sampMtx[:,0].flatten().A[0],sampMtx[:,1].flatten().A[0],s=10)
y= zeros(shape(lowDDataMat))
ax.scatter(reconMat[:,0].flatten().A[0],reconMat[:,1].flatten().A[0],marker='o',s=10,c='red')
ax2= fig.add_subplot('222')
ax2.scatter(lowDDataMat[:].flatten().A[0],y[:],s=10,c='green')

print '变换后的坐标'
ax= fig.add_subplot('223')
ax.scatter(reconMat[:,0].flatten().A[0],reconMat[:,1].flatten().A[0],s=10)

fig.show()