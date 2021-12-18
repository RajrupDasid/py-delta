import json

#Write file

first_name="Lara"
last_name="Croft"
semester=5
courses=['Algorithms',"Python","Assembly Language","Databases","AI"]

student_dict={
        'first_name':first_name,
        'last_name':last_name,
        'courses':courses
}

with open("students.json",mode="w") as file:
    json.dump(student_dict,file)

#read file

with open("students.json",mode="r") as file:
    studet_data=json.load(file)
#print(f"Name {studet_data['first_name']}")
