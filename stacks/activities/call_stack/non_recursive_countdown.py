'''
Non-recursive countdown function to illustrate call stack while debugging.
'''


def exclamation_count(num: int) -> str:

    result = str(num) + '!'
    return result


def countdown(n: int):

    while n >= 0:
        print(exclamation_count(n))
        n -= 1
    

countdown(3)
