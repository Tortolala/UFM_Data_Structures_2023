
arr = [1, 2, 3, 4, 5] # Declares 'array'

for i in range(5): # Prints memory address of each element
    print('Element {} is in address: {}'.format(arr[i], id(arr[i])))
