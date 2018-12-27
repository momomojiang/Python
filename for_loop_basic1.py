# Basic - Print all the numbers/integers from 0 to 150.
for count in range(1,150):
	print(count)
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.
for i in range(5,1000000+1):
	if i%5==0:
	    print(i)


# Counting, the Dojo Way - Print integers 1 to 100.  
# If divisible by 5, print "Coding" instead. 
# If by 10, also print " Dojo".
for i in range(1,101):
  if i%10==0:
      print("coding dojo") 
       
  if i%5==0 and i%10!=0:
      print("coding")
      

# Whoa. That Sucker is Huge 
# - Add odd integers from 0 to 500,000, and print the final sum.
sum=0
for i in range(0,500000+1):
    if i%2==1:
    	sum=sum+i
print(sum)

# Countdown by Fours - 
# Print positive numbers starting at 2018, 
# counting down by fours (exclude 0).
def countdown(i):
	while i > 0:
		print(i)
		i=i-1
		if i ==0:
			break
countdown(2018)


# Flexible Countdown - 
# Based on earlier "Countdown by Fours", 
# given lowNum, highNum, mult, print multiples of 
# mult from lowNum to highNum, using a FOR loop.  
# For (2,9,3), print 3 6 9 (on successive lines)
mult = 3
for i in range(9,0,-1):
    if i % mult==0:
        print(i)


