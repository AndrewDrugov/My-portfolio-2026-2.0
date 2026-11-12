import random

def selection_sort(data):
    n = len(data)
    for a in range(n - 1):
        m = data[a]  # start maximum
        p = a  # index of vibraniy element
        for b in range(a + 1, n):
            if m > data[b]:
                p = b
                m = data[b]
        if p != a:
            t = data[a]
            data[a] = data[p]
            data[p] = t

    return data


def bingo(data):
     max_ = len(data)-1#last element index
     nextValue = data[max_]#last element

     #firts go through
     for i in range(max_ - 1, -1, -1):
         if data[i] > nextValue:
             nextValue = data[i]

     #push barrier to the left skip all element = max
     while max_ and data[max_] == nextValue:
         max_ -= 1
     while max_:
        value = nextValue
        nextValue = data[max_]
        #next go throughs
        for i in range(max_ - 1, -1, -1):
            if data[i] == value:#if was foun elemet wich was equal to our maximum
                data[i],data[max_] = data[max_],data[i]#switch their place with the right border aktiv
                max_ -= 1#and push the border to the left
            elif data[i] > nextValue:
                nextValue = data[i]
        while max_ and data[max_] == nextValue:
            max_ -= 1
     return data




def blinchiki(data):
    if len(data)>1:
        for size in range(len(data),1,-1):
            maxindex = max(range(size),key=data.__getitem__)#searching for index of max in activ zone
            if maxindex +1!= size:
                if maxindex != 0:
                    data[:maxindex + 1] = reversed(data[:maxindex + 1])
                data[:size] = reversed(data[:size])
    return data


data = [213,123,32,676,1234,97842,90347,12745,14,134,341,341,134,134,134,14,43,1345,23,27,772,7,2,6727]
def insertion(data):
    max_ = len(data)
    for i in range(1, max_):
        for j in range(i, 0, -1):
            if data[j]<data[j-1]:
                data[j], data[j-1] = data[j - 1], data[j]
            else:
                break
    return  data

def benarij(data):
    max_ = len(data)
    for i in range(1, max_):
        key = data[i]
        lo, hi = 0, i - 1
        while lo <=hi:
            mid = (lo + hi)//2
            if key<data[mid]:
                hi = mid-1
            else:
                lo = mid+1
        for j in range(i, lo, -1):
            data[j] = data[j - 1]
            data[lo] = key
    return data

def buble(data):
    max_ =len(data)
    for i in range(0, max_ - 1):
        for j in range(0, max_-1-i):
            if data[j]>data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
    return data

def merge_list(a,b):
    c=[]
    N=len(a)
    M=len(b)
    i= 0
    j= 0
    while i < N and j < M:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1                #Создай свою рекурсивную функцию, выводом которой будет не отсортированный массив чисел. Отсортируй его с помощью метода слияния.
        #             Посчитай все уровни рекурсии, которые
# были достигнуты в работе этой программы.

        else:
            c.append(b[j])
            j += 1
    c+=a[i:]+b[j:]
    return c

def split_merge(data):
    N = len(data)//2
    a, b = data[:N], data[N:]
    global k
    if len(a) > 1:
        k+=1
        a = split_merge(a)
    if len(b) > 1:
        k += 1
        b = split_merge(b)
    return merge_list(a,b)

def random_list(n, begin = 50, end = 1000):
     if n == 0:
         return []
     massiv = random_list(n-1)
     a = random.randint(begin,end)
     massiv.append(a)
     return massiv

def hoar_sort(data):
    if len(data) > 1:
        x=random.choice(data)
        #x = data[random.randint(0,len(data)-1)]

        low = [ i for i in data if i<x]
        eq = [ i for i in data if i==x]
        high = [ i for i in data if i>x]

        data = hoar_sort(low) + eq + hoar_sort(high)
    return data


# k = 0
# print(split_merge(random_list(996)))
# print(k)
print(hoar_sort(data))
