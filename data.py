#Data Types
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
is_tenured(tenure)