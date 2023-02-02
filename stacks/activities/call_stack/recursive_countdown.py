'''
Recursive countdown function to illustrate call stack while debugging.
'''


def countdown(n: int):

    print(n)

    if n == 0:
        return True

    else: 
        countdown(n - 1)

    
countdown(3)
