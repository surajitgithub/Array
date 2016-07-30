#MAXIMUM SUM i*arr[i] among all rotations of a given array
array=[]
num= input()
i=0
while i<num:
    item = input()
    array.append(item)
    i=i+1
print "the enterd values"
print array
i=0; in_sum=0 ; sum_values =0
while i< len(array):
   in_sum+= i*array[i]
   sum_values+=array[i]
   i+=1
i=1
print in_sum
new_sum=0
while i< len(array):
    new_sum = in_sum - sum_values + num * array[i-1]
    i+=1
    if new_sum>in_sum :
        in_sum = new_sum

print in_sum
print "is the largest sum of all the rotations possible"

