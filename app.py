
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

# Day 2
#Task Create a fonction to cook your favorite dish	

#favorite_dish:
#- parameters
#- methods - processes 
#- condition

def cook_favorite_dish(pasta_type, salmon_quality, cream_available, herbs=True, lemon_juice=True):
    
    if not pasta_type:
        return "You don't have any pasta, so you can't prepare this dish!"
    if not salmon_quality:
        return "You don't have any salmon"
    
    def cook_pasta():
        return f"Cook the {pasta_type} al dente in boiling salted water."
    
    def prepare_salmon():
        if salmon_quality == "fresh":
            return "Pan-sear the fresh salmon over medium heat until it's fully cooked."
        elif salmon_quality == "frozen":
            return "Thaw and then pan-sear the frozen salmon over medium heat."
        else:
            return "Cook the salmon in a pan."
    
    def prepare_sauce():
        if cream_available:
            sauce = "Prepare a cream sauce with a bit of garlic and pepper."
            if herbs:
                sauce += " Add some herbs."
            if lemon_juice:
                sauce += " Add a splash of lemon juice for balance."
            return sauce
        else:
            return "Prepare a light sauce with a little butter and lemon."
    
    def assemble_dish():
        return f"Mix the {pasta_type} with the salmon and the sauce. Serve hot."
    
    steps = [
        cook_pasta(),
        prepare_salmon(),
        prepare_sauce(),
        assemble_dish()
    ]
    
    return "\n".join(steps)

print(cook_favorite_dish(
    pasta_type="penne",
    salmon_quality="fresh",
    cream_available=True,
    herbs=True,
    lemon_juice=True
))

