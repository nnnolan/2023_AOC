with open(r'1_day/input.txt') as f:
    lines = f.readlines()
    # drop \n
    lines = [line.strip() for line in lines]

print(lines)
# for line in range(len(lines)):
#     for j in lines:
final_list = []
my_list = []

numerical_values = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five" : 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

# def replace_numbers_with_words(line):
    
#     if 
    

## replace all the words with numbers
for i in range(len(lines)):
    print(lines[i])
    
    # look through the string for any of the words in the dictionary
    # make sure that it just doesn't replace the first occurence
    # replace all occurences
    
    for key, value in numerical_values.items():
        lines[i] = lines[i].replace(key, str(value))
        print(lines[i])    
    

    
for i in lines:
    # print(i)
    my_list =[]
    for j in i:
        if j.isdigit() or j in numerical_values.values():
            # print(j)
            my_list.append(int(j))
    
    # print(my_list)
    # this hwole logic should happen after each line
    
    if len(my_list) == 1:
        final_list.append( (my_list[0]*10) + my_list[0] )
        
    else:
        first_value = my_list[0] 
        last_value = my_list[-1]
        
        final_list.append( (first_value*10) + last_value )
        
    
            
            
            
        # if len(my_list) == 1:
        #     print(my_list[0])
        #     final_list.append( (my_list[0]*10) + my_list[0] )
        #     print( (my_list[0]*10) + my_list[0])
                
                
                
            
        # else:
        #     ## make my list into an iterable

            
        # ## get first value, and last value
        #     first_value = my_list[0] 
        #     last_value = my_list[-1]
        
        # ## make a number like xy , not x+y but xy
        #     number = first_value*10 + last_value
        #     print(number, first_value, last_value)
        #     # print(number)
        #     final_list.append(number)
            

# sum final_list
print(sum(final_list))
    


    
            
        
import re

number_map = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

f = open("/Users/nolanpestano/Documents/GitHub/2023_AOC/1_day/input.txt").read().strip()
for k, v in number_map.items():
    f = f.replace(k, v)

total = 0
for line in f.split("\n"):
    found = re.findall(r'\d', line)
    number_as_string = found[0] + found[-1]
    total += int(number_as_string)

print(total)