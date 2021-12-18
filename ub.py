string="In computing, a server is a piece of computer hardware or software (computer program) that provides functionality for other programs or devices, called clients This architecture is called the client–server model. Servers can provide various functionalities, often called services, such as sharing data or resources among multiple clients, or performing computation for a client"
counts={}
for i in string:
    counts[i]=counts.get(i,0)+1
count={}
for k,v in counts.items():
    count[v]=k
print(count)