from asyncio import coroutines
from audioop import reverse

# NOTE:  course was changed to courses at the last mins
courses = ['math', 'physics','history', 'compSci']
'''
# length
print(len(courses))
# choose by index to get the last Item always.
print(course[-1]) #compSec
print(course[0:2])# will not include what is at 2 index
print(course[2:])# will start from 2 index to the end

# Add art to list
course.append('ART')
# Insert at a specific locaiton
course.insert(3,'ART')
print(course)

# What to extend our List

course_2 = ['education', 'workshop']
course.extend(course_2)
print(course)

# REMOVE form our list
course.remove('math') #=>['Physics', 'History', 'compSci']
course.pop('math') #=>remove last value in our list removing 'compSci' and return remove values.

# course.reverse()
course.sort() # sort alphabitcally order. If Number, In numerical number
course.sort(reverse=True) # sort in decending order.. 
# Get a sorted version of the List without effect to the orginal You say
sorted_course = sorted(course)
'''


nums = [2,1,23,4,2]
'''
print(max(nums)) #=> 23
print(min(nums)) #=> 1
print(sum(nums)) #=> 32

'''

'''
# Find the index of item 
print(course.index('compSci')) #=> 3
#  Check if it list
print('math' in course)
'''

# Iteration
'''
for course in courses:
    print(course)
    
    # Use the enumerator
'''

'''
for index, course in enumerate(courses):

    0 math
1 physics
2 history
3 compSci
    # print(index, course)
    '''
# If you wanna start at the value of 1
'''
for index, course in enumerate(courses, start=1):
    1 math
2 physics
3 history
4 compSci
    # print(index, course)
'''

'''

#  Turn List into String

course_str = ', '.join(courses)
# or
# course_str = '- '.join(course)

# Then Make a string into a list
new_list = course_str.split(' - ')
print(new_list)
'''

#  Tuple and Sets.
