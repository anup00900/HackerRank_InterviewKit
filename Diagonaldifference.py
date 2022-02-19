def diagonalDifference(arr):
    # Write your code here
    dia1=0
    dia2=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if i==j:
                dia1=dia1+arr[i][j]
    i=0
    j=len(arr)-1
    while j>=0:
        dia2=dia2+arr[i][j]
        j=j-1
        i=i+1
    
    return abs(dia2-dia1)    
              