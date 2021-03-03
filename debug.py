'''dstring=input('how far did you travel today(in miles)?')
tstring=input('how long did it take you(in hours)?')
dfloat=float(dstring)
tfloat=float(tstring)
s=dfloat/tfloat
print('your speed was ', s, "miles per hour")


for i in range(1,11):
    print(i)

for i in range(10,0,-1):
    print(i)

for i in range(2,50,2):
    print(i)

          #write a program to print a no.  check each no. wether each no. is even?

for i in range(0,100,2):
    print(i)
    if i%2==0:
        print('it is even number')


for i in range(4):
    if i==2:
        break
    print(i)

for val in "string":
     if val =="i":
         break
     print(val)
print("End")


fruits=["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x=="banana":
        break


fruits=["apple", "banana", "cherry"]
for x in fruits:
    if x=="banana":
        continue
    print(x)



i=0 # initilization
while i<=10: # conditional
    print(i)
    i=i+1 # stepping
print("program is over")

i=10
while i>=1:
    print(i)
    i=i-1
print("program is over")
'''
#write a program to print all the odd and even number with appropriate message from 1 to 50?n Using while loop.

'''
i=1
while 1<=50:
    if i%2==0:
        print(i, 'the number is even')
    else:
        print(i, 'the number is odd')
    i=i+1
'''
#write a program to find the sum of elements of list using while loop.
# 1st=[10,31,37,40,56,63,70]
#using for loop
'''
listi=(10,31,37,40,56,63,70)
sum=0
for i in listi:
    sum=sum+i
print('the sum is ', sum)
'''
#another method
lst=[10,31,37,40,56,63,70]
l=len(lst)
sum=0
for i in range(l):
     sum =sum+lst(l)
print('the sum is' , sum)
