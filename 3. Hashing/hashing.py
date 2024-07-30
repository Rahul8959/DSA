# def count_occurrences(array):
#     # Initialize an empty dictionary to store counts
#     counts = {}
    
#     # Iterate through each element in the array
#     for value in array:
#         # If the value is already in the dictionary, increment its count
#         if value in counts:
#             counts[value] += 1
#         # If the value is not in the dictionary, add it with a count of 1
#         else:
#             counts[value] = 1
    
#     return counts

# # Example usage
# array = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# counts = count_occurrences(array)
# print(counts)

def frequencyCount(arr, N, P):
    # code here\
    count = {}
    
    for val in arr:
        if(val in count):
            count[val] += 1
        else:
            count[val]=1
            
    return count

arr = [2,3,2,3,5]
n=5
p=5
tmp = frequencyCount(arr,n,p)
print(tmp)

for i in tmp:
    print(tmp[i])

count = [0]*n

print(count[0])