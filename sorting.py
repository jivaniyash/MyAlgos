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
            