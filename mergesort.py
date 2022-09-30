def mergesort(lst):
    if len(lst)>1:
        mid=len(lst)//2
        l=lst[:mid]
        r=lst[mid:]
        mergesort(l)
        mergesort(l)
        i=0
        j=0
        k=0
        while i<len(l) and j<len(r):
            if l[i]<=r[j]:
                lst[k]=l[i]
                i+=1
            else:
                lst[k]=r[j]
                j+=1
                k+=1
        while i<len(l):
            lst[k]=r[j]
            j+=1
            k+=1
        return lst
n=int(input("enter number of elements:"))
l=[]
for i in range(n):
    ele=int(input("enter elements:"))
    l.append(ele)
print(mergesort(l))
        	