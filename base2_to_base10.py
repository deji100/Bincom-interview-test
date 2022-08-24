import random

def getBase10():

    baseList = [random.randint(0, 1) for _ in range(4)]

    print(f'Base List {baseList}')
    print()

    base_string = "".join([str(x) for x in baseList])
    result = int(base_string, 2)
    
    return f'Result is {result}'

print()
print(getBase10())
print()