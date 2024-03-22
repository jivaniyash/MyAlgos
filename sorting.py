'''
File to write Sorting Algorithms
'''

def bubble_sort(array: list):
    # loop through each element
    for i in range(len(array)):
        for j in range(len(array)-1): # inner loop (last element is in correct position)
            if array[j+1] < array[j]:  
                array[j+1], array[j] = array[j], array[j+1] # swaps the adjacent element
        
    return array

def selection_sort(array: list):
    # selects smallest element from the current iteration

    for i in range(len(array)):

        temp_min_index = i # assuming ith value as min value
        for j in range(i+1,len(array)):
            if array[j] < array[temp_min_index]:
                temp_min_index = j
        # swap ith index value with minumum value
        array[i], array[temp_min_index] = array[temp_min_index], array[i]
    
    return array

def insertion_sort(array: list):
    # loop through array consider each element & swap it the left value if its smaller until left most
    for i in range(len(array)-1):
        # if array[i+1] < array[i]:
        for j in range(i+1,0,-1): # loop through current index to start (backwards)
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    
    return array

def merge_sort(array: list):
    
    def divide(array, li, ri): # divide array into subarray
        subarray = array[li:ri]
        if len(subarray) > 1:
            mid_index = len(subarray) // 2

            divide(array, li, li+mid_index) # left 
            divide(array, li+mid_index, ri) # right 

            merge(array, li, mid_index, ri) # merge subarrays & sort them

    def merge(array, li, mid_index, ri): # merge & sort subarray
        
        left_sub = array[li:li+mid_index]
        right_sub = array[li+mid_index:ri]

        # initiate left & right indexes to 0 & main array index to left_index (li)
        left_idx = right_idx = 0
        idx = li

        while left_idx < len(left_sub) and right_idx < len(right_sub): #loop until every item is merged and sorted
            if left_sub[left_idx] < right_sub[right_idx]: # if element of left array is less than right array
                array[idx] = left_sub[left_idx]
                left_idx += 1 # increment by 1 
            else: # if element of right array is less than left array
                array[idx] = right_sub[right_idx]
                right_idx += 1 
            idx += 1
            
        # if there are any remaining items in left or right
        
        while left_idx < len(left_sub):
            array[idx] = left_sub[left_idx]
            left_idx += 1
            idx += 1
        
        while right_idx < len(right_sub):
            array[idx] = right_sub[right_idx]
            right_idx += 1
            idx += 1
        
    divide(array, 0, len(array))
    return array

def quick_sort(array: list):
    # sorts array by picking pivot and calling recursively to make elements which are less than pivot to left and greater than pivot to right.

    def make_partition(array, left_index, right_index):
        # makes partition by swapping elements after comparing and returns the index of the pivot
        # pivot is always to the extreme right

        temp_pointer = left_index

        for i in range(left_index, right_index): # loop through each element

            if array[i] < array[right_index]: # compare if current element is less than pivot element
                array[i], array[temp_pointer] = array[temp_pointer], array[i] # swap with the temp_pointer

                # and move temp pointer to next index
                temp_pointer += 1
            
        # swap pivot with the correct location
        array[right_index], array[temp_pointer] = array[temp_pointer], array[right_index]
            
        return temp_pointer
    
    def recursive_call(array, left_index, right_index):
        if left_index < right_index:
            pivot = make_partition(array, left_index, right_index) # find pivot element from above function

            recursive_call(array, left_index, pivot-1) # left partition to sort

            recursive_call(array, pivot+1, right_index) # right partition to sort

    recursive_call(array, 0, len(array)-1)
    return array