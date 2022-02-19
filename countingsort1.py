def countingSort(arr):
    # Write your code here
    l=[0]*100
    for i in range(0,len(arr)):
        l[arr[i]]=l[arr[i]]+1
    return l    