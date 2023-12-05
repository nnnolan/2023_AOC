import re

with open(r'3_day/input.txt') as f:
    lines = f.readlines()
    
    lines = [line.strip() for line in lines]
    
def use_regex_nums(input_text):
    pattern = re.compile(r"\.\.342\.\.\.\.886\.\.\.\.122\.\.[A-Za-z0-9]+\.\.866\.\.\.\.\.\.\.\.438\.\.\.\.\*\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\*\.\.\.\.\.\.\.\.739\.\.\.716\.\.\.131\.\.\.\.561\.\.748\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.206\.\.\.\.\.\.155\.\.\.", re.IGNORECASE)
    return pattern.match(input_text)
    

symbols = []
for line in lines:
    symbols.append(re.findall(r'[^.0-9', line))
        
nums = []
for line in lines:

    

    


print(symbols)
print(nums)
