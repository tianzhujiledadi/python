# 希尔排序每个无序部分还是按照插入排序写的
def shell_sort(alist):
    """希尔排序"""
    n = len(alist)  # n=9
    gap = n // 2  # 间隔取队列长度的一半，下一次再取，  gap=4
    # 这个while循环控制的是gap变化到1的过程中执行的次数
    while gap >= 1:  # 步长需要取到1，因为2个子序列有序不意味着两个子序列合到一起之后也是有序的
        # 希尔算法，与普通插入算法的区别就是gap步长。
        for j in range(gap, n):  # 外层循环控制的是所有子序列的所有元素
            i = j
            # 内层循环控制的是子序列执行的特定算法的比较和交换
            while i >= gap:  # while i>0:  他比较到最前端的一个元素时停止比较
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2  # 缩短gap步长
if __name__ == '__main__':
    import  random
    import time
alist=[]
for i in  range(10000):
    alist.append(random.randint(0,10000))
print(alist)
start=time.time()
shell_sort(alist)
print(alist)
end=time.time()
print(end-start)