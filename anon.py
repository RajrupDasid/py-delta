dob=lambda n:n*2 #doesnot take names so it called anonomus function
print(dob(10))

larger = lambda a,b: a if a>b else b
print(larger(56,77))

#double ecah number
lst=[44,66,77,99,66]
lst1=list(map(lambda x:x*2,lst))
#addition of all the numbers in the list
#lst2=list(map(lambda y:y+y,lst1))
#print(lst2)

#print(lst1)
#sort names as their length in a list
names=["Manjaro","openSUSUE","Alma","Arch"]
names.sort(key=lambda x:len(x))
print (names)

def reverse_string(text):
	if len(text)==0:
		return text
	else:
		return reverse_string(text[1:])+text[0]
print(reverse_string("Manjaro"))