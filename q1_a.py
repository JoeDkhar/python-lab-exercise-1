#defining a dataype list
num=[-1,2,3,4,55,6]
#sum of all the items of the list
Sum=0
for i in num:
    Sum+=i
print("Sum of all the numbers are::",Sum)
#product of all the items of the list
product=1
for mul in num:
    product=product*mul
print("Product of all the numbers::",product)
#to find the largest number from a list
largest=0
for index in num:
    if(index>largest):
        largest = index

print("Largest number from the list::",largest)
#to find the smallest number from a list
smallest = 0
for index in num:
    if(index<smallest):
        smallest= index

print("Smallest number from the list::",smallest)

