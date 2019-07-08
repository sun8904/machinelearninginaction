# coding=utf-8
import numpy
import logRegres

dataMat, labelMat = logRegres.loadDataSet()
weights = logRegres.gradAscent(dataMat, labelMat)
print weights
#logRegres.plotBestFit(weights.getA())
weights =logRegres.stocGradAscent0(dataMat, labelMat)
print '--随机梯度'
#logRegres.plotBestFit(weights)

weights =logRegres.stocGradAscent1(dataMat, labelMat)
print '--改进的随机梯度'
logRegres.plotBestFit(weights)

import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111)

x = numpy.arange(-8.0, 8.0, 0.2)
print logRegres.sigmoid(-0.3)
# 设置偏移量 不是所有数据都是x=0划分
y= [logRegres.sigmoid(xi-0.1) for xi in x]
ax.plot(x, y)
plt.xlabel('X1');
plt.ylabel('X2');
#plt.show()
print '--预测病马'
logRegres.multiTest()