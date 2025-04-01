
#exemple 

a = 10
b = 5

c = a - b
d = a * b
e = a / b
f = a % b

print("c =", c)
print("d =", d)
print("e =", e)
print("f =", f)

name = "aurelien "
surname = "Goron"

student_name = name + " " + surname
print(student_name)


#Task 
# 1. Write If Else statement to validate if x is larger than y return true if yes

x = 10
y = 5

if (x > y):
    print("True")
else:
    print("False")

# exemple avec une fonction

def eval(x,y):
    if y > x:
        return True
    return False

print(eval(100,200))
# 2. write IF ELSE statment to validate if x is larger tgan y and less than b return true

x = 10
y = 5
b = 12

if (x > y && b > x):
    print("True")
else:
    print("False")

