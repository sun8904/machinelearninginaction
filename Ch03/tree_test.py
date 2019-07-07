# coding=utf-8
import trees
import treePlotter

dateset, labels = trees.createDataSet()
print dateset
print labels
shannon = trees.calcShannonEnt(dateset)
print shannon
print '--条件熵'
ha = trees.calcShannonEnt(trees.splitDataSet(dateset, 0, 5))
hb = trees.calcShannonEnt(trees.splitDataSet(dateset, 0, 3))
hc = trees.calcShannonEnt(trees.splitDataSet(dateset, 0, 1))
hxy = 1.0 / 3 * ha + 1.0 / 4 * hb + 5.0 / 12 * hc
print ha, hb, hc
print hxy
print '--信息增益'
ig = shannon - hxy
print ig
print '--找到最佳分类特征'
feature = trees.chooseBestFeatureToSplit(dateset)
print   labels[feature]
print '--创建决策树'
labelsCopy = labels[:]
tree = trees.createTree(dateset, labelsCopy)
print tree
# print '--画图'
# treePlotter.createPlot(tree)
print '--用决策树测试数据'
#mytree = treePlotter.retrieveTree(0)
testdata = [4, 4, 1, 'cha']
label = trees.classify(tree, labels, testdata)
print label
print '--保存树'
trees.storeTree(tree,'houseTree')
print '--测试隐形眼镜类型'
fr= open('lenses.txt')
# for line in fr.readlines():
#     print line
#     row = line.strip().split('\t');
#     print row
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
len_labels=['age','prescript', 'astigmatic', 'tearRate']
len_tree=trees.createTree(lenses, len_labels)
print len_tree
print len_labels
treePlotter.createPlot(len_tree)
