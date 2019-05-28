# If you want to have single quote in string, use double quote to cover complete string
course = "Python's for beginners"
print(course)

# If you want to have double quote in string, use single quote to cover complete string
another_course = 'Python "for" beginners'
print(another_course)

# Multiline string: Use triple single/double quote
message_in_single_quote = '''
Hi Rajesh,

How are you?

Thanks!
'''
print(message_in_single_quote)

message_in_double_quote = """
Hi Arya,

How are you? Double quote!

Thanks!
"""
print(message_in_double_quote)

# String in python is like an array of chars
my_name = 'Rajesh'
print(my_name[0], my_name[1])
# Python also support negative index
print(my_name[-1])

# Square bracket also provides substring
print(my_name[0:4])
# Square bracket also provides substring all the way to last
print(my_name[3:])
# Square bracket also provides substring all the way to first
print(my_name[:4])
# Square bracket also provides substring all the way from to last
print(my_name[:])
