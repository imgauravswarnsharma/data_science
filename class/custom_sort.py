def bubble_sort(x, key = lambda x: x):
    for i in range(len(x)):
        flag = True
        for j in range(len(x)-i-1):
            if key(x[j]) > key(x[j+1]):
                x[j], x[j+1] = x[j+1], x[j]
                flag = False
        if flag:
            break
    return x

def selection_sort(x, key = lambda x: x):
    for i in range(len(x)-1):
        temp = i
        for j in range(i+1, len(x)):
            if key(x[temp]) > key(x[j]):
                temp = j
        if temp != i:
            x[temp], x[i] = x[i], x[temp]
    return x


def insertion_sort(x, key = lambda x: x):
    for i in range(1, len(x)):
        flag = True
        temp = i
        for j in range(i-1, -1, -1):
            if key(x[j]) > key(x[temp]):
                x[temp], x[j] = x[j], x[temp]
                temp = j
                flag = False
            if flag:
                break
    return x

def merge_sort(x, key = lambda x: x):
    n = len(x)
    if len(x) == 1:
        return x

    left = merge_sort(x[:len(x)//2], key)
    right = merge_sort(x[len(x)//2:] , key)

    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if key(left[i]) < key(right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j +=1
    if i == len(left):
        result += right[j:]
    if j == len(right):
        result += left[i:]

    return result