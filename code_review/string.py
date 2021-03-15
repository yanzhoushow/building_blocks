# common errors that should be caught during code review
#  - str.replace(old, new) is not in-place operation => new_str = str.replace(old, new)
#  - str delete a char or substring is through str.replace('pattern', '')

string = 'xcdlzfdie'
new_str = string.replace('i','c')
print(new_str)                                # 'xcdlzfdce'
    
upper_str = new_str.replace('c', 'C', 1)      # 1: only replace 1 occurance from left to right
print(upper_str)                              # 'xCdlzfdce'
