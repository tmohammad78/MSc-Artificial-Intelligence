first_name = "Mohammad"
last_name = "Taheri"
full_name = f"Hello Mr {first_name} {last_name}" # f-string , f means format()
print(full_name)
sample_strip="   this is with space"
print(sample_strip.lstrip())

CONST_VARIABLE = 5000 #This is sample const variable that shouldn't be changed 

sample_list = [1,24,24,5,6,7,34,67]
sample_list.append(37)
print(sample_list) #[1, 24,24, 5, 6, 7, 34, 67, 37]

sample_list.remove(24)  #remove one of them

del sample_list[0]

print(sample_list) # [24,5, 6, 7, 34, 67, 37]

sample_list.insert(4, "34")

print(sample_list) # [24,1, 5, 6, 7, '34', 34, 67, 37]

sample_list.reverse()

print(len(sample_list))


for item in sample_list:
    print(f'item: {item}') # This is indentation of language , spaces

another_list = list(range(1,7))

another_list_add_two = list(range(1,7,2))

squares = [value ** 2 for value in range(1,11)]

print(squares)

new_list = squares[2:5] # from index 2 to index 4 (is included)

print(new_list)
print(squares[-3:]) # last three items 

copy_list = squares[:] # Copy the array , with different refrences
same_list = squares # has same refrences 
squares.append(300)

print(same_list,copy_list) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 300] , [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

dimesions = (2,2) # this is tuple , tuple is an immutable list 

print(dimesions[1])

# dimesions[1] = 4 # TypeError: 'tuple' object does not support item assignment
# for changing value we should replace all of them

dimesions = (4,5)

#### Python Enhancement Proposal (PEP).
# PEP 8 : Should use 4 space for Indentation

print(4 in dimesions) # True

if 7 not in dimesions:
    print("7 not exist")

a = list()

if a:
    print("a is not empty")
else:
    print("a is empty")

#### Dictionary is like objects , key value 
alien_0 = {'color': 'green', 'points': 5} # Sample dictionary
print(alien_0['color'],'it should be green')

del alien_0["points"]

print(alien_0,"it hasn't points key")
alien_0["name"] = "ali"

for key,value in alien_0.items():
    print(f'{key}:{value}')

for key in alien_0.keys():
    print(f'key: {key}')

for value in alien_0.values():
    print(f'value: {value}')

alien_0["test"] = "ali"
alien_0["test1"] = "ali"
alien_0["test1"] = "ali"

print("##########")

for value in set(alien_0.values()): # In js we use set for delete duplicated value too .
    print(f'value is: {value}')


def sumFn(a,b):
    return a 

sumFn(10,2) ## 12

def sampleFn(fName,lName,**others): ### ** combines other inputs as dictionary , * combines them at tuple 
    print(others)
    desc = f'Hi {fName} {lName}'
    if 'age' in others:
        desc += " " + f'my age is {others["age"]}'
    return desc

def sampleFn2(fName,lName,*others): ### ** combines other inputs as dictionary , * combines them at tuple 
    print(others)
    result = 0
    desc = f'Hi {fName} {lName}'
    for a in others:
        result += a
    if result > 0:
        desc += f' salary is {result}'
    return desc


print(sampleFn2("Mohammad","Taheri" , 20 , 30 , 4 ))
print(sampleFn2("Ali","Hosseini"))


############ Module 

from utils import sumBy5,printText ### Or import utils , and call function : utils.sumBy5(10)
printText(sumBy5(10)) ### 15 

# ### We can import all function in this way 
# from utils import * 

# test()

##### alise 
# import utils as ut

# from utils import sumBy5 as sm
# sm(20)

#### PEP 8 Convention of functions 
# def function_name(
# parameter_0, parameter_1, parameter_2,
# parameter_3, parameter_4, parameter_5):
# function body...