import asyncio
from time import sleep
from datetime import datetime
#async def main():

 #   print('tim')
  #  await foo('text')
#main()
#print(main())#co rutine object
#asyncio.run(main())
#async def foo(text):
 #   print(text)
  #  await asyncio.sleep(1)
    
#asyncio.run(main())

#sroring the time at which script start executing
start=datetime.now()
def func1():
    print("NASA")
    sleep(5)
    print("Complete executing func1")
def func2():
    print("ESA")
    sleep(5)
    print("Complete executing func2")
func1()
func2()
print("Total Execution time :"+str((datetime.now())-start))

#concurrent COmputing
#Concurrent computing means executing several instructions concurrently or 
#@at the same time
start=datetime.now()
async def funcx():
    print("openSUSE")
    await asyncio.sleep(5)
    print("Complete execution funcx")
async def funcy():
    print("Manjaro")
    await asyncio.sleep(5)
    print("complete executing func y")
    
async def main():
    await asyncio.gather(funcx(), funcy())
asyncio.run(main())
print("Total execution time:"+str((datetime.now())-start))


    
