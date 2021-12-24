def multiply(a,b):
	return a*b
print(multiply(6,8))

x=lambda x:x*8
print(x(8))

def reverse_string(text):
	if len(text)==0:
		return text
	else:
		return reverse_string(text[1:])+text[0]
print(reverse_string("openSUSE"))

#word count of repetation
string1="Manjaro Linux is the Best Arch based Linux"
counts={}
for i in string1:
	counts[i]=counts.get(i,0)+1
count={}
for k,v in counts.items():
	count[v]=k
print(count)
#getting out the viowels  from string
x=0
for i in string1:
	if i in ["a","e","i","o","u","A","E","I","O","U"]:
		x+=1
print(x)

list1=["Manjaro","openSUSE","Arch","Gentoo"]
list1.append("Nixos")
print(list1)