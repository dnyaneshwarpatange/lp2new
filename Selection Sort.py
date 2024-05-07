# Function for Selection Sort of elements 
 
def Selection_Sort(array): 
    for i in range(len(array)): 
 
        # Find the minimum element in remaining unsorted array 
        min_idx = i 
        for j in range(i + 1, len(array)): 
            if array[min_idx] > array[j]: 
                min_idx = j 
 
        # Swap the minimum element with the first element 
        array[i], array[min_idx] = array[min_idx], array[i] 
     
 
# Main 
 
array=[] 
n = int(input("\nEnter number of element in Array : ")) 
 
print("\nEnter Elements in Array : ") 
for i in range(0, n): 
    ele = int(input()) 
    array.append(ele)  # adding the element 
 
print("\nArray Before Performing Selection Sort : ") 
print(array) 
 
print("\nArray After Performing Selection Sort : ") 
Selection_Sort(array) 
print(array) 