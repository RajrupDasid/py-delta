lis1=["a","b","z","c"]
lis1.sort()
lis2=["Ruuh","Lara","Max","Ben",[1,2,4,5.6]]
lis2.sort()
lis1.extend(lis2)

for i in lis1:
    if i=="Ben":
        break
    print("ben has found on pos", )

#list objects are mutabe means their values can be change in runtime
#touple are immutable objects their values cannot change on runtime 
#sets unorders
courses=["History","Math","Physics","SI"]

print(len(courses))
print (courses[0])#index location

if len(courses[0])>len(courses[1]):
    print ("0 index has a bigger length")
else:
    print("error themethod you used is useless")


#adding an item into list
courses.append("Computer Science")
print(courses)

#or we can use inset to insert an element ## insert took 2 arguments 
courses.insert(3,"Astronomy")
print(courses)


#string  manipulation
#using recursive function
def reverse_string(text):
    if len(text)==0:
        return text
    else:
        return reverse_string(text[1:])+text[0]
print(reverse_string("MathematicsAstrophysics"))

courses_2=['Art','Education']
courses.extend(courses_2)
numbers=[8,55,77,76,33,90,42,2,1]
numbers.sort(reverse=True)
courses.sort(reverse=True)
print(courses)
print(numbers)

