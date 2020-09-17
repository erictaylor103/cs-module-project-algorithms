'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    #optimized version 1
    for i in range(0, len(arr)):
        if arr.count(arr[i]) == 1:
            return arr[i]
    
    else:
        return None


    #optimized version 2
    #create a dictionary key, value
    #dict = {

    #}
    #for num in arr:
        # if num is in the dict add a 1 to the num count
        #the 1 we added to the num count will be the value in
        #the key, value pairs in the dict
        #so we know how many times that num appears in dict
    #    if num in dict:
    #        dict[num] = dict[num] + 1
        #if num is not in dict, add num to the dict
    #    else:
    #        dict[num] = 1
#ask why I am comparing the key insteads of the value
#key should be the num and value the ampunt of times num appears in the list

    #for key, value in dict.items():
    #    print(key, value)
    #    if dict[key] == 1:
    #        return key


    #simple naive solution
    #O(n^2)
    #for num in arr: #O(n)
     #   if arr.count(num) == 1: #O(n)
    #        return num

    #using XOR
    #result = 0  
    #for i in arr:  
    #    result ^= i  #what does the XOR do and how it works exactly
    #return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")