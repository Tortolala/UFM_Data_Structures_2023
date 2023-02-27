# Stacks 

The file `stack.py` contains the class definition of the object: *Stack*. While `test.py` holds a few operations done to demonstrate the functionality of the data structure.

## Complexities

| Method   | Time complexity | Space complexity |
|----------|-----------------|------------------|
| push()   | O(1)            | O(n)             |
| pop()    | O(1)            | O(n)             |
| peek()   | O(1)            | O(n)             |
| search() | O(n)            | O(n)             |


## Activities

### **Exercise #1: Class improvements**

Create a new version of the class definition and make the following modifications:

1) In order to avoid using the len() method to calculate the MAX value, use an attribute to keep track of it.

2) When encountering a stack overflow/underflow, the program should show a warning and continue to execute.

3) Implement the *Search(key)* method.

    Note: `test.py` must be modify to reflect the changes done.


### **Exercise #2: Reversing a List**

Create a new version of the class definition (based on the class definition resulting from the previous exercise). Then:

1) Modify the class definition so the elements in the stack are integers.

2) In `test.py`, create a list of size 10 filled with sample numbers.

3) Use a Stack instance in order reverse such list and print the result.
