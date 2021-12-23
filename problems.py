words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
new=[]
for i in words:
	if i =="e":
		new.append(i+"d")
	else:
		new.append(i+"ed")
print(new)
