""" #Data Types
#Numbers 1,2,3
def add(x,y):
    print(x + y)
add(1,2)
#string "a,b,c"
name="Mark"
def greeting(person):
    print(person)
greeting(name)
#1 and "1" are not the same
add("1","2")
#undefined/null

#booLeans
tenure = False
def is_tenured(status):
    if(status == True):
        print("They have tenure")
    else:
        print("they are not tenured")
is_tenured(tenure) """
""" x = 3
y = float(3)
print(x,y) """
"""  """
""" """ 
""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """
""" print(values[0])
print(values[6]) """
""" 
"test"
["t","e","s","t"] """
""" """ 
""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """
""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """
""" x = "test"
print(f"hello {x}") """
""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" now=0
userword = input("Words please")
y = userword.split()
for i in y:
    now+=1
print(now)    
 """
""" 
bill = input("Bill")
tip = input("Tip")
float(bill)
int(tip)
total = float(bill) + float(tip)
print(f"total ${total}, bill ${bill}, tip ${tip}") """
""" number=128472489621
evenorodd=0
for i in range(number):
    if evenorodd < number:
        evenorodd+=2
        print(evenorodd)
if evenorodd == number:
    print("Even")
if evenorodd > number:
    print("Odd") """
""" bill = float(input("What is the bill?"))
service = input("Was it bad, okay, good , or great")
tip = 0
if service == "bad":
    print("0% tip")
    print(f"You bill is $ {bill}")
    print("You have tip $0")
elif service == "okay":
    print("15% tip")
    bill = bill * 1.15
    tip = bill * 0.15
    print(f"You bill is $ {bill}")
    print(f"You have tip $ {tip}")
elif service == "good":
    print("20% tip")
    bill = bill * 1.20
    tip = bill * 0.20
    print(f"You bill is $ {bill}")
    print(f"You have tip $ {tip}")
elif service == "great":
    print("25% tip")
    bill = bill * 1.25
    tip = bill * 0.25
    print(f"You bill is $ {bill}")
    print(f"You have tip $ {tip}") """
""" number = int(input("Give number "))
pain = 1
sadness = 0
aaa = number*number
for amom in range(aaa):
    if pain < number: 
        if sadness < number:
            sadness = sadness + pain
        if sadness == number:
            print(pain)
            pain += 1
            sadness = 0
        if sadness > number:
            pain += 1
            sadness = 0
print(number) """
""" x = int(input("First number: "))
y = int(input("Second number: "))
gcf = 0
if x >= y:
    for i in range(1, x):
        if x % i == 0:
            if y % i == 0:
                gcf = i
else:
    for i in range(1, y):
        if x % i == 0:
            if y % i == 0:
                gcf = i
print(gcf) """