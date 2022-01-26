from asyncio import coroutines
from audioop import reverse

# Video: https://www.youtube.com/watch?v=W8KRzm-HUcc&t=28s
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

# ##### Tuple 
# This is Mutable 
'''
list_1 = ['math', 'physics','history', 'compSci']
list_2 = list_1
list_1[0] = 'Art'
# Notice how ART changed.
['Art', 'physics', 'history', 'compSci']
['Art', 'physics', 'history', 'compSci']

print(list_2)
print(list_1)


# Immutable ... This is what a Tuple is.
tuple_1 = ('math', 'physics','history', 'compSci')
tuple_2 = tuple_1

# If we try to change it, we get error.
tuple_1[0] = 'Art'
#  TypeError: 'tuple' object does not support item assignment

# Tuples Can not be modified. Much better to use a List instead. Tuple give you quick access.
#  But uses all the same methods as LISTs
print(tuple_1)
print(tuple_2)
'''

# SETS.
cs_course = {'math', 'physics','history', 'compSci'}
art_course = {'math', 'physics','history', 'design'}
#  There Order changes, because order doesn not matter. 
#  It will not allow duplicates
'''
print(cs_course)
print('math' in cs_course) #=> true
#  What Course two set have in common. 
# course the both have in common
print(cs_course.intersection(art_course)) # {'history', 'physics', 'math'}

# Course Different between 2 sets
print(cs_course.difference(art_course)) # {'compSci}

# Join both courses together
print(cs_course.union(art_course)) # {'physics', 'history', 'math', 'compSci', 'design'}
'''

# Create and empty List
empty = []
# Create empty Tuples
empty = ()

# Create empty Sets
empty_set = {}
# or
empty_set = set()

