def reverse_string_sol_1(string):
    reverse_string=str()
    for x in reversed(range(0,len(string))):
        reverse_string+=string[x]
    return reverse_string

def reverse_string_sol_2(string):
    reverse_string=str()
    for x in reversed(string):
        reverse_string+=x
    return reverse_string

def reverse_string_sol_3(string):
    reverse_string=str()
    for x in string[::-1]:
        reverse_string+=x
    return reverse_string

def reverse_string_sol_4(string):
    reverse_string=str()
    for x in range(len(string)-1,-1,-1):
        reverse_string+=string[x]
    return reverse_string

def reverse_string_sol_5(string,index="start",reverse_string=""):
    if index=="start":
        index=len(string)-1
        reverse_string=str()
    reverse_string+=string[index]
    if index!=0:
        reverse_string=reverse_string_sol_5(string,index-1,reverse_string)
    return reverse_string

string='banana'

print("solution 1: ",reverse_string_sol_1(string))
print("solution 2: ",reverse_string_sol_2(string))
print("solution 3: ",reverse_string_sol_3(string))
print("solution 4: ",reverse_string_sol_4(string))
print("solution 5: ",reverse_string_sol_5(string))


