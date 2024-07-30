def selection_sort(arr, n):
    for i in range(n-1):
        mini = i
        for j in range(i, n):
            if(arr[j]<arr[mini]):
                mini=j
        arr[mini],arr[i]=arr[i],arr[mini]        
        print(i, ": ", arr)

n = int(input("Enter the Size of array: "))
x = input("Enter the Array Values: ")
arr = [int(val) for val in x.split()]
selection_sort(arr, n)
print(arr)