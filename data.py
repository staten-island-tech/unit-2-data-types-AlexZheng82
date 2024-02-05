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
number=1284
evenorodd=0
for i in range(number):
    evenorodd+=2
    print(evenorodd)
    if evenorodd == number:
        print("Even")
    if evenorodd > number:
        print("Odd")