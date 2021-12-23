#reverse a function wthout using reverse
def reverse_string(text):
	if len(text)==0:
		return text
	else:
		return reverse_string(text[1:])+text[0]
print (reverse_string("Manjaro"))

#addition of given prime numbers
def addition(n):
	num=1
	sum=0
	while num<n+1:
		sum=sum+num
		num=num+1
	return sum
print(addition(5))

#word count in a string
string1="NokiaLumia"
counts={}
for i in string1:
	counts[i]=counts.get(i,0)+1
count={}
for k,v in counts.items():
	count[v]=k
print(count)

#if else even odd determination
x=13
if x%2==0:
	print("Even number ")
else:
	print("odd number")
#nested if else statement
#finding out the biggest number 

x=12
y=10
if x<y:
	print("x is less than y")
else:
	if x>y:
		print("x is greater than y")
	else:
		print("500 internal server error")		
#
