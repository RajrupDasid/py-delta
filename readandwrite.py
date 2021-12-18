with open("rwx.text","r") as f:
    string=f.read()
    
    counts={}
    for i in string:
        counts[i]=counts.get(i,0)+1
    count={}
    for k ,v in counts.items():
        count[v]=k
    print(count)