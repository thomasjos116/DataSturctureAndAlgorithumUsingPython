# How  to check the number that conatins in the array or not 


def maximum_product(sample_array):
    max1,max2 = 0,0
    for num in sample_array:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return max1 * max2
arr = [10,12,3, 5, 17, 3, 21]

print(maximum_product(arr))


