from data_persistence.data_persistence import unpickle_object


saved_stack = unpickle_object('./test_stack')
print('\nLength of saved stack: {}'.format(saved_stack.top))
