course = 'Python for beginners'
# Length of string. len() is a generic function to find length of string or array or list
print(len(course))

# Specific function to string, these are known as methods
upper_course = course.upper()
print(upper_course)
# Find returns index
print(course.find('p'))
print(course.find('P'))
print(course.find('thon'))
print(course.replace('Python', 'Java'))
# in expression returns boolean
print('Python' in course)
print('python' in course)
