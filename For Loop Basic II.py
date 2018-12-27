# Biggie Size - Given an array, write a function that changes 
# all positive numbers in the array to "big". 
# Example: makeItBig([-1, 3, 5, -5]) returns that same array, 
# changed to [-1, "big", "big", -5].
def big(arr):
	for i in range(len(arr)):
		if arr[i]>0:
		    arr[i]="big"
	print(arr)
  
big([-1, 3, 5, -5])



# Count Positives - Given an array of numbers, create a function 
# to replace last value with number of positive values. 
# Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] 
# and returns it.  (Note that zero is not considered to be a positive number).
def countPositive(arr):
    count=0
    for i in range(len(arr)):
        if arr[i]>0:
            count+=1
    arr[len(arr)-1]=count
    
    print(arr)
    
countPositive([-1,1,1,1])




# SumTotal - Create a function that takes an array as an argument
# and returns the sum of all the values in the array.  
# For example sumTotal([1,2,3,4]) should return 10
def sumTotal(arr):
	total=0
	for i in range(len(arr)):
		total+=arr[i]
	print(total)
sumTotal([1,2,3,4])

# Average - Create a function that takes an array as an argument 
# and returns the average of all the values in the array.  
# For example multiples([1,2,3,4]) should return 2.5
def average(arr):
    total=0
    avg=0
    for i in range(len(arr)):
        total+=arr[i]
    avg=total/len(arr)
    print(avg)

average([1,2,3,4])   


# Length - Create a function that takes an array as an argument 
# and returns the length of the array.  
# For example length([1,2,3,4]) should return 4
def length(arr):
	lengthArr=len(arr)
	print(lengthArr)
  
length([1,2,3,4])



# Minimum - Create a function that takes an array as an 
# argument and returns the minimum value in the array.  
# If the passed array is empty, have the function return false.  
# For example minimum([1,2,3,4]) should return 1; 
# minimum([-1,-2,-3]) should return -3.
def minimum(arr):
    minimum=arr[0]
    for i in range(len(arr)):
		    if minimum>arr[i]:
		        minimum=arr[i]

    print(minimum)

minimum([-1,-2,-3])



# Maximum - Create a function that takes an array as an argument 
# and returns the maximum value in the array.  
# If the passed array is empty, have the function return false.  
# For example maximum([1,2,3,4]) should return 4; 
# maximum([-1,-2,-3]) should return -1.
def function(arr):
    biggiest_num=arr[0]
    i=1
    if len(arr)<=1:
		    return False
    for i in range(len(arr)):
        if biggiest_num<arr[i]:
        	biggiest_num=arr[i]
    print(biggiest_num)
function([-1,-2,-3])


# UltimateAnalyze - Create a function that takes an array as an 
# argument and returns a dictionary that has the sumTotal, 
# average, minimum, maximum and length of the array.
def ultimateAnalyze(arr):
    minimum_num=arr[0]
    maximum_num=arr[0]
    total_num=0
    i=0
    for i in range(len(arr)):
        if minimum_num > arr[i]:
        	minimum_num=arr[i]
        if maximum_num < arr[i]:
        	maximum_num=arr[i]
        total_num+=arr[i]
    avg=total_num/len(arr)
    length=len(arr)
    print("minimun number is " + str(minimum_num))
    print("maximum number is " + str(maximum_num))
    print("Total value is "+ str(total_num))
    print("average number is " + str(avg))
    print("Arrey length is " + str(length))

ultimateAnalyze([1,2,3,4])


# ReverseList - Create a function that takes an array as an 
# argument and return an array in a reversed order.  
# Do this without creating an empty temporary array.  
# For example reverse([1,2,3,4]) should return [4,3,2,1]. 
# This challenge is known to appear during basic technical interviews.
def reverse(list):
    length=len(list)
    for i in range(0,length//2):
        length=length-1
        temp=list[i]
        list[i]=list[length]
        list[length]=temp
    print(list)
reverse([1,2,3,4])





# def reverseList(arr):
#     newArr=[]
#     for i in range(len(arr)-1,-1,-1):
#         newArr.append(arr[i])
#     print(newArr)

# reverseList([1,2,3,4])

# def reverse(lst):
#     i = 0            # first item
#     j = len(lst)-1   # last item
#     while i<j:
#         lst[i],lst[j] = lst[j],lst[i]
#         i += 1
#         j -= 1
#     print(lst)

# reverse([1,2,3,4])

def reverselist(list): 
    for i in range(0,len(list)//2):
        temp = list[i]
        list[i]=list[len(list)-i-1]
        list[len(list)-i-1] = temp
    return list
print(reverselist([1,2,3,4,5]))





