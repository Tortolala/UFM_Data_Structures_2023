from data_persistence import pickle_object, unpickle_object
from stack import Stack


# Saving object 
s = Stack(10)
s.push('A')
s.push('E')
s.push('I')
print(s)

pickle_object(s, './data_persistence/saved_stack')


# Retrieving object
s_2 = unpickle_object('./data_persistence/saved_stack')
print(s_2)
print(id(s_2))
