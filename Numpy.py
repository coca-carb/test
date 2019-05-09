import numpy as np
import matplotlib.pyplot as plt
'''
array
'''
data=[1,2,3,4,5,6,7,8,9,10]
a=np.array(data)#将list转换为array
b=np.arange(1,10,2)#生成1到10，步长为2的array
c=np.reshape(a,(2,5))#将a重塑2行5列
#c=np.arange(10).reshape((2,5))
d=c.T #转置

#切片操作
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])

#条件逻辑式表述为数组运算 np.where(condition,x,y)
def where_test():
    A=0;B=0;C=1
    #aa=1;bb=2;cc=3;result=0
    D=[A,B,C]
    if D.count(0)==0:
        print('0')
    elif D.count(0)==1:
        print('1')
    elif D.count(0)==2:
        print('2')
    else:
        print('3')

    print(np.where(D.count(0)==0,0,np.where(D.count(0)==1,1,np.where(D.count(0)==2,2,3))))
    #result=np.where(D.count(0)==0,0,np.where(D.count(0)==1,aa,np.where(D.count(0)==2,aa+bb,aa+bb+cc)))
    #print(result)

#统计方法 mean sum std var max argmax.....
#print(min(a),np.argmax(data))#最大值元素的索引

#集合逻辑 np.in1d(x,y) 得到一个表示“x是否包含于y”的布尔型数组 就是x是否在y里
def in1d_test():
    a=[1,4,10,2,8,11]
    b=[2,3,4]
    print(sum(np.in1d(b,a))/len(b))

'''
numpy 高级应用
'''
#数组的合并 np.concatenate([arr1,arr2],axis=0/1) 0行合并  1列合并
#拆分  one,two,three=np.split(arr,[1,3])

#广播  (如果两个数组的后缘维度的轴长度相符或其中一方长度为1，则广播兼容)
def boardcast():
    arr = np.random.randn(4,3)
    print(arr)
    print(arr.mean(0))
    demeaned = arr - arr.mean(0)

    arr_0 = arr.mean(0)[np.newaxis,:]#要广播的轴在哪里，newaxis就在哪里
    print(arr_0)
    demeaned_0 = arr - arr_0
    print(demeaned)
    print(demeaned_0)

    rowmean = arr.mean(1).reshape((4,1))
    rowmean_1 = arr.mean(1)[:,np.newaxis]
    rowmeaned = arr - rowmean
    rowmeaned_1 = arr - rowmean_1

    print("*"*50)
    print(rowmeaned)
    print(rowmeaned_1)

boardcast()


