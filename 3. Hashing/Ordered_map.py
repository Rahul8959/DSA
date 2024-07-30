from collections import OrderedDict

def frequencyCount(arr, N):
    # Create an ordered dictionary to store the frequency of each element
    hash_map = OrderedDict()
    
    # Iterate through the array and count the occurrences of each element
    for num in arr:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1
    
    # Print the ordered dictionary (for debugging purposes)
    print("Ordered Dictionary with Frequencies:")
    for key, value in hash_map.items():
        print(f'{key}: {value}')
    
    # Update the array with the frequency counts for elements 1 to N
    for i in range(1, N + 1):
        if i in hash_map:
            arr[i - 1] = hash_map[i]
        else:
            arr[i - 1] = 0

    # Print the final array (for debugging purposes)
    print("Updated Array with Frequencies:")
    print(arr)

# Example usage
arr = [7,2, 6, 6, 2, 3, 2, 3, 5,7,7,7,7,7]
N = len(arr)
frequencyCount(arr, N)
