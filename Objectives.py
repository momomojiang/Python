# Countdown - Create a function that accepts a number as an input. 
#  Return a new array that counts down by one, from the number
#  (as arrays 'zero'th element) down to 0 (as the last element).  
#  For example countDown(5) should return [5,4,3,2,1,0].
def countdown(num):
    a=[]
    for x in range(num,0,-1):
        a.append(x)
    print(a)

countdown(5)

		
# Print and Return - Your function will receive an array with two numbers.
# Print the first value, and return the second.
def printAndReturn(arr):
	print(arr[0])
	return arr[1]
a=printAndReturn([1,2])
print(a)



# First Plus Length - Given an array, return the sum of the first 
# value in the array, plus the array is length.
def firstPlusLength(arr):
	sum=arr[0]+len(arr)
	print(sum)
firstPlusLength([1,2])


# Values Greater than Second - Write a function that accepts any array, 
# and returns a new array with the array values that are greater 
# than its 2nd value.  Print how many values this is.  
# If the array is only one element long, have the function return False
def greater(arr):
    newArr=[]
    if len(arr)<=1:
		    return False
    else:
        for i in range(len(arr)-1):
            if arr[i]<arr[i+1]:
                newArr.append(arr[i+1])
        print("newArr length is " + str(len(newArr)) + " and each value is " + str((newArr)))
        
        return newArr
        
# greater([2,4,5,6])
f = greater([2,4,5,6])
print(f)
# newArr length is 3 and each value is [4, 5, 6]
# [4, 5, 6]
   


def greater(arr):
    newArr=[]
    if len(arr)<=1:
            return False
    else:
        for i in range(len(arr)):
            if arr[i]>arr[1]:
                newArr.append(arr[i])
        print("newArr length is " + str(len(newArr)) + " and each value is " + str((newArr)))
        
        return newArr
        
# greater([2,4,5,6])
f = greater([2,4,5,6])
print(f)
# newArr length is 2 and each value is [5, 6]
# [5, 6]
 

# This Length, That Value - Write a function called 
# lengthAndValue which accepts two parameters, size and value. 
# This function should take two numbers and return a list of 
# length size containing only the number in value. 
# For example, lengthAndValue(4,7) should return [7,7,7,7].
def lengthAndValue(size,value):
    arr=[]
    i=1
    for i in range(size):
	      arr.append(value)
    arr[0]=4
    print(arr)

lengthAndValue(4,7)




