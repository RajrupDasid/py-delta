def Linux():
	print("I am studying python on Linux")
	print('openSUSE Linux')
	return 'Linux'
Linux()

def hello():
	print("Hello")
	print("Glad to meet you")
	print("Python basic class")
hello()
print("Error")
hello()

def mult(a):
	b=5*a
	return b
print (mult(7))

def add(a,b):
	c=a+b
	return c
print(add(70,90))

#def add(z=int(input("Enter a number here")),r=int(input("Enter another number here"))):
#	return "The subtraction of two number is :"+str(a+b)
#print(add())

def hello2(s):
	print('Hello'+s)
	print("Glad to meet you")
hello2("Lara"+"and Ruuh")

def cyu(s1,s2):
	if len(s1)>len(s2):
		print(s1)
	else:
		print(s2)
cyu("Hello","Good Bye")
cyu("Manjaro","openSUSE")

def square(x):
	y=x*x
	return y
tosquare=10
result=square(tosquare)

#n=lambda a:a*b
#=n[8]

#Program to filter out only the even number items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list=list(filter(lambda x:(x%2==0),my_list ))

print(new_list)
#program to doule each item in a list using map

lista=list(map(lambda x:x*2,my_list))
print(lista)
