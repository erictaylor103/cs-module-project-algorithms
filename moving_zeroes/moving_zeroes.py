'''
Input: a List of integers
Returns: a List of integers
'''

#the order of the result array does not matter
#set an index or value that will traverse trough each
#item in the array, and if it finds a "0",
#then pop the "0" and append it to the back of the array 
#the index or value will start at the begining of the array


def moving_zeroes(arr):
    
    non_zeros = []
    zeros = []
    #check if arr is Not Empty
    
        #use "i" as a pointer to traverse trough "arr" (full length of the arr)
    for i in range(len(arr)):
        #if "i" is equal to 0, then append it to the zeros list
        if arr[i] == 0:
            zeros.append(arr[i])
        else:
        #otherwise append "i" to the "non-zeros" list
            non_zeros.append(arr[i])
    #combine arr with the non-zeros list and the zeros list
    arr = non_zeros + zeros
    
    #return the new comnined arr
    return arr
        

print(moving_zeroes([8, 1, 0, 3, 0, 12]))



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")