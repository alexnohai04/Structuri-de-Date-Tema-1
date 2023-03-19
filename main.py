import random
import time

def radix_sort(L):
    start=time.time()
    if len(L) == 0:
        return L

    cifra_max = len(str(max(L)))
    for i in range(cifra_max):
        buckets = [[] for _ in range(10)]
        for nr in L:
            cifra = (nr // (10 ** i)) % 10
            buckets[cifra].append(nr)
        L = [nr for bucket in buckets for nr in bucket]
    stop=time.time()
    return L,(stop-start)


def merge(L):
    start=time.time() 

    def MergeSort(L):
        if len(L) <= 1:
            return L

        mij = len(L) // 2
        st = L[:mij]
        dr = L[mij:]

        st = MergeSort(st)
        dr = MergeSort(dr)

        return Merge(st, dr)

    def Merge(st, dr):
        rezultat = []
        i = j = 0

        while i < len(st) and j < len(dr):
            if st[i] < dr[j]:
                rezultat.append(st[i])
                i += 1
            else:
                rezultat.append(dr[j])
                j += 1

        rezultat += st[i:]
        rezultat += dr[j:]
        return rezultat

    L2=MergeSort(L)
    stop=time.time()
    return L2,(stop-start)

def shell_sort(L):
    start=time.time()
    n = len(L)
    distanta = n // 2

    while distanta > 0:
        for i in range(distanta, n):
            temp = L[i]
            j = i

            while j >= distanta and L[j - distanta] > temp:
                L[j] = L[j - distanta]
                j -= distanta

            L[j] = temp
        distanta //= 2
    stop=time.time()
    return L,(stop-start)


def count_sort(L):
    start=time.time()
    max_val = max(L)

    fr = [0] * (max_val + 1)
    for num in L:
        fr[num] += 1

    L_sortat = []
    for i in range(max_val + 1):
        L_sortat += [i] * fr[i]
    stop=time.time()
    return L_sortat,(stop-start)

def bubble_sort(L):
    start=time.time()
    n = len(L)
    for i in range(n):
        for j in range(n - i - 1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    stop=time.time()
    return L,(stop-start)
NrMax=int(input("NrMax="))
NrElemente=int(input("NrElemente="))
# L=[random.randint(1, NrMax) for i in range(NrElemente)]
L=[i for i in reversed(range(NrElemente))]
print(L)
L1,t1=radix_sort(L)
L2,t2=merge(L)
L3,t3=shell_sort(L)
L4,t4=count_sort(L)
L5,t5=bubble_sort(L)
start=time.time()
L6=sorted(L)
stop=time.time()
t6=stop-start

T=[]
T.append(("Radix=",t1))
T.append(("Merge=",t2))
T.append(("Shell=",t3))
T.append(("Count=",t4))
T.append(("Bubble=",t5))
T.append(("Implicit=",t6))

print("L sortata=",L1)
print("L Merge=",L2)
print("L Shell=",L3)
print("L Count=",L4)
print("L Bubble=",L5)
print("L Implicit=",L6)

k=1
T.sort(key =lambda x:x[1])
for el in T:
    print (f"{k}.)",*el)
    k = k + 1
