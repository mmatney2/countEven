


def countEven(num):
    result = 0
    for i in range(1, num+1):
        new = [int(c) for c in str(i)]
        print(new)
        if sum(new) % 2 ==0:
            result += 1
    return result
print(countEven(30))
