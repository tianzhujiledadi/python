
def  charu(list):
    for i in range(1,len(list)):   #代表从下标为1的位置开始拿数与前面的比较，再拿下标为2的数与前面的数进行比较
        for j in range(i,0,-1):
            if list[j]<list[j-1]:
                list[j],list[j-1]=list[j-1],list[j]
    print(list)
if __name__ == '__main__':
    import  random
    import time
list=[]
for i in  range(10000):
    list.append(random.randint(0,10000))
print(list)
start=time.time()
charu(list)
end=time.time()
print(end-start)
