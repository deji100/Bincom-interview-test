import random

def getBase10():
    baseList = [random.randint(0, 1) for _ in range(4)]
    print(baseList)
    base_string = "".join([str(x) for x in baseList])
    result = int(base_string, 2)
    return result

print(getBase10())