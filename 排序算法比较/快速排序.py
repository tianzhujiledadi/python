# def  kuaisu(n):
#     while len(n)<2:
#         return n
#     list1=[]
#     list2=[]
#     middle=n.pop(0)
#     for i in n:
#         if  middle>i:
#             list1.append(i)
#         else:
#             list2.append(i)
#     return  kuaisu(list1)+[middle]+kuaisu(list2)
# if __name__ == '__main__':
#     import  random
#     import time
# list=[]
# for i in  range(10000):
#     list.append(random.randint(0,10000))
# print(list)
# start=time.time()
# print(kuaisu(list))
# end=time.time()
# print(end-start)
import  random
import time
list=[]
for i in  range(10000):
    list.append(random.randint(0,10000))
print(list)
start=time.time()
#a=sorted(list)
#print(a)
list.sort()
print(list)
end=time.time()
print(end-start)
#而Python里的sort排序是一种名为Timsort的排序方法，其时间复杂度为O(n log n)，而且这是一种快速的稳定的排序方法。
# 它的发明者是Tim Peters在2001年为Python创造的一种排序算法。下图是Timsort的时间复杂度的介绍，
# 可以看到Timsort排序在各方面都是最优的。而且Timsort是在C语言中实现的，因此Timsort排序的性能是毋庸置疑的。
#Timsort在排序长度低于64的时候采取：插入排序 。高于64的时候采取Timsort是一种改良的归并排序。
