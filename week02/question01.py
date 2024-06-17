def max_kernel(num_list, k):
    result = []
    window = []

    # Handling edge cases
    if k <= 0 or not num_list:
        return result
   # Traverse through each element in num_list
    for i in range(len(num_list)):
             # Remove elements outside 
        if i >= k:
            window.pop(0)
        # Add the current element 
        window.append(num_list[i])
        # Find the maximum element 
        if len(window) == k:
            max_in_window = max(window)
            result.append(max_in_window)

    return result

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))  # 
