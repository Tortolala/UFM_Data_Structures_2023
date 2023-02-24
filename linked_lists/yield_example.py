'''
Yield behaviour example.
'''

def generator():

   yield 1
   yield 2
   yield 3


gen_object = generator()
print(gen_object)
print(type(gen_object))

for i in gen_object:
   print(i)
