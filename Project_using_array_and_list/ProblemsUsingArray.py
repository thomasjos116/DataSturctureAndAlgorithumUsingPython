# How  to check the number that conatins in the array or not 

import numpy as np

sample_array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def find_number(array, number):
    for i in range(len(array)):
        if array[i] == number:
            print(i)

find_number(sample_array, 20)


# 2)max poroduct of two integers in the array 

def maximum_product(sample_array):
    max1,max2 = 0,0
    for num in sample_array:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return max1 * max2

print(maximum_product(sample_array))

# 3)return the list without first and last elemets 
def middle(lst):
    return lst[1:-1]
    
myList = [1,2,3,4]
print(middle(myList))

# 4)find the sum of the diagonal elements in the 2D array

def diagonal_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    print(sum)
    
myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
diagonal_sum(myList2D)

# 5)find the best two values from the list :


def first_second(my_list):
    max1,max2 = float('-inf'),float('-inf')
    for num in my_list:
        if num > max1:
            max2 =max1
            max1 = num
        elif num > max2 and num != max1 :        
            max2 = num
    return max1, max2
my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(my_list))
