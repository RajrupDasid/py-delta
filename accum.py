lst=[4,5,6,7,8]
accum=0
for i in lst:
	accum+=1
print(accum)
#accumulator pattern with conditions
phrase="What a wonderful day to program"
evl=0
for char in phrase:
	if char !=" ":
		evl=evl+1
print(evl)
#print out viowels numbers using accumulator
s="The quick brown fox jumps over the lazy dog"
x=0
for i in s:
	if i in ["a","e","i","o","u","A","E","I","O","U"]:
		x+=1
print("The string has"+ str(x) +"Numbers of viowels")
#accumulating the max value
nums=[9,8,3,6,7,8,99,77]
best_nums=0
for n in nums:
	if n>best_nums:
		best_nums=n
print(best_nums)
