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


