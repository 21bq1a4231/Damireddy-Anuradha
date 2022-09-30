def insertion_sort(lst):
    for i in range(1,len(lst)):
        x=lst[i]
        j=i-1
        while j>0 and x<lst(j):
            lst[j+1]=lst[j]
            j=i-1
            lst[j+1]=x
        return lst
n=int(input("enter number of elements:"))
lst=[]
for i in range(n):
    ele=int(input("enter elements:"))
    lst.append(ele)
print(insertion_sort(lst))