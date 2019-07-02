# a=[2,4,7,1,3,5]
# for i in range(len(a)-1):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
#     print(a)

import  random
import time
a=[]
for i in  range(10000):
    a.append(random.randint(0,10000))
print(a)
start=time.time()
for i in range(len(a)-1):
    count=0
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            count+=1
            a[i],a[j]=a[j],a[i]
    if  count==0:
        break
print(a)
end=time.time()
print(end-start)



