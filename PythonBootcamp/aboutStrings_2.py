# Single double and triple quotes
print('Hello World')

print("Hello 'gaming ' world")

print('''
Hello World
About gaming
how are u''')

# Multiline comments
'''
hello World
'''

# String info functions
# len
new_str = "Hello World"
print("Length of string:{}".format(len(new_str)))
# slicing
print("new_str[:4]:{}".format(new_str[:4]))
print("new_str[::2]:{}".format(new_str[::2]))
print("new_str[::-1]:{}".format(new_str[::-1]))

# String properties
# Python strings are immutable
# though u can do this
s = "Temp"
a = "a"
s = a*10
print(s)

# String built-in methods
# upper
# lower
# split

# formatting strings
print('{0:<8} | {1:^8} | {2:>8}'.format('Left', 'Center', 'Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11, 22, 33))
print(f"My 10 character, four decimal number is:{num:10.4f}")
