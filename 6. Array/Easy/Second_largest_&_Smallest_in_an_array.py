def second_largest(arr,n):
    largest = arr[0]
    slargest = -1
    for i in range(n):
        if(arr[i]>largest):
            slargest = largest
            largest = arr[i]
        elif(arr[i]<largest and arr[i]>slargest):
            slargest=arr[i]

    return slargest

def second_smallest(arr,n):
    smallest = float('inf')
    ssmallest = float('inf')

    for i in range(n):
        if (arr[i]<smallest):
            ssmallest = smallest
            smallest = arr[i]
        elif (arr[i]<ssmallest and arr[i] != smallest):
            ssmallest = arr[i]
    return ssmallest



x = input("Enter array items: ")
arr = [int(i) for i in x.split()]
print("Second Largest: ",second_largest(arr,len(arr)))
print("Second Smallest: ", second_smallest(arr, len(arr)))