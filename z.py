a="String 1"
b="String 2"
if len(a)==len(b):
    print("simialr")
else:
    False

class Customer:
    def __init__(self,name,add):
        self.name=name
        self.add=add
    def mark(self,phone):
        self.phone=phone
    def smaller(self,items):
        self.items=items
    def prices(self,price):
        self.price=price
        if price>self.items:
            price1=price*self.items
            print("what ever",price1)
details=Customer("Lara","USA")
details.mark(98094829482)
details.smaller(6)
details.prices(100)

print (details.name,details.phone,details.items,details.price)

def rever(text):
    if len(text)==0:
        return text
    else:
        return rever(text[1:])+text[0]
print (rever("Manjaro"))

list=[]
lis1="Python"
list.append("Manjaro")
print(list)

newlist=["name","number"]
addlist=["colon","pl"]

addlist.extend(newlist)
print(addlist)
