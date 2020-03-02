string = 'abcdefg'
print(string)
index = 5
print(string[index])

#string = string[:-index+1] + string[index+1:]
string = string[0:index] + string[index+1:len(string)]
print(string)