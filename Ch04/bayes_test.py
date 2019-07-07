# coding=utf-8
import bayes

dateset,vec=bayes.loadDataSet()
print dateset
print '--词集，不考虑出现次数'
val_set= bayes.createVocabList(dateset)
print val_set
print '--每篇的词集向量 '
word_vec =bayes.setOfWords2Vec(val_set,dateset[0])
print word_vec
traindoc=[]
for doc in dateset:
    traindoc.append(bayes.setOfWords2Vec(val_set,doc))
p0_v,p1_v,p_ab= bayes.trainNB0(traindoc, vec)
print p_ab
print p0_v
print p1_v

print '-- test'
bayes.testingNB()
print '--测试垃圾邮件'
bayes.spamTest()
