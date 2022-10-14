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
