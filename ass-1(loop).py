#1]
#Explain with an example each when to use a for loop and a while loop.
#A for loop is generally used when you know the exact number of times you want to repeat a certain block of code.
#It works well with sequences like lists, arrays, or known ranges.
# EX: print no 1 to 10
for i in range(1,11):
    print(i)


'''A while loop is used when you need to repeat a block of code as long as a certain condition is true.
It's suitable when you don't know in advance how many iterations will be required.
EX : Add all natural no'''
n=int(input("Enter no :"))
sum =0
i=1
while i<=n:
    sum=sum+i
    i=i+1
    print("sum = ",sum)


print("********************************************************")


#2] Using for loop to calculate the sum and product of the first 10 natural numbers
sum = 0
product = 1
for i in range (1,11):
    sum=sum+i
    product= product*i
print("forLoop:  sum =",sum,"\nproduct =",product)


print("********************************************************")


# Using while loop to calculate the sum and product of the first 10 natural numbers
o=1
sum = 0
product = 1
while o<=10:
    sum=sum+o
    product= product*o
    o=o+1
print("WhileLoop:  sum =",sum,"\nproduct =",product)

print("********************************************************")


""" Create a python program to compute the electricity bill for a household.
The per-unit charges in rupees are as follows: 
For the first 100 units, the user will be charged Rs. 4.5 per unit,
 for the next 100 units, the user will be charged Rs. 6 per unit, 
and for the next 100 units, the user will be charged Rs. 10 per unit, 
After 300 units and above the user will be charged Rs. 20 per unit.
You are required to take the units of electricity consumed in a month from the user as input..
Your program must pass this test case: when the unit of electricity consumed by the user in a month is
310, the total electricity bill should be 2250.
"""
bill=0
unit=float(input("Enter the unit:"))

if unit <= 100:
    bill = unit*4.5
    
elif unit <=200:
    bill= (100*4.5)+(100*6)    

elif unit <=300:
    bill=(100*4.5)+(100*6)+(100*10)

else :
    bill=(100*4.5)+(100*6)+(100*10)+((unit-300)*20) 

print("Bill = ",int(bill))

# **********************************************
'''
4]
Create a list of numbers from 1 to 100. 
Use for loop and while loop to calculate the cube of each
number and if the cube of that number is divisible by 4 or 5 then append that number 
in a list and print that list.

'''
list=[]
for i in range(1,101):
    cube=i**3
    if cube % 4==0 and cube % 5==0 :
      list.append(i)
print(list)

#*********************************************************