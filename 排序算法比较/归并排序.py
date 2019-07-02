def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1
    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    #print(c,'!!!!')
    return c
def merge_sort(lists):
    if len(lists) <2:
        #print(lists,'****')
        return lists
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    #print(left,right,'&&&&')
    return merge(left, right)
if __name__ == '__main__':
    import random
    import time
lists = []
for i in range(10000):
    lists.append(random.randint(0, 10000))
print(lists)
start=time.time()
print(merge_sort(lists))
end=time.time()
print(end-start)

